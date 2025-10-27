/*
 * RTC.h
 *
 *  Created on: Sep 17, 2025
 *      Author: albve
 */

#ifndef INC_RTC_H_
#define INC_RTC_H_

#include "main.h"
#include"global_variables.h"
#include"SIM7000.h"
#include "peripherals.h"
#include <string.h>
#include <stdlib.h>

void RTC_Init(void);
int Get_DateTime_From_Network(void);
void Set_Default_DateTime(void);
uint8_t Calculate_Weekday(uint16_t year, uint8_t month, uint8_t day);
int8_t Calculate_Italy_Timezone(uint16_t year, uint8_t month, uint8_t day);
uint8_t Calculate_Last_Sunday(uint16_t year, uint8_t month);
void Apply_Timezone_Correction(RTC_DateTypeDef* sDate, RTC_TimeTypeDef* sTime, int16_t correction_minutes);
void Adjust_Date(RTC_DateTypeDef* sDate, int16_t day_correction);



#endif /* INC_RTC_H_ */
