/*
 * process.c
 *
 *  Created on: Sep 20, 2024
 *      Author: albve
 */

#include <SIM7000.h>
#include "process.h"
#include "main.h"
#include "global_variables.h"
#include "peripherals.h"
#include "INA3221.h"
#include "DS18B20.h"
#include "stdio.h"
#include "string.h"
#include "FatFs/ff.h"
#include "psram.h"
#include "stdlib.h"
#include "battery_charger.h"
#include "leds.h"
#include "base64.h"
#include "init.h"


/*-----ACQUISIZIONE MISURE E LOG DEI DATI-----*/
void Save_Data(void)
{
	if(flags.ADC_Half_Buffer)
	{
		memcpy(Saving_Buffer + Address_Offset, &Pressure[0], PRESS_HALF_LEN);
		Last_Pressure = 0;
		for(int i = 0; i < PRESS_HALF_SAMPLES; i++)
		{
			Last_Pressure += Pressure[i];
		}
		Last_Pressure = (uint16_t)(Last_Pressure / PRESS_HALF_SAMPLES);
		Warning_Detection(&Pressure[0]);
		flags.ADC_Half_Buffer = 0;
	}
	else if(flags.ADC_Full_Buffer)
	{
		memcpy(Saving_Buffer + Address_Offset, &Pressure[PRESS_HALF_SAMPLES], PRESS_HALF_LEN);
		Last_Pressure = 0;
		for(int i = PRESS_HALF_SAMPLES; i < PRESS_FULL_SAMPLES; i++)
		{
			Last_Pressure += Pressure[i];
		}
		Last_Pressure = (uint16_t)(Last_Pressure / PRESS_HALF_SAMPLES);
		Warning_Detection(&Pressure[PRESS_HALF_SAMPLES]);
		flags.ADC_Full_Buffer = 0;
	}
	flags.ADC_Complete = 0;
	Address_Offset += PRESS_HALF_LEN;

	uint8_t current_period_cnt = Period_cnt;
	Last_Volume = 0;
	for(int i = 0; i < current_period_cnt; i++)
	{
		Last_Volume += Volume_Period[i];
	}
	if(current_period_cnt != 0)
	{
		Last_Volume = (uint32_t)(Last_Volume / current_period_cnt);
	}
	Volume_Average_Buffer[Volume_Avg_Cnt] = Last_Volume;
	Last_Volume = 0;
	Volume_Avg_Cnt++;
	uint8_t NonZero_samples = 0;
	for(int i = 0; i < (config.samp_freq / ACC_FIFO_WATERMARK); i++)
	{
		if(Volume_Average_Buffer[i] != 0)
		{
			NonZero_samples++;
			Last_Volume += Volume_Average_Buffer[i];
		}
	}
	Last_Volume = (uint32_t)(Last_Volume / NonZero_samples);
	memset(Volume_Period, 0, sizeof(Volume_Period));
	if(Volume_Avg_Cnt >=  (config.samp_freq / ACC_FIFO_WATERMARK))
	{
		Volume_Avg_Cnt = 0;
	}
	Period_cnt = 0;
	memcpy(Saving_Buffer + Address_Offset, &Last_Volume, sizeof(uint32_t));
	Address_Offset += sizeof(uint32_t);

	if(sys.ACC_Present)
	{
		memcpy(Saving_Buffer + Address_Offset, Acceleration, ACCELERATION_LEN);
		int32_t temp_x = 0;
		int32_t temp_y = 0;
		int32_t temp_z = 0;
		for(int i = 0; i < ACCELERATION_LEN; i += 7)
		{
			temp_x += Acceleration[i+1] | (Acceleration[i+2] << 8); 
			temp_y += Acceleration[i+3] | (Acceleration[i+4] << 8);
			temp_z += Acceleration[i+5] | (Acceleration[i+6] << 8);
		}
		Last_Acceleration.x = (uint16_t)(temp_x / ACC_FIFO_WATERMARK);
		Last_Acceleration.y = (uint16_t)(temp_y / ACC_FIFO_WATERMARK);
		Last_Acceleration.z = (uint16_t)(temp_z / ACC_FIFO_WATERMARK);
		flags.ACC_Complete = 0;
	}
	Address_Offset += ACCELERATION_LEN;

	INA3221_Read_Measure(&Supply);
	uint16_t new_temp = 0;
	if((new_temp = Read_Temperature()) != 0)
	{
		Temperature = new_temp;
	}
	BC_MultiRead_Reg(REG3B_VBAT_ADC, &Vbatt);

//	__disable_irq();
	Compressed_Sample_Typedef sample;
    sample.compressed_size = Compress_Sample(Saving_Buffer, SAVING_BUFFER_LEN, compressed_data);
	RAM_Save_Measure(&sample, compressed_data);
//	__enable_irq();

	Address_Offset = 0;

	if(flags.Hammer_Detected || flags.Threshold_Detected)
	{
		Cycles_After_Warning++;
		if(Cycles_After_Warning >= config.buffering_secs * (config.samp_freq / ACC_FIFO_WATERMARK))
		{
			if(!flags.CMD.Measure_Request)
			{
				if (!flags.Meas_TransferInProgress)
				{
					LED_Start(RED_LED, FAST, LOW);
					Switch_Buffer();
					flags.CMD.Measure_Request = 1;
					Send_Measure_Addr = 0;
					Cycles_After_Warning = 0;
					if(flags.Hammer_Detected)
					{
						flags.Hammer_Detected = 0;
					}
					if(flags.Threshold_Detected)
					{
						flags.Threshold_Detected = 0;
					}
				}
				
			}
		}
	}

}

