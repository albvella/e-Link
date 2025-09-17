/*
 * process.h
 *
 *  Created on: Sep 20, 2024
 *      Author: albve
 */

#ifndef INC_PROCESS_H_
#define INC_PROCESS_H_

#include "main.h"

void Save_Data(void);
void Warning_Detection(uint16_t* Data);
void RAM_Save_Measure(uint8_t* Buffer);
void Send_Measure(void);
void Apply_Config(void);

#endif /* INC_PROCESS_H_ */
