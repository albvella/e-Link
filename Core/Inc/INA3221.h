/*
 * INA3321.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_INA3221_H_
#define INC_INA3221_H_

#include "main.h"

typedef struct
{
	uint16_t	v1;
	uint16_t	v2;
	uint16_t	v3;
	uint16_t	i1;
	uint16_t	i2;
	uint16_t	i3;

}supply_bus_t;



void INA3221_Init();
void INA3221_Read_Measure(supply_bus_t *reading);
int INA3221_read_reg(uint8_t reg, uint16_t *rdata);
int INA3221_write_reg(uint8_t reg, uint16_t wdata);

#endif /* INC_INA3221_H_ */
