/*
 * process.c
 *
 *  Created on: Sep 20, 2024
 *      Author: albve
 */

#include "process.h"
#include "main.h"
#include "global_variables.h"
#include "LTE.h"
#include "INA3221.h"
#include "DS18B20.h"
#include "stdio.h"
#include "string.h"


/*-----ACQUISIZIONE MISURE E LOG DEI DATI-----*/
void Data_Logging(void)
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

	sprintf(MQTT_Logging, "%u,%u,%u,%u,%u,%u,%u,%u,%u,%u", Last_Pressure, Last_Volume, Last_Acceleration, Supply.i1, Supply.i2, Supply.i3, Supply.v1, Supply.v2, Supply.v3, Temperature);
	LTE_publish_MQTT_Message(sys.MQTT.topic, MQTT_Logging);
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

	if(max - min >= HAMMER_THRESHOLD)
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
