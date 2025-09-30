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

	memcpy(Saving_Buffer + Address_Offset, Volume_Period, MAX_VOLUME_LEN);
	uint8_t current_period_cnt = Period_cnt;
	Last_Volume = 0;
	for(int i = 0; i < current_period_cnt; i++)
	{
		Last_Volume += Volume_Period[i];
	}
	Last_Volume = (uint32_t)(Last_Volume / current_period_cnt);
	memset(Volume_Period, 0, sizeof(Volume_Period));
	Period_cnt = 0;
	Address_Offset += MAX_VOLUME_LEN;

	if(sys.ACC_Present)
	{
		memcpy(Saving_Buffer + Address_Offset, Acceleration, ACCELERATION_LEN);
		Last_Acceleration.x = 0;
		Last_Acceleration.y = 0;
		Last_Acceleration.z = 0;
		for(int i = 0; i < ACCELERATION_LEN; i += 7)
		{
			Last_Acceleration.x += Acceleration[i+1] | (Acceleration[i+2] << 8); 
			Last_Acceleration.y += Acceleration[i+3] | (Acceleration[i+4] << 8); 
			Last_Acceleration.z += Acceleration[i+5] | (Acceleration[i+6] << 8); 
		}
		Last_Acceleration.x = (uint16_t)(Last_Acceleration.x / (ACCELERATION_LEN / 7));
		Last_Acceleration.y = (uint16_t)(Last_Acceleration.y / (ACCELERATION_LEN / 7));
		Last_Acceleration.z = (uint16_t)(Last_Acceleration.z / (ACCELERATION_LEN / 7));
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

	uint8_t compressed_data[MAX_COMPRESSED_SIZE];
	Compressed_Sample_Typedef sample;
    sample.compressed_size = Compress_Sample(Saving_Buffer, SAVING_BUFFER_LEN, compressed_data);

	__disable_irq();
	RAM_Save_Measure(&sample, compressed_data);
	__enable_irq();

	Address_Offset = 0;

	if(flags.Hammer_Detected || flags.Threshold_Detected)
	{
		Cycles_After_Warning++;
		if(Cycles_After_Warning >= config.buffering_secs * (config.samp_freq / ACC_FIFO_WATERMARK))
		{
			if(!flags.CMD.Measure_Request)
			{
				LED_Start(RED_LED, FAST, LOW);
				Switch_Buffer();
				flags.CMD.Measure_Request = 1;
				Send_Measure_Addr = Saved_Bytes;
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

/*-----CAMBIO BUFFER-----*/
void Switch_Buffer(void)
{
    sys.Inactive_RAM_Len = sys.Current_RAM_Len;

    if (sys.Active_RAM_Buffer == 0) 
	{
		sys.RAM_Buffer_Base_tosend = RAM_SECOND_BUFFER_ADD;
        sys.Active_RAM_Buffer = 1;
        sys.Current_RAM_Base = RAM_SECOND_BUFFER_ADD;
    } 
	else 
	{
		sys.RAM_Buffer_Base_tosend = RAM_FIRST_BUFFER_ADD;
        sys.Active_RAM_Buffer = 0;
        sys.Current_RAM_Base = RAM_FIRST_BUFFER_ADD;
    }

    sys.Current_RAM_Len = 0;
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
	sys.Inactive_RAM_Len = 0;
	sys.Current_RAM_Base = RAM_FIRST_BUFFER_ADD;
	sys.Current_RAM_Len = 0;
	flags.SIM_isConnected = 1;
	memset(Pressure, 0, sizeof(Pressure));
	memset(Volume_Period, 0, sizeof(Volume_Period));
	memset(Acceleration, 0, sizeof(Acceleration));
	memset(&Supply, 0, sizeof(Supply));
	Temperature = 0;
	Saved_Bytes = 0;
	Saved_Samples = 0;
	Address_Offset = 0;
	Cycles_After_Warning = 0;
	Clear_Flags();

	ADC_TIMER->Instance->PSC = 100 - 1;
	ADC_TIMER->Instance->ARR = (uint32_t)(SystemCoreClock / (ADC_TIMER->Instance->PSC * config.samp_freq)) - 1;
	ACC_TIMER->Instance->ARR = (uint32_t)(config.samp_freq / 25) - 1;
	ACC_TIMER->Instance->CCR3 = (uint32_t)((ACC_TIMER->Instance->ARR + 1) / 2);

	HAL_TIM_IC_Start_IT(VOLUME_TIMER, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(ACC_TIMER, TIM_CHANNEL_3);
	HAL_ADC_Start_DMA(PRESSURE_ADC, (uint32_t*)&Pressure, PRESS_FULL_SAMPLES);
	HAL_TIM_OC_Start_IT(ADC_TIMER, TIM_CHANNEL_3);
}

/*-----FINE MISURA-----*/
void Stop_Measure(void)
{
	HAL_ADC_Stop_DMA(PRESSURE_ADC);
	HAL_TIM_OC_Stop_IT(ADC_TIMER, TIM_CHANNEL_3);
	HAL_TIM_PWM_Stop(ACC_TIMER, TIM_CHANNEL_3);
	HAL_TIM_IC_Stop_IT(VOLUME_TIMER, TIM_CHANNEL_1);
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

	if(max - min >= Hammer_Th)
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
    uint32_t address = sys.Current_RAM_Base + sys.Current_RAM_Len;

	if(Saved_Samples >= sys.RAM_Samples_Number) 
	{
		sys.Current_RAM_Len = Saved_Bytes;
		Saved_Bytes = 0;
		Saved_Samples = 0;
		address = sys.Current_RAM_Base;
    }

	RAM_Write(address, METADATA_SIZE, (uint8_t*)sample);
    address += METADATA_SIZE;

	RAM_Write(address, samples_size, compressed_data);
    
    Saved_Bytes += total_size;
	Saved_Samples++;
}

/*-----INVIO CHUNK MISURA-----*/
uint32_t Send_Measure_Chunk(uint32_t buffer_base, uint32_t buffer_len, uint32_t start_address)
{
    uint32_t raw_fill = 0;
    uint8_t raw_buffer[1024]; // buffer temporaneo per i dati raw
    uint32_t address = start_address;
    uint32_t end_address = start_address;
    uint8_t first_loop = 1;

    if (buffer_len == 0) 
    {
        return 0;
    }

    do {
        if (address >= buffer_base + buffer_len) 
        {
            address = buffer_base;
        }

        if ((buffer_base + buffer_len - address) < METADATA_SIZE && address < buffer_base + buffer_len) 
        {
            break;
        }
        if ((raw_fill + METADATA_SIZE) > sizeof(raw_buffer)) 
        {
            break;
        }

        Compressed_Sample_Typedef sample_header;
        RAM_Read(address, METADATA_SIZE, (uint8_t*)&sample_header);

        uint32_t sample_size = sample_header.compressed_size.pressure_size +
                               sample_header.compressed_size.volume_size +
                               sample_header.compressed_size.acceleration_size;
        uint32_t sample_total_size = METADATA_SIZE + sample_size;

        if ((raw_fill + sample_total_size) > sizeof(raw_buffer)) 
        {
            break;
        }

        RAM_Read(address, METADATA_SIZE, raw_buffer + raw_fill);
        raw_fill += METADATA_SIZE;
        address += METADATA_SIZE;
        if (address >= buffer_base + buffer_len) address = buffer_base;

        RAM_Read(address, sample_size, raw_buffer + raw_fill);
        raw_fill += sample_size;
        address += sample_size;
        if (address >= buffer_base + buffer_len) address = buffer_base;

        if (address == end_address && !first_loop) 
        {
            break;
        }
        first_loop = 0;
    } while (1);

    if (raw_fill > 0) 
    {
        // Codifica in base64
        size_t b64_len = Base64_Encode(raw_buffer, raw_fill, (char*)tcp_chunk, sizeof(tcp_chunk));
        SIM_Send_TCP_Chunk_DMA(tcp_chunk, b64_len);
    }

    if (address == end_address) 
    {
        return 0;
    }
    return address;
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
		uint8_t nibble = ADPCM_Compression(adc[i], &press_state, step_size_table_12bit);
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

	if (PRESS_HALF_SAMPLES % 2 != 0) 
	{
		output[out_idx++] = packed_byte;
		packed_byte = 0;
	}
	sizes.pressure_size = out_idx - pressure_start;

	// --- 2. Flusso (RLE) ---
	uint32_t *counter = (uint32_t*)(input + PRESS_HALF_LEN);
	uint16_t volume_start = out_idx;

	uint32_t prev = counter[0];
	uint16_t run_len = 1;

	for (int i = 1; i < MAX_VOLUME_SAMPLES; i++) {
		if (counter[i] == prev && run_len < 255) {
			run_len++;
		} else {
			// Scrivi valore e run_len (4 byte valore + 1 byte run_len)
			output[out_idx++] = prev & 0xFF;
			output[out_idx++] = (prev >> 8) & 0xFF;
			output[out_idx++] = (prev >> 16) & 0xFF;
			output[out_idx++] = (prev >> 24) & 0xFF;
			output[out_idx++] = run_len;
			prev = counter[i];
			run_len = 1;
		}
	}
	// Scrivi l'ultimo run
	output[out_idx++] = prev & 0xFF;
	output[out_idx++] = (prev >> 8) & 0xFF;
	output[out_idx++] = (prev >> 16) & 0xFF;
	output[out_idx++] = (prev >> 24) & 0xFF;
	output[out_idx++] = run_len;

	sizes.volume_size = out_idx - volume_start;

	// --- 3. Accelerometro (3 canali separati) ---
	uint8_t *accel = input + PRESS_HALF_LEN + MAX_VOLUME_LEN;
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
		uint8_t nibble_x = ADPCM_Compression(x, &acc_x_state, step_size_table_16bit);
		uint8_t nibble_y = ADPCM_Compression(y, &acc_y_state, step_size_table_16bit);
		uint8_t nibble_z = ADPCM_Compression(z, &acc_z_state, step_size_table_16bit);
		output[out_idx++] = nibble_x | (nibble_y << 4);
		output[out_idx++] = nibble_z;
	}
	sizes.acceleration_size = out_idx - accel_start;

	return sizes;
}

/*-----FUNZIONE DI COMPRESSIONE ADPCM-----*/
uint8_t ADPCM_Compression(int16_t sample, AdpcmState_Typedef* state, uint16_t* step_size_table) 
{
    int32_t diff = (int32_t)sample - state->previous_value;
    uint16_t step = step_size_table[state->step_index];
    uint8_t nibble = 0;

    if (diff < 0) 
	{
        nibble = 8; // Bit di segno
        diff = -diff;
    }

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

    // Clamp del valore predetto
    if (state->previous_value > 32767) state->previous_value = 32767;
    if (state->previous_value < -32768) state->previous_value = -32768;

    // Aggiorna l'indice dello step
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
			return;
		}
		else
		{
			if(((config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * SAVING_BUFFER_LEN) * 2 > psram_get_size()) 
			{
				config.samp_freq = (uint16_t)atoi(new_cfg_val);
			}
		}
	}
	else if(strcmp(cfg_var, "BUFFER_SECS") == 0)
	{
		if((uint8_t)atoi(new_cfg_val) < 5 || (uint8_t)atoi(new_cfg_val) > 30)
		{
			return;
		}
		else
		{
			if(((config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * SAVING_BUFFER_LEN) * 2 > psram_get_size()) 
			{
				config.buffering_secs = (uint8_t)atoi(new_cfg_val);
			}
		}
	}
	else if(strcmp(cfg_var, "CONN_TIMEOUT") == 0)
	{
		config.connection_timeout = (uint32_t)atoi(new_cfg_val);
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
    }
    else if(strcmp(cfg_var, "LOW_TH") == 0) 
	{
        if(cfg_idx >= 0 && cfg_idx < 24) 
		{
            config.low_th[cfg_idx] = (uint16_t)atoi(new_cfg_val);
        }
    }
    else if(strcmp(cfg_var, "DATA_TOPIC") == 0) 
	{
        strncpy(config.data_topic, new_cfg_val, sizeof(config.data_topic) - 1);
        config.data_topic[sizeof(config.data_topic) - 1] = '\0';
		strcpy(sys.MQTT.Data_Topic, config.data_topic);
    }
    else if(strcmp(cfg_var, "CMD_TOPIC") == 0) 
	{
        strncpy(config.command_topic, new_cfg_val, sizeof(config.command_topic) - 1);
        config.command_topic[sizeof(config.command_topic) - 1] = '\0';
		strcpy(sys.MQTT.Command_Topic, config.command_topic);
    }
	else if(strcmp(cfg_var, "INFO_TOPIC") == 0)
	{
		strncpy(config.info_topic, new_cfg_val, sizeof(config.info_topic) - 1);
		config.info_topic[sizeof(config.info_topic) - 1] = '\0';
		strcpy(sys.MQTT.Info_Topic, config.info_topic);
	}
	else if(strcmp(cfg_var, "OTA_TOPIC") == 0)
	{
		strncpy(config.ota_topic, new_cfg_val, sizeof(config.ota_topic) - 1);
		config.ota_topic[sizeof(config.ota_topic) - 1] = '\0';
		strcpy(sys.MQTT.OTA_Topic, config.ota_topic);
	}
	else
	{
		return;
	}

	if (f_open(&config_file, CONFIG_FILE, FA_WRITE | FA_CREATE_ALWAYS) == FR_OK)
	{
		f_write(&config_file, &config, sizeof(config), &bytes_written);
		f_close(&config_file);
	}
	else
	{
		return;
	}
	
	memset(cfg_var, 0, sizeof(cfg_var));
	cfg_idx = 0;
	memset(new_cfg_val, 0, sizeof(new_cfg_val));	
}

/*-----RECUPERO E INVIO VALORE DI CONFIGURAZIONE-----*/
void Get_Config(void)
{
	char value_str[128] = {0};
	const char* topic = sys.MQTT.Info_Topic;

	if(strcmp(cfg_var, "DEVICE_ID") == 0)
	{
		sprintf(value_str, "%u", config.device_id);
	}
	else if(strcmp(cfg_var, "SAMP_FREQ") == 0)
	{
		sprintf(value_str, "%u", config.samp_freq);
	}
	else if(strcmp(cfg_var, "BUFFER_SECS") == 0)
	{
		sprintf(value_str, "%u", config.buffering_secs);
	}
	else if(strcmp(cfg_var, "CONN_TIMEOUT") == 0)
	{
		sprintf(value_str, "%lu", config.connection_timeout);
	}
	else if(strcmp(cfg_var, "HAMMER_TH") == 0)
	{
		sprintf(value_str, "%u", config.hammer_th);
	}
	else if(strcmp(cfg_var, "HIGH_TH") == 0 && cfg_idx >= 0 && cfg_idx < 24)
	{
		sprintf(value_str, "%u", config.high_th[cfg_idx]);
	}
	else if(strcmp(cfg_var, "LOW_TH") == 0 && cfg_idx >= 0 && cfg_idx < 24)
	{
		sprintf(value_str, "%u", config.low_th[cfg_idx]);
	}
	else if(strcmp(cfg_var, "DATA_TOPIC") == 0)
	{
		strncpy(value_str, config.data_topic, sizeof(value_str)-1);
	}
	else if(strcmp(cfg_var, "CMD_TOPIC") == 0)
	{
		strncpy(value_str, config.command_topic, sizeof(value_str)-1);
	}
	else if(strcmp(cfg_var, "INFO_TOPIC") == 0)
	{
		strncpy(value_str, config.info_topic, sizeof(value_str)-1);
	}
	else if(strcmp(cfg_var, "OTA_TOPIC") == 0)
	{
		strncpy(value_str, config.ota_topic, sizeof(value_str)-1);
	}
	else
	{
		strncpy(value_str, "UNKNOWN", sizeof(value_str)-1);
	}

	memset(cfg_var, 0, sizeof(cfg_var));
	cfg_idx = 0;
	memset(new_cfg_val, 0, sizeof(new_cfg_val));	

	SIM_publish_MQTT_Message(topic, value_str);
}

/*-----AZZERAMENTO FLAG-----*/
void Clear_Flags(void)
{
	memset(&sys, 0, sizeof(sys));
	if(!sys.ACC_Present)
	{
		sys.ACC_Present = 1;
	}
}
