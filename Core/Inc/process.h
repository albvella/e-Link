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
void Start_Measure(void);
void Stop_Measure(void);
void Warning_Detection(uint16_t* Data);
void RAM_Save_Measure(Compressed_Sample_Typedef* sample, uint8_t* compressed_data);
void Send_Measure(void);
void Apply_Config(void);
uint16_t Compress_Sample(uint8_t* input, uint16_t input_len, uint8_t* output);
void Clear_Flags(void);

#endif /* INC_PROCESS_H_ */
