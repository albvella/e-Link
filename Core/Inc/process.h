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
void Switch_Buffer(void);
void Erase_RAM_Data(void);
void Start_Measure(void);
void Stop_Measure(void);
void Warning_Detection(uint16_t* Data);
void RAM_Save_Measure(Compressed_Sample_Typedef* sample, uint8_t* compressed_data);
uint32_t Send_Measure_Chunk(uint32_t buffer_base, uint32_t buffer_len, uint32_t start_address);
void Apply_Config(void);
Compressed_Sizes_Typedef Compress_Sample(uint8_t* input, uint16_t input_len, uint8_t* output);
uint8_t ADPCM_Compression(int16_t sample, AdpcmState_Typedef* state, uint16_t* step_size_table);
void Clear_Flags(void);

#endif /* INC_PROCESS_H_ */
