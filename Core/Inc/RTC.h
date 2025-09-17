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



#endif /* INC_RTC_H_ */