/*-----CAMBIO BUFFER-----*/
void Switch_Buffer(void)
{
	__disable_irq();
    uint32_t temp_add = sys.Current_RAM_Address;
    uint32_t temp_len = sys. Current_RAM_Len;
    sys.Inactive_RAM_Address = temp_add;
    sys.Inactive_RAM_Len = temp_len;

    if (sys.Active_RAM_Buffer == 0) 
	{
		sys.Inactive_RAM_Base = RAM_FIRST_BUFFER_ADD;
        sys.Active_RAM_Buffer = 1;
        sys.Current_RAM_Base = RAM_SECOND_BUFFER_ADD;
    } 
	else 
	{
		sys.Inactive_RAM_Base = RAM_SECOND_BUFFER_ADD;
        sys.Active_RAM_Buffer = 0;
        sys.Current_RAM_Base = RAM_FIRST_BUFFER_ADD;
    }

    sys.Current_RAM_Address = 0;
    sys.Current_RAM_Len = 0;
	__enable_irq();
}

/*-----CANCELLAZIONE DATI RAM-----*/
void Erase_RAM_Data(void)
{
	uint8_t zero_buffer[1024] = {0};
	for (uint32_t addr = 0; addr < 0x800000; addr += sizeof(zero_buffer)) 
	{
		RAM_Write(addr, sizeof(zero_buffer), zero_buffer);
	}
}


