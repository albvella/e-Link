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
	MEASURE_INIT_STATE,
	MEASURING_STATE,
	SEND_RECORDING_STATE
} Machine_State_TypeDef;

typedef struct {
	uint8_t ADC_Complete : 1;
	uint8_t ADC_Half_Buffer : 1;
	uint8_t ADC_Full_Buffer : 1;
	uint8_t RAM_Mounted : 1;
	uint8_t FLASH_Mounted : 1;
	uint8_t Hammer_Detected : 1;
	uint8_t Threshold_Detected : 1;
	uint8_t BC_Interrupt : 1;
	uint8_t ACC_Present : 1;
	uint8_t ACC_Complete : 1;
} System_Flags_TypeDef;

typedef struct {
	char server_name[100];
	char port[100];
	char username[100];
	char password[100];
	char clientID[100];
	char topic[100];
} MQTT_TypeDef;

typedef struct {
    uint8_t file_ota_open;
    FIL file_ota;
    uint32_t file_ota_written;

    uint8_t file_meas_1_open;
    FIL file_meas_1;
    uint8_t file_meas_2_open;
    FIL file_meas_2;

    uint16_t Low_th;
    uint16_t High_th;

    uint64_t BC_Flags;

    char apn[100];
    MQTT_TypeDef MQTT;
} System_Resources_Typedef;
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
