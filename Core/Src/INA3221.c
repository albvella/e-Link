/*
 * INA3221.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#include "INA3221.h"
#include "INA3221_reg.h"
#include "peripherals.h"
#include "global_variables.h"

void INA3221_Init()
{
	uint16_t rcheck = 0;

	INA3221_write_reg(INA3221_REG_CONFIG, 0x8000);   //RESET

	HAL_Delay(100);

	INA3221_read_reg(INA3221_REG_MID, &rcheck);

	if(rcheck != INA3221_DEFAULT_MID)
		while(1);

	INA3221_write_reg(INA3221_REG_CONFIG, 0x7D27);   //CH1 CH2 CH3 Enabled, 512 AVG, 1.1ms conv time, continous mode
	INA3221_Read_Measure(&Supply);
}

void INA3221_Read_Measure(supply_bus_t *measure)
{
	INA3221_read_reg(INA3221_REG_BUSVOLTAGE_1, (uint16_t *)&(measure->v1));
	INA3221_read_reg(INA3221_REG_BUSVOLTAGE_2, (uint16_t *)&(measure->v2));
	INA3221_read_reg(INA3221_REG_BUSVOLTAGE_3, (uint16_t *)&(measure->v3));
	INA3221_read_reg(INA3221_REG_SHUNTVOLTAGE_1, (uint16_t *)&(measure->i1));
	INA3221_read_reg(INA3221_REG_SHUNTVOLTAGE_2, (uint16_t *)&(measure->i2));
	INA3221_read_reg(INA3221_REG_SHUNTVOLTAGE_3, (uint16_t *)&(measure->i3));
}


int INA3221_read_reg(uint8_t reg, uint16_t *rdata)
{
	int result = -1;
	uint8_t data[2] = {0};

	if(HAL_I2C_Master_Transmit(I2C, INA3221_ADDR_0 << 1, &reg, 1, 100) == HAL_OK)
	{

		if(HAL_I2C_Master_Receive(I2C,  INA3221_ADDR_0 << 1, data, 2, 100) == HAL_OK)
		{
			result = 0;
			*rdata = (data[0] << 8) | data[1];
		}
	}

	return result;
}


int INA3221_write_reg(uint8_t reg, uint16_t wdata)
{
    int result = -1;
    uint8_t data[3];
    
    data[0] = reg;                    
    data[1] = (wdata >> 8);          
    data[2] = (wdata & 0xFF);        

    if(HAL_I2C_Master_Transmit(I2C, INA3221_ADDR_0 << 1, data, 3, 100) == HAL_OK)
    {
        result = 0;
    }
    
    return result;
}