/*-----AVVIO MISURA-----*/
void Start_Measure(void)
{
	Erase_RAM_Data();
	sys.RAM_Samples_Number = (config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * 2;
	sys.Active_RAM_Buffer = 0;
	sys.Inactive_RAM_Address = 0;
	sys.Current_RAM_Base = RAM_FIRST_BUFFER_ADD;
	sys.Current_RAM_Address = 0;
	flags.SIM_isConnected = 1;
	memset(Pressure, 0, sizeof(Pressure));
	memset(Volume_Period, 0, sizeof(Volume_Period));
	memset(Volume_Average_Buffer, 0, sizeof(Volume_Average_Buffer));
	memset(Acceleration, 0, sizeof(Acceleration));
	memset(&Supply, 0, sizeof(Supply));
	Volume_Avg_Cnt = 0;
	Temperature = 0;
	Saved_Bytes = 0;
	Saved_Samples = 0;
	Address_Offset = 0;
	Cycles_After_Warning = 0;
	Measure_Bytes_Sent = 0;
	Clear_Flags();

	ADC_TIMER->Instance->PSC = 100 - 1;
	ADC_TIMER->Instance->ARR = (uint32_t)(SystemCoreClock / ((ADC_TIMER->Instance->PSC + 1) * config.samp_freq)) - 1;
	ACC_TIMER->Instance->ARR = (uint32_t)(config.samp_freq / 25) - 1;
	ACC_TIMER->Instance->CCR3 = (uint32_t)((ACC_TIMER->Instance->ARR + 1) / 2);
	if(Acc_Init(&acc, config.samp_freq) != HAL_OK)
	{
		state = IDLE;
		return;
	}

	lsm6dsv16x_fifo_mode_set(&acc, LSM6DSV16X_STREAM_MODE);
	HAL_ADC_Start_DMA(PRESSURE_ADC, (uint32_t*)&Pressure, PRESS_FULL_SAMPLES);
	HAL_TIM_IC_Start_IT(VOLUME_TIMER, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(ACC_TIMER, TIM_CHANNEL_3);
	HAL_TIM_Base_Start(ADC_TIMER);
}

/*-----FINE MISURA-----*/
void Stop_Measure(void)
{
	__disable_irq();
	HAL_ADC_Stop_DMA(PRESSURE_ADC);
	HAL_TIM_Base_Stop(ADC_TIMER);
	HAL_TIM_PWM_Stop(ACC_TIMER, TIM_CHANNEL_3);
	HAL_TIM_IC_Stop_IT(VOLUME_TIMER, TIM_CHANNEL_1);
	lsm6dsv16x_fifo_mode_set(&acc, LSM6DSV16X_BYPASS_MODE);
	__enable_irq();
}

/*-----DETECTION COLPO D'ARIETE-----*/
void Warning_Detection(uint16_t* Data)
{
	uint16_t max = Data[0];
	uint16_t min = Data[0];

	for(int i = 1; i < PRESS_HALF_SAMPLES; i++)
	{
		if(Data[i] > max)
		{
			max = Data[i];
		}
		else if(Data[i] < min)
		{
			min = Data[i];
		}

		if(Data[i] < sys.Low_th || Data[i] > sys.High_th)
		{
			flags.Threshold_Detected= 1;
		}
	}

	if(max - min >= config.hammer_th)
	{
		flags.Hammer_Detected = 1;
	}

}

/*-----SALVATAGGIO MISURA IN RAM-----*/
void RAM_Save_Measure(Compressed_Sample_Typedef* sample, uint8_t* compressed_data)
{
    uint32_t samples_size = sample->compressed_size.pressure_size +
                            sample->compressed_size.volume_size +
                            sample->compressed_size.acceleration_size;
    uint32_t total_size = METADATA_SIZE + samples_size;
	uint8_t aligned_metadata[8] __attribute__((aligned(4))) = {0};

    // Copia SOLO i 6 bytes necessari
    aligned_metadata[0] = sample->compressed_size.pressure_size & 0xFF;
    aligned_metadata[1] = sample->compressed_size.pressure_size >> 8;
    aligned_metadata[2] = sample->compressed_size.volume_size & 0xFF;
    aligned_metadata[3] = sample->compressed_size.volume_size >> 8;
    aligned_metadata[4] = sample->compressed_size.acceleration_size & 0xFF;
    aligned_metadata[5] = sample->compressed_size.acceleration_size >> 8;

    // Controllo corruzione
    if (sys.Current_RAM_Address >= (RAM_SECOND_BUFFER_ADD - RAM_FIRST_BUFFER_ADD)) 
	{
    	sys.Current_RAM_Len = sys.Current_RAM_Address;
        sys.Current_RAM_Address = 0;
        Saved_Bytes = 0;
        Saved_Samples = 0;
    }

    // ========= LOGICA CIRCOLARE (PRIORITARIA) =========
    if(Saved_Samples >= sys.RAM_Samples_Number) 
	{
        // RESET CIRCOLARE - riparti dall'inizio dello stesso buffer
    	sys.Current_RAM_Len = sys.Current_RAM_Address;
        sys.Current_RAM_Address = 0;
        Saved_Bytes = 0;
        Saved_Samples = 0;
    }

    uint32_t address = sys.Current_RAM_Base + sys.Current_RAM_Address;

    // Controllo overflow SOLO se non siamo in modalità circolare
    if (sys.Current_RAM_Address + total_size > (RAM_SECOND_BUFFER_ADD - RAM_FIRST_BUFFER_ADD)) 
	{
    	sys.Current_RAM_Address = 0;
		Saved_Bytes = 0;
		Saved_Samples = 0;
    }

    // Salvataggio normale
    RAM_Write(address, METADATA_SIZE + 2, aligned_metadata);
    address += METADATA_SIZE;
	if(samples_size % 4 != 0)
	{
		uint32_t padding_size = 4 - (samples_size % 4);
		memset(compressed_data + samples_size, 0xFF, padding_size);
		samples_size += padding_size;
		total_size += padding_size;
	}
    RAM_Write(address, samples_size, compressed_data);
    
    Saved_Bytes += total_size;
    sys.Current_RAM_Address += (METADATA_SIZE + SAVING_SAMPLE_SIZE);
    Saved_Samples++;
}

/*-----INVIO CHUNK MISURA-----*/
uint32_t Send_Measure_Chunk(uint32_t buffer_base, uint32_t buffer_len, uint32_t start_address)
{
    uint32_t raw_fill = 0;
    uint8_t raw_buffer[1100];
    uint32_t address = buffer_base + start_address;

    // Controllo base
    if (start_address >= (RAM_SECOND_BUFFER_ADD - RAM_FIRST_BUFFER_ADD))
    {
        return (uint32_t)-1;  // Parametri non validi
    }

    do 
    {
        // Chunk pieno per metadata
        if ((raw_fill + METADATA_SIZE) > sizeof(raw_buffer)) 
        {
            break;  // Chunk pieno, invia
        }

        if(address == buffer_base + buffer_len)
        {
        	address = buffer_base;
        }

        // ========= LETTURA METADATA =========
        Compressed_Sample_Typedef sample_header;
        RAM_Read(address, METADATA_SIZE, (uint8_t*)&sample_header);

        uint32_t sample_size = sample_header.compressed_size.pressure_size +
                               sample_header.compressed_size.volume_size +
                               sample_header.compressed_size.acceleration_size;

        // ========= VALIDAZIONE SAMPLE =========
        if (sample_size == 0 || sample_size > MAX_COMPRESSED_SIZE ||
            sample_header.compressed_size.pressure_size > 500 ||
            sample_header.compressed_size.volume_size > 100 ||
            sample_header.compressed_size.acceleration_size > 1000) 
        { 
            break;
        }

        uint32_t sample_total_size = METADATA_SIZE + sample_size;

        // Chunk non può contenere questo sample
        if ((raw_fill + sample_total_size) > sizeof(raw_buffer)) 
        {
            break;  // Invia chunk corrente
        }

        // ========= COPIA METADATA =========
        memcpy(raw_buffer + raw_fill, (uint8_t*)&sample_header, METADATA_SIZE);
        raw_fill += METADATA_SIZE;
        address += METADATA_SIZE;

        // ========= COPIA DATI SAMPLE =========
        RAM_Read(address, sample_size, raw_buffer + raw_fill);
        raw_fill += sample_size;
        address += SAVING_SAMPLE_SIZE;

    } while (1);

    //  INVIO CHUNK (se contiene dati)
    if (raw_fill > 0) 
    {
        size_t b64_len = Base64_Encode(raw_buffer, raw_fill, (char*)tcp_chunk, sizeof(tcp_chunk));
        SIM_Send_TCP_Chunk(b64_len);
        return (address - buffer_base);  // Prossimo indirizzo
    }

    // Nessun dato processato
    return (uint32_t)-1;
}

/*-----COMPRESSIONE DATI-----*/
Compressed_Sizes_Typedef Compress_Sample(uint8_t *input, uint16_t input_len, uint8_t *output)
{
	uint16_t out_idx = 0;
	uint8_t packed_byte = 0;
	Compressed_Sizes_Typedef sizes = {0, 0, 0};

    AdpcmState_Typedef press_state = {0, 0};
    AdpcmState_Typedef acc_x_state = {0, 0}, acc_y_state = {0, 0}, acc_z_state = {0, 0};

	// --- 1. Pressione ---
	uint16_t *adc = (uint16_t*)input;
	uint16_t pressure_start = out_idx;

	output[out_idx++] = adc[0] & 0xFF;
	output[out_idx++] = adc[0] >> 8;
	press_state.previous_value = adc[0];
	for (int i = 1; i < PRESS_HALF_SAMPLES; i++) 
	{
		uint8_t nibble = ADPCM_Compression(adc[i], &press_state, step_size_table_12bit, index_adjustment_table_press);
		if (i % 2 != 0) 
		{
			packed_byte = nibble;
		} else 
		{
			packed_byte |= (nibble << 4);
			output[out_idx++] = packed_byte;
			packed_byte = 0;
		}
	}

	if ((PRESS_HALF_SAMPLES - 1) % 2 != 0) 
	{
		output[out_idx++] = packed_byte;
		packed_byte = 0;
	}
	sizes.pressure_size = out_idx - pressure_start;

	// --- 2. Flusso (Ultimo Valore) ---
	uint32_t *counter = (uint32_t*)(input + PRESS_HALF_LEN);

	output[out_idx++] = counter[0] & 0xFF;
	output[out_idx++] = (counter[0] >> 8) & 0xFF;
	output[out_idx++] = (counter[0] >> 16) & 0xFF;
	output[out_idx++] = (counter[0] >> 24) & 0xFF;

	sizes.volume_size = 4;		

	// --- 3. Accelerometro (3 canali separati) ---
	uint8_t *accel = input + PRESS_HALF_LEN + VOLUME_LEN;
	uint16_t accel_start = out_idx;

	uint16_t x0 = accel[1] | (accel[2] << 8);
	uint16_t y0 = accel[3] | (accel[4] << 8);
	uint16_t z0 = accel[5] | (accel[6] << 8);
	acc_x_state.previous_value = x0;
	acc_y_state.previous_value = y0;
	acc_z_state.previous_value = z0;
	for(int k=0; k<7; ++k) output[out_idx++] = accel[k];
	for (int i = 1; i < ACC_FIFO_WATERMARK; i++) 
	{
		uint16_t x = accel[i*7+1] | (accel[i*7+2] << 8);
		uint16_t y = accel[i*7+3] | (accel[i*7+4] << 8);
		uint16_t z = accel[i*7+5] | (accel[i*7+6] << 8);
		uint8_t nibble_x = ADPCM_Compression(x, &acc_x_state, step_size_table_16bit, index_adjustment_table_acc);
		uint8_t nibble_y = ADPCM_Compression(y, &acc_y_state, step_size_table_16bit, index_adjustment_table_acc);
		uint8_t nibble_z = ADPCM_Compression(z, &acc_z_state, step_size_table_16bit, index_adjustment_table_acc);
		output[out_idx++] = nibble_x | (nibble_y << 4);
		output[out_idx++] = nibble_z;
	}
	sizes.acceleration_size = out_idx - accel_start;

	return sizes;
}

/*-----FUNZIONE DI COMPRESSIONE ADPCM-----*/
uint8_t ADPCM_Compression(int16_t sample, AdpcmState_Typedef* state, const uint16_t* step_size_table, const int8_t* index_adjustment_table) 
{
    int32_t diff = (int32_t)sample - state->previous_value;
    uint16_t step = step_size_table[state->step_index];
    uint8_t nibble = 0;

    if (diff < 0) 
    {
        nibble = 8; // Bit di segno
        diff = -diff;
    }

    if (step == 0) step = 1;
    
    // Calcola il nibble quantizzato
    uint32_t temp = (uint32_t)diff * 4;
    if (temp < step) 
    {
        nibble |= 0;
    } 
    else 
    {
        nibble |= (uint8_t)((temp / step > 7) ? 7 : (temp / step));
    }

    // Ricostruisci il valore per la predizione successiva (usando solo il nibble)
    int32_t reconstructed_diff = (step * (nibble & 7)) / 4 + step / 8;
    if (nibble & 8) {
        reconstructed_diff = -reconstructed_diff;
    }
    
    state->previous_value += reconstructed_diff;

    // CLAMP DINAMICO BASATO SULLA LUT
    if (step_size_table == step_size_table_12bit) 
    {
        // Dati 12-bit ADC: unsigned 0-4095
        if (state->previous_value > 4095) state->previous_value = 4095;
        if (state->previous_value < 0) state->previous_value = 0;
    } 
    else if (step_size_table == step_size_table_16bit) 
    {
        // Dati 16-bit accelerometro: signed -32768 to +32767
        if (state->previous_value > 32767) state->previous_value = 32767;
        if (state->previous_value < -32768) state->previous_value = -32768;
    }

    state->step_index += index_adjustment_table[nibble & 7];
    if (state->step_index < 0) state->step_index = 0;
    if (state->step_index > 87) state->step_index = 87;

    return nibble;
}


/*-----APPLICA VALORI CONFIGURAZIONE-----*/
void Apply_Config(void)
{
	FIL config_file;
	UINT bytes_written;
	
	if(strcmp(cfg_var, "DEVICE_ID") == 0) 
	{
		config.device_id = (uint8_t)atoi(new_cfg_val);
    }
	else if(strcmp(cfg_var, "SAMP_FREQ") == 0)
	{
		if((uint16_t)atoi(new_cfg_val) != 800 && (uint16_t)atoi(new_cfg_val) != 1600)
		{
			SIM_Send_TCP("R:ERR");
			return;
		}
		else
		{
			if(((config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * SAVING_BUFFER_LEN) * 2 > psram_get_size()) 
			{
				config.samp_freq = (uint16_t)atoi(new_cfg_val);
			}
			else
			{
				SIM_Send_TCP("R:ERR");
				return;
			}
		}
	}
	else if(strcmp(cfg_var, "BUFFER_SECS") == 0)
	{
		if((uint8_t)atoi(new_cfg_val) < 5 || (uint8_t)atoi(new_cfg_val) > 30)
		{
			SIM_Send_TCP("R:ERR");
			return;
		}
		else
		{
			if(((config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * SAVING_BUFFER_LEN) * 2 > psram_get_size()) 
			{
				config.buffering_secs = (uint8_t)atoi(new_cfg_val);
			}
			else
			{
				SIM_Send_TCP("R:ERR");
				return;
			}
		}
	}
	else if(strcmp(cfg_var, "CONN_TIMEOUT") == 0)
	{
		config.connection_timeout_ms = (uint32_t)atoi(new_cfg_val);
	}
	else if(strcmp(cfg_var, "LOG_PERIOD") == 0)
	{
		config.log_period_ms = (uint32_t)atoi(new_cfg_val);
	}
	else if(strcmp(cfg_var, "HAMMER_TH") == 0)
	{
		config.hammer_th = (uint16_t)atoi(new_cfg_val);
	}
    else if(strcmp(cfg_var, "HIGH_TH") == 0) 
	{
        if(cfg_idx >= 0 && cfg_idx < 24) 
		{
            config.high_th[cfg_idx] = (uint16_t)atoi(new_cfg_val);
        }
		else
		{
			SIM_Send_TCP("R:ERR");
			return;
		}
    }
    else if(strcmp(cfg_var, "LOW_TH") == 0) 
	{
        if(cfg_idx >= 0 && cfg_idx < 24) 
		{
            config.low_th[cfg_idx] = (uint16_t)atoi(new_cfg_val);
        }
		else
		{
			SIM_Send_TCP("R:ERR");
			return;
		}
    }
    else if(strcmp(cfg_var, "TCP_IP") == 0)
	{
        strncpy(config.tcp_IPaddress, new_cfg_val, sizeof(config.tcp_IPaddress) - 1);
        config.tcp_IPaddress[sizeof(config.tcp_IPaddress) - 1] = '\0';
		strcpy(sys.TCP.IP_address, config.tcp_IPaddress);
		flags.TCP_Parameter_Changed = 1;
    }
    else if(strcmp(cfg_var, "TCP_PORT") == 0)
	{
        strncpy(config.tcp_Port, new_cfg_val, sizeof(config.tcp_Port) - 1);
        config.tcp_Port[sizeof(config.tcp_Port) - 1] = '\0';
		strcpy(sys.TCP.Port, config.tcp_Port);
		flags.TCP_Parameter_Changed = 1;
    }
	else
	{
		SIM_Send_TCP("R:VAR_ERR");
		return;
	}

	if (f_open(&config_file, CONFIG_FILE, FA_WRITE | FA_CREATE_ALWAYS) == FR_OK)
	{
		f_write(&config_file, &config, sizeof(config), &bytes_written);
		f_close(&config_file);
	}
	else
	{
		SIM_Send_TCP("R:SAV_ERR");
		return;
	}
	
	memset(cfg_var, 0, sizeof(cfg_var));
	cfg_idx = 0;
	memset(new_cfg_val, 0, sizeof(new_cfg_val));	
	SIM_Send_TCP("R:OK");
}

/*-----RECUPERO E INVIO VALORE DI CONFIGURAZIONE-----*/
void Send_Config(void)
{
	char value_str[128] = {0};

	if(strcmp(cfg_var, "DEVICE_ID") == 0)
	{
		sprintf(value_str, "R:%u", config.device_id);
	}
	else if(strcmp(cfg_var, "SAMP_FREQ") == 0)
	{
		sprintf(value_str, "R:%u", config.samp_freq);
	}
	else if(strcmp(cfg_var, "BUFFER_SECS") == 0)
	{
		sprintf(value_str, "R:%u", config.buffering_secs);
	}
	else if(strcmp(cfg_var, "CONN_TIMEOUT") == 0)
	{
		sprintf(value_str, "R:%lu", config.connection_timeout_ms);
	}
	else if(strcmp(cfg_var, "LOG_PERIOD") == 0)
	{
		sprintf(value_str, "R:%lu", config.log_period_ms);
	}
	else if(strcmp(cfg_var, "HAMMER_TH") == 0)
	{
		sprintf(value_str, "R:%u", config.hammer_th);
	}
	else if(strcmp(cfg_var, "HIGH_TH") == 0 && cfg_idx >= 0 && cfg_idx < 24)
	{
		sprintf(value_str, "R:%u", config.high_th[cfg_idx]);
	}
	else if(strcmp(cfg_var, "LOW_TH") == 0 && cfg_idx >= 0 && cfg_idx < 24)
	{
		sprintf(value_str, "R:%u", config.low_th[cfg_idx]);
	}
	else if(strcmp(cfg_var, "TCP_IP") == 0)
	{
		sprintf(value_str, "R:%s", config.tcp_IPaddress);
	}
	else if(strcmp(cfg_var, "TCP_PORT") == 0)
	{
		sprintf(value_str, "R:%s", config.tcp_Port);
	}
	else
	{
		strncpy(value_str, "R:ERR", sizeof(value_str)-1);
	}

	memset(cfg_var, 0, sizeof(cfg_var));
	cfg_idx = 0;
	memset(new_cfg_val, 0, sizeof(new_cfg_val));	

	SIM_Send_TCP(value_str);
}

/*-----AZZERAMENTO FLAG-----*/
void Clear_Flags(void)
{
	if(!sys.ACC_Present)
	{
		memset(&flags, 0, sizeof(flags));
		flags.ACC_Complete = 1;
	}
	else
	{
		memset(&flags, 0, sizeof(flags));
	}
}
