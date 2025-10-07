/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32l4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "FatFs/ff.h"
/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */
typedef enum {
    IDLE,
	MEASURE_INIT_STATE,
	MEASURING_STATE,
	OTA_STATE
} Machine_State_TypeDef;

typedef struct {
    int16_t previous_value; // Ultimo valore predetto/ricostruito
    int8_t  step_index;     // Indice nella tabella degli step di quantizzazione
} AdpcmState_Typedef;

typedef struct{
    uint8_t header;
    uint16_t x;
    uint16_t y;
    uint16_t z;
} Acceleration_Data_TypeDef;

typedef struct {
	uint8_t Data_Request : 1;
	uint8_t Measure_Request : 1;
	uint8_t Start_OTA : 1;
	uint8_t Ping : 1;
	uint8_t Set_Config : 1;
    uint8_t Get_Config : 1;
	uint8_t Start_Meas : 1;
	uint8_t Idle : 1;
} CMD_Typedef;

typedef struct {
	uint8_t ADC_Complete : 1;
	uint8_t ADC_Half_Buffer : 1;
	uint8_t ADC_Full_Buffer : 1;
	uint8_t Hammer_Detected : 1;
	uint8_t Threshold_Detected : 1;
	uint8_t BC_Interrupt : 1;
	uint8_t ACC_Complete : 1;
	uint8_t Message_Rx : 1;
    uint8_t MQTT_ReadytoSend : 1;
    uint8_t TCP_ReadytoSend : 1;
    uint8_t TCP_isSending : 1;
    uint8_t SIM_isConnected : 1;
    CMD_Typedef CMD;
} System_Flags_TypeDef;

typedef struct {
	char server_name[100];
	char port[100];
	char username[100];
	char password[100];
	char clientID[100];
	char Data_Topic[100];
	char Command_Topic[100];
	char OTA_Topic[100];
    char Info_Topic[100];
} MQTT_TypeDef;

typedef struct {
    char IP_address[100];
    char Port[100];
} TCP_Typedef;

typedef struct {
    uint8_t OTA_File_isOpen : 1;
    FIL OTA_File;
    uint8_t ACC_Present : 1;
    uint8_t RAM_Mounted : 1;
	uint8_t FLASH_Mounted : 1;
    uint16_t Low_th;
    uint16_t High_th;
    uint64_t BC_Flags;
    RTC_DateTypeDef onDate;
	RTC_TimeTypeDef onTime;
    char apn[100];
    uint32_t RAM_Samples_Number;
    uint8_t Active_RAM_Buffer;
    uint32_t Current_RAM_Base;
    uint32_t Current_RAM_Len;
    uint32_t RAM_Buffer_Base_tosend;
    uint32_t Inactive_RAM_Len;
    uint32_t SIM_Prompt_Status;
    uint32_t SIM_Connection_Status;
    TCP_Typedef TCP;
} System_Resources_Typedef;

typedef struct {
    uint8_t device_id;
    uint16_t samp_freq;
    uint8_t buffering_secs;
    uint32_t connection_timeout;
    uint16_t hammer_th;                    
    uint16_t low_th[24];                   
    uint16_t high_th[24];                  
    char tcp_IPaddress[64];   
    char tcp_Port[64];   
} Config_Typedef;  

typedef struct{
    uint16_t pressure_size;
    uint16_t volume_size;
    uint16_t acceleration_size;
} Compressed_Sizes_Typedef;

typedef struct {       
    Compressed_Sizes_Typedef compressed_size;    
    uint8_t data[];              
} __attribute__((packed)) Compressed_Sample_Typedef;
/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define USR_BTN_Pin GPIO_PIN_13
#define USR_BTN_GPIO_Port GPIOC
#define DBG_Pin GPIO_PIN_3
#define DBG_GPIO_Port GPIOC
#define LTE_STATUS_Pin GPIO_PIN_3
#define LTE_STATUS_GPIO_Port GPIOA
#define FLASH_nCS_Pin GPIO_PIN_12
#define FLASH_nCS_GPIO_Port GPIOB
#define FLASH_nWP_Pin GPIO_PIN_6
#define FLASH_nWP_GPIO_Port GPIOC
#define FLASH_nRESET_Pin GPIO_PIN_7
#define FLASH_nRESET_GPIO_Port GPIOC
#define LTE_POWER_ON_Pin GPIO_PIN_11
#define LTE_POWER_ON_GPIO_Port GPIOA
#define LTE_RESET_Pin GPIO_PIN_12
#define LTE_RESET_GPIO_Port GPIOA
#define ACC_nCS_Pin GPIO_PIN_15
#define ACC_nCS_GPIO_Port GPIOA
#define DCD_Pin GPIO_PIN_5
#define DCD_GPIO_Port GPIOB
#define DTR_Pin GPIO_PIN_9
#define DTR_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
