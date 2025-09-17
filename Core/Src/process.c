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
#include "INA3221.h"
#include "DS18B20.h"
#include "stdio.h"
#include "string.h"
#include "FatFs/ff.h"


/*-----ACQUISIZIONE MISURE E LOG DEI DATI-----*/
void Save_Data(void)
{
	if(flags.ADC_Half_Buffer)
	{
		memcpy(Logging_Buffer + Address_Offset, &Pressure[0], PRESS_FULL_SAMPLES);
		Last_Pressure = Pressure[PRESS_HALF_SAMPLES - 1];
		Warning_Detection(&Pressure[0]);
		flags.ADC_Half_Buffer = 0;
	}
	else if(flags.ADC_Full_Buffer)
	{
		memcpy(Logging_Buffer + Address_Offset, &Pressure[PRESS_HALF_SAMPLES], PRESS_FULL_SAMPLES);
		Last_Pressure = Pressure[PRESS_FULL_SAMPLES - 1];
		Warning_Detection(&Pressure[PRESS_HALF_SAMPLES]);
		flags.ADC_Full_Buffer = 0;
	}
	Address_Offset += PRESS_FULL_SAMPLES;

	memcpy(Logging_Buffer + Address_Offset, Volume_Period, MAX_VOLUME_LEN);
	Last_Volume = Volume_Period[Period_cnt];
	Period_cnt = 0;
	memset(Volume_Period, 0, sizeof(Volume_Period));
	Address_Offset += MAX_VOLUME_LEN;

	if(flags.ACC_Present)
	{
		memcpy(Logging_Buffer + Address_Offset, Acceleration, ACCELERATION_LEN);
		Last_Acceleration = Acceleration[ACCELERATION_LEN - 1];
		flags.ACC_Complete = 0;
	}
	Address_Offset += ACCELERATION_LEN;

	INA3221_Read_Measure(&Supply);
	memcpy(Logging_Buffer + Address_Offset, &Supply, SUPPLY_LEN);
	Address_Offset += SUPPLY_LEN;

	Temperature = Read_Temperature();
	memcpy(Logging_Buffer + Address_Offset, &Temperature, TEMP_LEN);

	RAM_Save_Measure(Logging_Buffer);

	flags.ADC_Complete = 0;
	Address_Offset = 0;

	if(flags.Hammer_Detected || flags.Threshold_Detected)
	{
		Seconds_After_Warning++;
		if(Seconds_After_Warning == 30)
		{
			state = SEND_RECORDING_STATE;
			Seconds_After_Warning = 0;
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
void RAM_Save_Measure(uint8_t* Buffer)
{
	UINT written = 0;

	if(Saves_cnt == 0)
	{
		f_close(&sys.file_meas_1);
		sys.file_meas_1_open = 0;
		f_unlink(MEASURE_FILE_NAME_1);
		res = f_open(&sys.file_meas_1, MEASURE_FILE_NAME_1, FA_READ | FA_WRITE | FA_CREATE_ALWAYS);
		sys.file_meas_1_open = 1;
	}

	if(Saves_cnt == 30)
	{
		f_close(&sys.file_meas_2);
		sys.file_meas_2_open = 0;
		f_unlink(MEASURE_FILE_NAME_2);
		res = f_open(&sys.file_meas_2, MEASURE_FILE_NAME_2, FA_READ | FA_WRITE | FA_CREATE_ALWAYS);
		sys.file_meas_2_open = 1;
	}

	if(Saves_cnt < 30)
	{
		res = f_write(&sys.file_meas_1, (uint8_t *)&Buffer, LOGGING_BUFFER_LEN, &written);
		Saves_cnt++;
	}
	else if(Saves_cnt < 60)
	{
		res = f_write(&sys.file_meas_2, (uint8_t *)&Buffer, LOGGING_BUFFER_LEN, &written);
		Saves_cnt++;
	}
	else
	{
		Saves_cnt = 0;
	}
}

/*-----INVIO MISURA COMPLETA-----*/
void Send_Measure(void)
{

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
