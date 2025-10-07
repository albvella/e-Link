/*
 * init.h
 *
 *  Created on: Sep 17, 2024
 *      Author: albve
 */

#ifndef INC_INIT_H_
#define INC_INIT_H_

#include "main.h"
#include "lsm6dsv16x_reg.h"

void System_Init(void);
void FatFS_Init(void);
int Acc_Init(stmdev_ctx_t* acc, uint16_t fs);
void RTC_Init(void);
int Get_DateTime_From_Network(void);
void Set_Default_DateTime(void);
uint8_t Calculate_Weekday(uint16_t year, uint8_t month, uint8_t day);
void Config_Init(void);

#endif /* INC_INIT_H_ */
