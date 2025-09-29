/*
 * ota.h
 *
 *  Created on: Sep 26, 2025
 *      Author: albve
 */

#ifndef INC_OTA_H_
#define INC_OTA_H_

#include "main.h"

int OTA_Init(void);
int OTA_Receive(void);
int OTA_CRC_Check(void);
int OTA_Apply(void);
uint32_t OTA_CRC(uint8_t *buf, uint32_t len, uint32_t prev_crc);

#endif /* INC_OTA_H_ */
