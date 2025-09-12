/*
 * extflash.c
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#include <string.h>

#include "main.h"
#include "peripherals.h"
#include "extflash.h"

#define FLASH_SPI_DEF_TIMEOUT 		(100)
#define FLASH_WRITE_ERASE_TIMEOUT 	(1000)
#define FLASH_STATUS_POLL_INTERVAL	(1)

#define EFLASH_DEF_MANIFACTURER (0x9D)
#define EFLASH_DEF_DEVID		(0x17)
#define EFLASH_DEF_PAGE_SIZE 	(256)
#define EFLASH_DEF_SECTOR_SIZE 	(4096)
#define EFLASH_PAGES_PER_SECTOR (EFLASH_DEF_SECTOR_SIZE / EFLASH_DEF_PAGE_SIZE)

#define EFLASH_CMD_NORD			(0x03)	//Normal Read Mode
#define EFLASH_CMD_FRD			(0x0B)	//Fast Read Mode

#define EFLASH_CMD_PP			(0x02)	//Page Program

#define EFLASH_CMD_WREN			(0x06)	//Write Enable
#define EFLASH_CMD_WRDI			(0x04)	//Write Disable

#define EFLASH_CMD_RDSR			(0x05)	//Read Status Register
#define EFLASH_CMD_WRSR			(0x01)	//Write Status Register

#define EFLASH_CMD_RDFR			(0x48)	//Read Function Register
#define EFLASH_CMD_WRFR			(0x42)	//Write Function Register

#define EFLASH_CMD_RDBR			(0x16)	//Read Bank Address Register
#define EFLASH_CMD_RDBR_2		(0xC8)	//Read Bank Address Register



#define EFLASH_CMD_RDID			(0xAB)	//Read Manufacturer and Product ID
#define EFLASH_CMD_RDJID		(0x9F)	//Read Manufacturer and Product ID by JEDEC ID Command
#define EFLASH_CMD_RDMDID		(0x90)	//Read Manufacturer and Device ID
#define EFLASH_CMD_RDJDIDQ		(0xAF)	//Read JEDEC ID QPI mode
#define EFLASH_CMD_RDUID		(0x4B)	//Read Unique ID Number
#define EFLASH_CMD_RDSFDP		(0x5A)	//SFDP Read
#define EFLASH_CMD_CLERP		(0x82)	//Clear Extended Read Register


#define EFLASH_CMD_RDERP		(0x81)	//Read extended read register
#define EFLASH_CMD_CLERP		(0x82)	//Read extended read register

#define EFLASH_CMD_SER			(0xD7)	//Sector erase (4 KB)
#define EFLASH_CMD_BER32		(0x52)	//Sector erase (32 KB)
#define EFLASH_CMD_BER64		(0xD8)	//Sector erase (64 KB)
#define EFLASH_CMD_CER			(0xC7)	//Chip erase


#define STATUS_WIP				(1)
#define STATUS_WEL				(1 << 1)

#define ESTATUS_WIP				(1)
#define ESTATUS_PROT_ERR		(1 << 1)
#define ESTATUS_P_ERR			(1 << 2)
#define ESTATUS_E_ERR			(1 << 3)

#define SFDP_FLASH_DENSITY		(0x34)


typedef struct extflash_cmd{

	uint8_t 	cmd;
	uint8_t		address_en;
	uint16_t	tx_nb;
	uint16_t	rx_nb;
	uint16_t	dummy_nb;

	uint32_t	address;

	uint8_t		*tx_data;
	uint8_t		*rx_data;

}extflash_cmd, *extflash_cmd_t;











uint32_t	exflashSize = 0; //Dimensione della flash in bytes
uint32_t	exflashNumSectors = 0;
uint8_t		exflashInitDone = 0;


void extflash_cs_set()
{
	HAL_GPIO_WritePin(FLASH_nCS_GPIO_Port, FLASH_nCS_Pin, GPIO_PIN_RESET);
}

void extflash_cs_reset()
{
	HAL_GPIO_WritePin(FLASH_nCS_GPIO_Port, FLASH_nCS_Pin, GPIO_PIN_SET);
}

void extflash_wp_set()
{
	HAL_GPIO_WritePin(FLASH_nWP_GPIO_Port, FLASH_nWP_Pin, GPIO_PIN_RESET);
}

void extflash_wp_reset()
{
	HAL_GPIO_WritePin(FLASH_nWP_GPIO_Port, FLASH_nWP_Pin, GPIO_PIN_SET);
}


void extflash_hard_reset()
{

	HAL_GPIO_WritePin(FLASH_nRESET_GPIO_Port, FLASH_nRESET_Pin, GPIO_PIN_RESET);

	HAL_Delay(50);

	HAL_GPIO_WritePin(FLASH_nRESET_GPIO_Port, FLASH_nRESET_Pin, GPIO_PIN_SET);

	return;
}


int32_t extflash_send_cmd(extflash_cmd_t command)
{

	uint8_t addr_bytes[4] = {0};
	uint8_t dummy_bytes[8] = {0};
	uint8_t dummy = 0;
	uint8_t cmd_data = command->cmd;

	if(command->address_en != 0)
	{
		addr_bytes[0] = (command->address >> 16) & 0xFF;
		addr_bytes[1] = (command->address >> 8) & 0xFF;
		addr_bytes[2] = (command->address) & 0xFF;
	}

	extflash_cs_set();

	HAL_SPI_Transmit(EXTFLASH_SPI, &cmd_data, 1, FLASH_SPI_DEF_TIMEOUT);

	if(command->address_en != 0)
	{
		HAL_SPI_Transmit(EXTFLASH_SPI, addr_bytes, 3, FLASH_SPI_DEF_TIMEOUT);
	}

	if(command->dummy_nb > 0)
	{
		dummy = command->dummy_nb > sizeof(dummy_bytes) ? sizeof(dummy_bytes) : command->dummy_nb;
		HAL_SPI_Transmit(EXTFLASH_SPI, dummy_bytes, dummy, FLASH_SPI_DEF_TIMEOUT);
	}

	if(command->tx_nb > 0 && command->tx_data != NULL)
	{
		HAL_SPI_Transmit(EXTFLASH_SPI, command->tx_data, command->tx_nb, FLASH_SPI_DEF_TIMEOUT);
	}

	if(command->rx_nb > 0 && command->rx_data != NULL)
	{
		HAL_SPI_Receive(EXTFLASH_SPI, command->rx_data, command->rx_nb, FLASH_SPI_DEF_TIMEOUT);
	}

	extflash_cs_reset();

	return 0;
}







int extflash_read_status(uint8_t *status)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_RDSR;
	command.address_en = 0;
	command.address = 0;
	command.rx_nb = 1;
	command.rx_data = status;

	return extflash_send_cmd(&command);

}


int extflash_read_extended_read_reg(uint8_t *ereg)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_RDERP;
	command.address_en = 0;
	command.address = 0;
	command.rx_nb = 1;
	command.rx_data = ereg;

	return extflash_send_cmd(&command);
}


int extflash_clear_extended_read_reg()
{
	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_CLERP;

	return extflash_send_cmd(&command);
}


int extflash_write_status(uint8_t status)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_WRSR;
	command.address_en = 0;
	command.address = 0;
	command.tx_nb = 1;
	command.tx_data = &status;

	return extflash_send_cmd(&command);

}

int extflash_set_write_protection(uint8_t enable)
{

	extflash_cmd command = {0};
	command.cmd = enable==0 ? EFLASH_CMD_WREN : EFLASH_CMD_WRDI;

	return extflash_send_cmd(&command);
}

int extflash_read_sfdp(uint32_t regaddr, uint8_t *reg, uint8_t nregs)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_RDSFDP;
	command.address_en = 1;
	command.address = regaddr;
	command.dummy_nb = 1;
	command.rx_nb = nregs;
	command.rx_data = reg;

	return extflash_send_cmd(&command);

}

int extflash_raw_read(uint32_t address, uint8_t *pBuffer, uint16_t nbytes)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_FRD;
	command.address_en = 1;
	command.address = address;
	command.dummy_nb = 1;
	command.rx_nb = nbytes;
	command.rx_data = pBuffer;

	return extflash_send_cmd(&command);

}

int extflash_raw_erase(uint32_t address)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_SER;
	command.address_en = 1;
	command.address = address;

	return extflash_send_cmd(&command);
}

int extflash_raw_page_write(uint32_t address, const uint8_t *pBuffer)
{

	extflash_cmd command = {0};
	command.cmd = EFLASH_CMD_PP;
	command.address_en = 1;
	command.address = address;
	command.tx_nb = EFLASH_DEF_PAGE_SIZE;
	command.tx_data = pBuffer;

	return extflash_send_cmd(&command);
}


int extflash_sector_read(uint32_t sector, uint32_t nsectors, uint8_t *pBuffer)
{
	int result = 0;
	uint8_t ereg = 0;
	uint32_t tmo = HAL_GetTick();
	uint8_t *wPtr = pBuffer;
	uint32_t address = sector * EFLASH_DEF_SECTOR_SIZE;

	if(extflash_read_extended_read_reg(&ereg) < 0)return -1;

	while((ereg & ESTATUS_WIP) && (HAL_GetTick() - tmo < FLASH_WRITE_ERASE_TIMEOUT))
	{
		//Scrittura-erase in corso
		if(extflash_read_extended_read_reg(&ereg) < 0)return -1;
		HAL_Delay(FLASH_STATUS_POLL_INTERVAL);
	}

	while(nsectors > 0)
	{
		result = extflash_raw_read(address, wPtr, EFLASH_DEF_SECTOR_SIZE);
		if(result < 0)return -1;

		address += EFLASH_DEF_SECTOR_SIZE;
		wPtr += EFLASH_DEF_SECTOR_SIZE;
		nsectors--;
	}

	return 0;

}

int extflash_wait_for_wop(uint32_t timeout)
{
	uint8_t ereg = 0;
	uint32_t tmo = HAL_GetTick();

	if(extflash_read_extended_read_reg(&ereg) < 0)return -1;

	while((ereg & ESTATUS_WIP) && (HAL_GetTick() - tmo < timeout))
	{
		//Scrittura-erase in corso
		if(extflash_read_extended_read_reg(&ereg) < 0)return -1;
		HAL_Delay(FLASH_STATUS_POLL_INTERVAL);
	}

	if(ereg & (ESTATUS_PROT_ERR | ESTATUS_P_ERR | ESTATUS_E_ERR))
	{
		return -2; //Erase o write error
	}

	return 0;
}

int extflash_sector_write(uint32_t sector, uint32_t nsectors, const uint8_t *pBuffer)
{
	int result = 0;
	const uint8_t *wPtr = pBuffer;
	uint32_t address = sector * EFLASH_DEF_SECTOR_SIZE;

	extflash_clear_extended_read_reg();

	while(nsectors > 0)
	{
		//Controllo operazioni in corso
		result = extflash_wait_for_wop(FLASH_WRITE_ERASE_TIMEOUT);
		if(result < 0)break;

		//Erase del settore
		result = extflash_set_write_protection(0);
		if(result < 0)break;
		result = extflash_raw_erase(address);
		if(result < 0)break;

		//Attesa ERASE
		result = extflash_wait_for_wop(FLASH_WRITE_ERASE_TIMEOUT);
		if(result < 0)break;

		for(int i=0; i < EFLASH_PAGES_PER_SECTOR; i++)
		{
			result = extflash_set_write_protection(0);
			if(result < 0)break;
			result = extflash_raw_page_write(address, wPtr);
			if(result < 0)break;

			address += EFLASH_DEF_PAGE_SIZE;
			wPtr += EFLASH_DEF_PAGE_SIZE;
			//Attesa write
			result = extflash_wait_for_wop(FLASH_WRITE_ERASE_TIMEOUT);
			if(result < 0)break;
		}

		nsectors--;
	}

	extflash_set_write_protection(1);

	return 0;

}


unsigned int extflash_get_sector_size()
{
	return EFLASH_DEF_SECTOR_SIZE;
}

unsigned int extflash_get_sector_count()
{
	return exflashNumSectors;
}


unsigned int extflash_get_size()
{
	return exflashSize;
}

int extflash_is_initialized()
{
	return exflashInitDone;
}

int extflash_init()
{
	uint8_t manufacturer_id[2] = {0};
	extflash_cmd command = {0};
	uint8_t density[4] = {0};

	exflashInitDone = 0;
	exflashNumSectors = 0;

	extflash_hard_reset();
	extflash_cs_reset();
	extflash_wp_reset();

	command.cmd = EFLASH_CMD_RDMDID;
	command.address_en = 1;
	command.address = 0;
	command.rx_nb = 2;
	command.rx_data = manufacturer_id;

	extflash_send_cmd(&command);

	if(manufacturer_id[0] != EFLASH_DEF_MANIFACTURER || manufacturer_id[1] != EFLASH_DEF_DEVID)
	{
		return -1;
	}

	memset((void *)&command, 0, sizeof(command));

	extflash_read_sfdp(SFDP_FLASH_DENSITY, density, sizeof(density));

	memcpy(&exflashSize, density, sizeof(uint32_t));

	exflashSize += 1;
	exflashSize >>= 3;

	exflashNumSectors = exflashSize / EFLASH_DEF_SECTOR_SIZE;

	exflashInitDone = 1;

	return 0;

}
