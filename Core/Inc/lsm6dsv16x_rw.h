/*
 * lsm6dsv16x_rw.h
 *
 *  Created on: Feb 28, 2025
 *      Author: albve
 */

#ifndef INC_LSM6DSV16X_RW_H_
#define INC_LSM6DSV16X_RW_H_

#include "main.h"

int32_t acc_write(void *handle, uint8_t reg, const uint8_t *bufp, uint16_t len);
int32_t acc_read(void *handle, uint8_t reg, uint8_t *bufp, uint16_t len);


#endif /* INC_LSM6DSV16X_RW_H_ */
