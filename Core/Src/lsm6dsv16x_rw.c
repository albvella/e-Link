/*
 * lsm6dsv16x_rw.c
 *
 *  Created on: Feb 28, 2025
 *      Author: albve
 */

#include "lsm6dsv16x_rw.h"
#include "main.h"
#include "global_variables.h"
#include "peripherals.h"

/* -------------SCRITTURA ACCELEROMETRO-------------*/
int32_t acc_write(void *handle, uint8_t reg, const uint8_t *bufp, uint16_t len)
{
	HAL_GPIO_WritePin(ACC_nCS_GPIO_Port, ACC_nCS_Pin, GPIO_PIN_RESET);
	HAL_SPI_Transmit(handle, &reg, 1, 1000);
	HAL_SPI_Transmit(handle, (uint8_t*) bufp, len, 1000);
	HAL_GPIO_WritePin(ACC_nCS_GPIO_Port, ACC_nCS_Pin, GPIO_PIN_SET);
	return 0;
}

/* -------------LETTURA ACCELEROMETRO-------------*/
int32_t acc_read(void *handle, uint8_t reg, uint8_t *bufp, uint16_t len)
{
	reg |= 0x80;
	HAL_GPIO_WritePin(ACC_nCS_GPIO_Port, ACC_nCS_Pin, GPIO_PIN_RESET);
	HAL_SPI_Transmit(handle, &reg, 1, 1000);
	HAL_SPI_Receive(handle, bufp, len, 1000);
	HAL_GPIO_WritePin(ACC_nCS_GPIO_Port, ACC_nCS_Pin, GPIO_PIN_SET);
	return 0;
}
