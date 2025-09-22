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

#define APP_CONFIG_FILE "/flash/config.bin"

#define APP_OTA_FILE (1)
#define APP_OTA_FILE_NAME "/ram/ota.bin"
#define APP_OTA_FILE_SIZE (0x1F400) // 128 kBytes

#define APP_MEASURE_FILE (2)
#define MEASURE_FILE_NAME_1 "/ram/meas1.bin"
#define MEASURE_FILE_NAME_2 "/ram/meas2.bin"

#define SIM_RXBUFFER_SIZE          1024
#define ACC_FIFO_WATERMARK         200
#define PRESS_HALF_SAMPLES         ACC_FIFO_WATERMARK
#define PRESS_FULL_SAMPLES         PRESS_HALF_SAMPLES * 2
#define MAX_VOLUME_LEN             40
#define MAX_VOLUME_SAMPLES         MAX_VOLUME_LEN / 2
#define ACCELERATION_LEN           ACC_FIFO_WATERMARK * 7
#define SUPPLY_LEN                 12
#define TEMP_LEN                   2
#define PRESS_HALF_LEN             PRESS_FULL_SAMPLES

#define SAVING_BUFFER_LEN         PRESS_HALF_LEN + MAX_VOLUME_LEN + ACCELERATION_LEN

#define SAMPLE_SIZE SAVING_BUFFER_LEN

#define MAX_COMPRESSED_SIZE 1200     // Worst case: poca compressione
#define METADATA_SIZE 6              // timestamp + compressed_size
#define MAX_SAMPLE_TOTAL_SIZE (METADATA_SIZE + MAX_COMPRESSED_SIZE)

#define SIM_PROMPT_TIMEOUT_MS 3000

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
extern uint16_t Volume_Period[MAX_VOLUME_LEN/2];
extern uint8_t Acceleration[ACC_FIFO_WATERMARK*7];
extern uint16_t Last_Pressure;
extern uint16_t Last_Volume;
extern Acceleration_Data_TypeDef Last_Acceleration;
extern uint16_t Temperature;

extern char MQTT_Logging[100];
extern uint8_t Saving_Buffer[SAVING_BUFFER_LEN];
extern int Address_Offset;

extern char LTE_Ack_buffer[100];

extern uint16_t Cycles_After_Warning;

extern uint32_t Saved_Bytes;
extern uint16_t Saved_Samples;

extern FRESULT res;

extern uint16_t Hammer_Th;
extern uint16_t High_TH[24];
extern uint16_t Low_TH[24];

extern stmdev_ctx_t acc;
extern lsm6dsv16x_fifo_status_t fifo_status;
extern uint16_t num;

extern uint8_t sim_rx_buffer[SIM_RXBUFFER_SIZE];
extern uint16_t sim_write_ptr;
extern uint16_t sim_read_ptr;

extern char cfg_var[20];
extern int cfg_idx;
extern char new_cfg_val[10];

extern uint16_t step_size_table_16bit[88];
extern uint16_t step_size_table_12bit[88];
extern int8_t index_adjustment_table[8];


#endif /* INC_GLOBAL_VARIABLES_H_ */
