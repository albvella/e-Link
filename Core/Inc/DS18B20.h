/*
 * DS18B20.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_DS18B20_H_
#define INC_DS18B20_H_

#include "main.h"

void Temp_Sensor_Init(void);
void Temp_Sensor_Write(uint8_t data);
uint8_t Temp_Sensor_ReadByte(void);
uint8_t Temp_Sensor_ReadBit(void);
void Temp_Start_Conversion(void);
uint16_t Temperature_Init(void);
uint16_t Read_Temperature(void);

#endif /* INC_DS18B20_H_ */
