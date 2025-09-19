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
	Last_Volume = (uint16_t)(Last_Volume / current_period_cnt);
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

	uint8_t compressed_data[MAX_COMPRESSED_SIZE];
    uint32_t compressed_size = Compress_Sample(Saving_Buffer, SAVING_BUFFER_LEN, compressed_data);

	Compressed_Sample_Typedef sample;
    sample.timestamp = HAL_GetTick();
    sample.compressed_size = compressed_size;

	RAM_Save_Measure(&sample, compressed_data);

	Address_Offset = 0;

	if(flags.Hammer_Detected || flags.Threshold_Detected)
	{
		Cycles_After_Warning++;
		if(Cycles_After_Warning >= config.buffering_secs * (config.samp_freq / ACC_FIFO_WATERMARK))
		{
			state = SEND_RECORDING_STATE;
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

/*-----AVVIO MISURA-----*/
void Start_Measure(void)
{
	sys.RAM_Samples_Number = (config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * 2;
	sys.RAM_Buffer_Len = 0;
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

	HAL_TIM_PWM_Start(ACC_TIMER, TIM_CHANNEL_3);
	HAL_ADC_Start_DMA(PRESSURE_ADC, (uint32_t*)&Pressure, PRESS_FULL_SAMPLES);
	HAL_TIM_OC_Start_IT(ADC_TIMER, TIM_CHANNEL_3);
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
    uint32_t total_size = METADATA_SIZE + sample->compressed_size;
    uint32_t address = Saved_Bytes;

	if(Saved_Samples >= sys.RAM_Samples_Number) 
	{
		sys.RAM_Buffer_Len = Saved_Bytes;
		Saved_Bytes = 0;
		Saved_Samples = 0;
		address = 0;
    }

	RAM_Write(address, METADATA_SIZE, (uint8_t*)sample);
    address += METADATA_SIZE;

	RAM_Write(address, sample->compressed_size, compressed_data);
    
    Saved_Bytes += total_size;
	Saved_Samples++;
}

/*-----INVIO MISURA COMPLETA-----*/
void Send_Measure(void)
{
    uint8_t tcp_chunk[1460];
    uint32_t chunk_fill = 0;
    uint32_t address = Saved_Bytes;
    uint32_t total_processed = 0;

	HAL_UART_DMAStop(LTE_UART);

    while (total_processed < sys.RAM_Buffer_Len) 
	{
        Compressed_Sample_Typedef sample_header;
        RAM_Read(address, METADATA_SIZE, (uint8_t*)&sample_header);
        address += METADATA_SIZE;

        uint32_t sample_total_size = METADATA_SIZE + sample_header.compressed_size;
        uint32_t sample_bytes_left = sample_total_size;
        uint32_t sample_addr = address;

        while (sample_bytes_left > 0) 
		{
            uint32_t chunk_space = sizeof(tcp_chunk) - chunk_fill;
            uint32_t bytes_to_copy = (sample_bytes_left < chunk_space) ? sample_bytes_left : chunk_space;

            RAM_Read(sample_addr, bytes_to_copy, tcp_chunk + chunk_fill);

            chunk_fill += bytes_to_copy;
            sample_addr += bytes_to_copy;
            sample_bytes_left -= bytes_to_copy;

            if (chunk_fill == sizeof(tcp_chunk)) 
			{
                SIM_Send_TCP_Chunk(tcp_chunk, sizeof(tcp_chunk));
                chunk_fill = 0;
            }
        }

        address += sample_header.compressed_size;
        total_processed += sample_total_size;

        if (address >= sys.RAM_Buffer_Len) 
		{
            address = 0;
        }
    }

    // Invia ultimo chunk parziale
    if (chunk_fill > 0) 
	{
        SIM_Send_TCP_Chunk(tcp_chunk, chunk_fill);
    }
}

/*-----COMPRESSIONE DATI-----*/
uint16_t Compress_Sample(uint8_t *input, uint16_t input_len, uint8_t *output)
{
    uint16_t out_idx = 0;

    // 1. Pressione: delta + RLE
    uint16_t *adc = (uint16_t*)input;
    for (int i = 0; i < PRESS_HALF_SAMPLES;) {
        int run = 1;
        while (i + run < PRESS_HALF_SAMPLES && adc[i] == adc[i + run]) run++;
        if (run > 2) {
            output[out_idx++] = 0x80; // RLE flag
            output[out_idx++] = run;
            output[out_idx++] = adc[i] & 0xFF;
            output[out_idx++] = adc[i] >> 8;
            i += run;
        } else {
            int16_t delta = adc[i] - (i > 0 ? adc[i-1] : 0);
            output[out_idx++] = 0x00; // delta flag
            output[out_idx++] = delta & 0xFF;
            output[out_idx++] = delta >> 8;
            i++;
        }
    }

    // 2. Flusso: RLE
    uint16_t *counter = (uint16_t*)(input + PRESS_HALF_LEN);
    for (int i = 0; i < MAX_VOLUME_SAMPLES;) {
        int run = 1;
        while (i + run < MAX_VOLUME_SAMPLES && counter[i] == counter[i + run]) run++;
        if (run > 2) {
            output[out_idx++] = 0x81; // RLE flag
            output[out_idx++] = run;
            output[out_idx++] = counter[i] & 0xFF;
            output[out_idx++] = counter[i] >> 8;
            i += run;
        } else {
            output[out_idx++] = 0x01; // value flag
            output[out_idx++] = counter[i] & 0xFF;
            output[out_idx++] = counter[i] >> 8;
            i++;
        }
    }

    // 3. Accelerometro: header + delta/RLE per assi
    uint8_t *accel = input + PRESS_HALF_LEN + MAX_VOLUME_LEN;
    for (int i = 0; i < ACC_FIFO_WATERMARK; i++) {
        uint8_t header = accel[i*7];
        uint16_t x = accel[i*7+1] | (accel[i*7+2] << 8);
        uint16_t y = accel[i*7+3] | (accel[i*7+4] << 8);
        uint16_t z = accel[i*7+5] | (accel[i*7+6] << 8);

        // Delta coding per X/Y/Z
        int16_t dx = x - (i > 0 ? (accel[(i-1)*7+1] | (accel[(i-1)*7+2] << 8)) : 0);
        int16_t dy = y - (i > 0 ? (accel[(i-1)*7+3] | (accel[(i-1)*7+4] << 8)) : 0);
        int16_t dz = z - (i > 0 ? (accel[(i-1)*7+5] | (accel[(i-1)*7+6] << 8)) : 0);

        output[out_idx++] = header;
        output[out_idx++] = dx & 0xFF;
        output[out_idx++] = dx >> 8;
        output[out_idx++] = dy & 0xFF;
        output[out_idx++] = dy >> 8;
        output[out_idx++] = dz & 0xFF;
        output[out_idx++] = dz >> 8;
    }

    return out_idx;
}

/*-----APPLICA VALORI CONFIGURAZIONE-----*/
void Apply_Config(void)
{
	FIL config_file;
	UINT bytes_read;
	
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
			config.samp_freq = (uint16_t)atoi(new_cfg_val);
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
			config.buffering_secs = (uint8_t)atoi(new_cfg_val);
		}
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

	if(((config.samp_freq / ACC_FIFO_WATERMARK) * config.buffering_secs * SAVING_BUFFER_LEN) * 2 > psram_get_size()) 
	{
		if(config.samp_freq > 1600)
		{
			config.samp_freq = 1600;
		}
		else if(config.buffering_secs > 30)
		{
			config.buffering_secs = 30;
		}
	}

	if (f_open(&config_file, APP_CONFIG_FILE, FA_WRITE | FA_CREATE_ALWAYS) != FR_OK) 
	{
		return;
	}

	if (f_open(&config_file, APP_CONFIG_FILE, FA_READ) == FR_OK) 
	{
		if (f_read(&config_file, &config, sizeof(config), &bytes_read) == FR_OK && bytes_read == sizeof(config))
		{
			f_close(&config_file);
			return;
		}
		f_close(&config_file);
	}
	memset(cfg_var, 0, sizeof(cfg_var));
	cfg_idx = 0;
	memset(new_cfg_val, 0, sizeof(new_cfg_val));	
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
