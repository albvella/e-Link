/*
 * battery_charger.c
 *
 *  Created on: Sep 17, 2024
 *      Author: albve
 */

#include "battery_charger.h"
#include "peripherals.h"
#include "global_variables.h"


/*------INIZIALIZZAZIONE BATTERY CHARGER------*/
void BC_Init(void)
{
	BC_Write_Reg(REG00_MINIMAL_SYSTEM_VOLTAGE, 0x0E);           //Tensione minima di uscita con 3 celle = 9V
	BC_MultiWrite_Reg(REG01_CHARGE_VOLTAGE_LIMIT, 0x04EC);      //Limite tensione di carica con 3 celle = 12.6V
	BC_MultiWrite_Reg(REG03_CHARGE_CURRENT_LIMIT, 0x0064);      //Limite corrente di carica con 3 celle = 1A
	BC_Write_Reg(REG10_CHARGER_CONTROL_1, 0x85);                //Tensione di OVP in ingresso = 26V
	BC_Write_Reg(REG14_CHARGER_CONTROL_5, 0x96);                //Informazione sulla presenza dello Ship-FET
	BC_Write_Reg(REG15_MPPT_CONTROL, 0xAB);                     //MPPT attivato, tensione di MPP = 0.875*Vin, misura di 300ms ogni 2 minuti della Vin
	BC_Write_Reg(REG28_CHARGER_MASK_0, 0xE1);                   //Interrupt attivati: Poor source, Power good, VAC2 present, VAC1 present
	BC_Write_Reg(REG29_CHARGER_MASK_1, 0xD7);                   //Interrupt attivati: nessuno
	BC_Write_Reg(REG2A_CHARGER_MASK_2, 0x7F);                   //Interrupt attivati: nessuno
	BC_Write_Reg(REG2B_CHARGER_MASK_3, 0x1F);                   //Interrupt attivati: nessuno
	BC_Write_Reg(REG2C_FAULT_MASK_0, 0xFC);                     //Interrupt attivati: VAC2 over-voltage, VAC1 over-voltage
	BC_Write_Reg(REG2D_FAULT_MASK_1, 0xF4);                     //Interrupt attivati: nessuno
}

/*------SCRITTURA REGISTRO 8 BIT------*/
int BC_Write_Reg(uint8_t reg, uint8_t wdata)
{
	int result = -1;
	uint8_t toSend[2];
	toSend[0] = reg;
	toSend[1] = wdata;

	if(HAL_I2C_Master_Transmit(I2C, BATTERY_CHARGER_ADDR << 1, toSend, 2, 100) == HAL_OK)
	{
		result = 0;
	}

	return result;
}

/*------LETTURA REGISTRO 8 BIT------*/
int BC_Read_Reg(uint8_t reg, uint8_t *rdata)
{
	int result = -1;

	if(HAL_I2C_Master_Transmit(I2C, BATTERY_CHARGER_ADDR, &reg, 1, 100) == HAL_OK)
	{
		if(HAL_I2C_Master_Receive(I2C,  BATTERY_CHARGER_ADDR << 1 | 0x01, rdata, 1, 100) == HAL_OK)
		{
			result = 0;
		}
	}

	return result;
}

/*------SCRITTURA REGISTRO 16 BIT------*/
int BC_MultiWrite_Reg(uint8_t reg, uint16_t wdata)
{
	int result = -1;
	uint8_t toSend[3];
	toSend[0] = reg;
	toSend[1] = (wdata & 0xFF00) >> 8;
	toSend[2] = wdata & 0x00FF;

	if(HAL_I2C_Master_Transmit(I2C, BATTERY_CHARGER_ADDR << 1, toSend, 3, 100) == HAL_OK)
	{
		result = 0;
	}

	return result;
}

/*------LETTURA REGISTRO 16 BIT------*/
int BC_MultiRead_Reg(uint8_t reg, uint16_t *rdata)
{
	int result = -1;
	uint8_t data[2] = {0};

	if(HAL_I2C_Master_Transmit(I2C, BATTERY_CHARGER_ADDR, &reg, 1, 100) == HAL_OK)
	{
		if(HAL_I2C_Master_Receive(I2C,  BATTERY_CHARGER_ADDR << 1 | 0x01, data, 2, 100) == HAL_OK)
		{
			result = 0;
			*rdata = (data[0] << 8) | data[1];
		}
	}

	return result;
}

/*------LETTURA FLAGS DI INTERRUZIONE------*/
int BC_Read_Flags(uint64_t *flags)
{
	int result = -1;
	uint64_t data[6] = {0};

	if(HAL_I2C_Master_Transmit(I2C, BATTERY_CHARGER_ADDR, (uint8_t *) REG22_CHARGER_FLAG_0, 1, 100) == HAL_OK)
	{
		if(HAL_I2C_Master_Receive(I2C,  BATTERY_CHARGER_ADDR << 1 | 0x01, (uint8_t *)data, 6, 100) == HAL_OK)
		{
			result = 0;
			*flags = (data[0] << 40) | (data[1] << 32) | (data[2] << 24) | (data[3] << 16) | (data[4] << 8) | data[5];
		}
	}

	return result;
}

/*------GESTIONE DELLE INTERRUZIONI------*/
void BC_Manage_Interrupts(uint64_t flags)
{
	uint8_t status = 0;

	if((flags & POOR_SOURCE_MASK) != 0)   //INGRESSO NON BUONO
	{

	}

	if((flags & VAC2_CHANGE_MASK) != 0)  //PANNELLO INSERITO O RIMOSSO
	{
		BC_Read_Reg(REG1B_CHARGER_STATUS_0, (uint8_t *)& status);
		if((status & VAC2_PRESENT_MASK) != 0)
		{
			BC_Write_Reg(REG13_CHARGER_CONTROL_4, 0x80); //INSERITA
		}
		else
		{
			BC_Write_Reg(REG13_CHARGER_CONTROL_4, 0x40); //RIMOSSA
		}
	}

	if((flags & VAC1_CHANGE_MASK) != 0)  //TURBINA INSERITA O RIMOSSA
	{

	}
}
