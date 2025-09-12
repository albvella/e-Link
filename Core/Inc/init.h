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
void RTC_Init(void);
void Acc_Init(stmdev_ctx_t* acc);

#endif /* INC_INIT_H_ */
