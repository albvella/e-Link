/*
 * global_variables.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_GLOBAL_VARIABLES_H_
#define INC_GLOBAL_VARIABLES_H_

#include "main.h"
#include "INA3221.h"
#include "INA3221_reg.h"
#include "FatFs/ff.h"
#include "lsm6dsv16x_reg.h"


#define FW_VERSION 0x0100

#define CONFIG_FILE "/flash/config.bin"

#define OTA_FILE (1)
#define OTA_FILE_NAME "/ram/ota.bin"
#define OTA_FILE_SIZE (0x1F400) // 128 kBytes

#define SIM_RXBUFFER_SIZE          2000
#define ACC_FIFO_WATERMARK         200
#define PRESS_HALF_SAMPLES         ACC_FIFO_WATERMARK
#define PRESS_FULL_SAMPLES         PRESS_HALF_SAMPLES * 2
#define MAX_VOLUME_SAMPLES         10
#define MAX_VOLUME_LEN             MAX_VOLUME_SAMPLES * 4
#define ACCELERATION_LEN           ACC_FIFO_WATERMARK * 7
#define SUPPLY_LEN                 12
#define TEMP_LEN                   2
#define PRESS_HALF_LEN             PRESS_FULL_SAMPLES

#define SAVING_BUFFER_LEN          PRESS_HALF_LEN + MAX_VOLUME_LEN + ACCELERATION_LEN

#define SAMPLE_SIZE                SAVING_BUFFER_LEN

#define MAX_COMPRESSED_SIZE        1200
#define METADATA_SIZE              6

#define SAVING_SAMPLE_SIZE         540

#define RAM_FIRST_BUFFER_ADD       0
#define RAM_SECOND_BUFFER_ADD      0x400000

#define SIM_PROMPT_TIMEOUT_MS      10000
#define SIM_CONNECTION_TIMEOUT_MS  60000

#define PROMPT                     0x203E0A0D            // "\r\n> "
#define SENDOK_H                   0x45530A0D            // "/r/nSE "
#define SENDOK_L                   0x4F20444E            // "ND O"
#define ERROR                      0x4F525245            // "ERRO"
#define COMMAND                    0x444D432B            // "+CMD"


extern Machine_State_TypeDef state;
extern System_Resources_Typedef sys;
extern System_Flags_TypeDef flags;
extern Config_Typedef config;

extern FATFS psram_fs;
extern FATFS flash_fs;

extern uint32_t T_current;
extern uint32_t T_prev;
extern uint32_t V_Period;

extern supply_bus_t Supply;
extern uint8_t Period_cnt;

extern uint16_t Pressure[PRESS_FULL_SAMPLES];
extern uint32_t Volume_Period[MAX_VOLUME_SAMPLES];
extern uint8_t Acceleration[ACC_FIFO_WATERMARK*7];
extern uint16_t Last_Pressure;
extern uint32_t Last_Volume;
extern Acceleration_Data_TypeDef Last_Acceleration;
extern uint16_t Temperature;
extern uint16_t Vbatt;

extern char Data_Logging[100];
extern uint8_t Saving_Buffer[SAVING_BUFFER_LEN];
extern int Address_Offset;

extern char LTE_Ack_buffer[100];

extern uint16_t Cycles_After_Warning;

extern uint32_t Saved_Bytes;
extern uint16_t Saved_Samples;
extern uint32_t Send_Measure_Addr;
extern uint8_t tcp_chunk[1460];
extern uint32_t Measure_Bytes_Sent;

extern FRESULT res;

extern uint16_t Hammer_Th;
extern uint16_t High_TH_Array[24];
extern uint16_t Low_TH_Array[24];

extern stmdev_ctx_t acc;
extern lsm6dsv16x_fifo_status_t fifo_status;
extern uint16_t num;

extern uint8_t sim_rx_buffer[SIM_RXBUFFER_SIZE];
extern uint16_t sim_write_ptr;
extern uint16_t sim_read_ptr;

extern char cfg_var[20];
extern int cfg_idx;
extern char new_cfg_val[10];

extern uint8_t compressed_data[MAX_COMPRESSED_SIZE];

extern const uint16_t step_size_table_16bit[88];
extern const uint16_t step_size_table_12bit[88];
extern const int8_t index_adjustment_table_press[8];
extern const int8_t index_adjustment_table_acc[8];

extern const unsigned char base64_table[256];
extern const char base64_enc_table[64];


#endif /* INC_GLOBAL_VARIABLES_H_ */
