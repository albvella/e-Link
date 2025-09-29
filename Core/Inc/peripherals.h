/*
 * peripherals.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_PERIPHERALS_H_
#define INC_PERIPHERALS_H_

#include "main.h"

extern ADC_HandleTypeDef hadc1;
extern DMA_HandleTypeDef hdma_adc1;
extern CRC_HandleTypeDef hcrc;
extern CRC_HandleTypeDef hcrc;
extern I2C_HandleTypeDef hi2c3;
extern QSPI_HandleTypeDef hqspi;
extern RTC_HandleTypeDef hrtc;
extern SPI_HandleTypeDef hspi2;
extern SPI_HandleTypeDef hspi3;
extern TIM_HandleTypeDef htim1;
extern TIM_HandleTypeDef htim2;
extern TIM_HandleTypeDef htim3;
extern TIM_HandleTypeDef htim4;
extern UART_HandleTypeDef huart4;
extern UART_HandleTypeDef huart1;

#define LED_TIMER      (&htim1)
#define GRN_LED        (TIM_CHANNEL_3)
#define RED_LED        (TIM_CHANNEL_2)
#define ORG_LED        (TIM_CHANNEL_1)
#define TEMP_UART      (&huart4)
#define SIM_UART       (&huart1)
#define I2C            (&hi2c3)
#define EXTFLASH_SPI   (&hspi2)
#define PSRAM_SPI      (&hqspi)
#define ACC_SPI        (&hspi3)
#define ACC_TIMER      (&htim3)
#define PRESSURE_ADC   (&hadc1)
#define ADC_TIMER      (&htim4)
#define VOLUME_TIMER   (&htim2)
#define ACC_INTERRUPT  (GPIO_PIN_2)
#define BC_INTERRUPT   (GPIO_PIN_4)
#define RI_INTERRUPT   (GPIO_PIN_8)
#define BTN_INTERRUPT  (GPIO_PIN_13)
#define HCRC           (&hcrc)



#endif /* INC_PERIPHERALS_H_ */
