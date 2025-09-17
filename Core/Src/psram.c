/*
 * psram.c
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */
#include <string.h>

#include "main.h"
#include "peripherals.h"
#include "psram.h"


#define PSRAM_PAGE_SIZE		(1024)

#define PSRAM_MANUFACTURER 	(0x0D)
#define PSRAM_KGD			(0x5D)

#define PSRAM_DENSITY_8MB	(0)
#define PSRAM_DENSITY_16MB	(1)
#define PSRAM_DENSITY_32MB	(2)
#define PSRAM_DENSITY_64MB	(3)

#define PSRAM_DENSITY_8MB_EADDR		(0x100000)
#define PSRAM_DENSITY_16MB_EADDR	(0x200000)
#define PSRAM_DENSITY_32MB_EADDR	(0x400000)
#define PSRAM_DENSITY_64MB_EADDR	(0x800000)


#define PSRAM_CMD_READ_ID					(0x9F)
#define PSRAM_CMD_QPI_ENABLE				(0x35)
#define PSRAM_CMD_QPI_DISABLE				(0xF5)

#define PSRAM_CMD_READ_SLOW					(0x03) //Max 33 Mhz
#define PSRAM_CMD_READ_FAST					(0x0B)
#define PSRAM_CMD_READ_FAST_QIO				(0xEB)

#define PSRAM_CMD_READ_SLOW_WAIT			(0)
#define PSRAM_CMD_READ_FAST_WAIT			(8)
#define PSRAM_CMD_READ_FAST_QIO_WAIT		(6)

#define PSRAM_CMD_QPI_READ_SLOW_WAIT		(4)
#define PSRAM_CMD_QPI_READ_FAST_WAIT		(4)
#define PSRAM_CMD_QPI_READ_FAST_QIO_WAIT	(6)

#define PSRAM_CMD_WRITE						(0x02)
#define PSRAM_CMD_WRITE_QUAD				(0x38)


volatile uint8_t qspiCmdCompleted = 0;

uint8_t		psramInitDone = 0;
uint8_t		psramQSPI = 0;
uint8_t		psramId[8] = {0};
uint32_t	psramSize = 0;
uint32_t	psramNumPages = 0;


int psram_reset()
{

	QSPI_CommandTypeDef sCommand = {0};

	sCommand.Instruction = 0x66;
	sCommand.InstructionMode = QSPI_INSTRUCTION_1_LINE;
	sCommand.AddressSize = QSPI_ADDRESS_NONE;
	sCommand.NbData = 0;

	if(HAL_QSPI_Command(PSRAM_SPI, &sCommand, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}

	sCommand.Instruction = 0x99;

	if(HAL_QSPI_Command(PSRAM_SPI, &sCommand, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}

	return 0;

}

int psram_qpi_mode_enabled()
{
	return psramQSPI;
}

int psram_qpi_mode(uint8_t enable)
{

	QSPI_CommandTypeDef sCommand = {0};

	if(!psramInitDone)return -1;

	if(psramQSPI==1 && enable == 0)
	{
		sCommand.Instruction = PSRAM_CMD_QPI_DISABLE;
		sCommand.InstructionMode = QSPI_INSTRUCTION_4_LINES;

	}else if(psramQSPI==0 && enable == 1)
	{
		sCommand.Instruction = PSRAM_CMD_QPI_ENABLE;
		sCommand.InstructionMode = QSPI_INSTRUCTION_1_LINE;

	}else{

		return 0;

	}

	if(HAL_QSPI_Command(PSRAM_SPI, &sCommand, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}

	psramQSPI = enable;

	return 0;
}

int psram_read_id(uint8_t *id_data, int id_data_size)
{
	QSPI_CommandTypeDef sCommand = {0};

	if(id_data == NULL || id_data_size < 8)return -2;

	sCommand.Instruction = 0x9F;
	sCommand.InstructionMode = QSPI_INSTRUCTION_1_LINE;
	sCommand.Address = 0;
	sCommand.AddressSize = QSPI_ADDRESS_24_BITS;
	sCommand.AddressMode = QSPI_ADDRESS_1_LINE;
	sCommand.DataMode    = QSPI_DATA_1_LINE;
	sCommand.NbData = 8;
	sCommand.AlternateByteMode = QSPI_ALTERNATE_BYTES_NONE;
	sCommand.DdrMode           = QSPI_DDR_MODE_DISABLE;
	sCommand.DdrHoldHalfCycle  = QSPI_DDR_HHC_ANALOG_DELAY;
	sCommand.SIOOMode          = QSPI_SIOO_INST_EVERY_CMD;

	if(HAL_QSPI_Command(PSRAM_SPI, &sCommand, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}

	if (HAL_QSPI_Receive(PSRAM_SPI, id_data, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}


	return 0;

}

int psram_internal_read_write(uint8_t write, uint32_t address, uint16_t nbytes, uint8_t *pBuffer)
{

	QSPI_CommandTypeDef sCommand = {0};

	sCommand.Address = address;
	sCommand.AlternateByteMode = QSPI_ALTERNATE_BYTES_NONE;
	sCommand.DdrMode           = QSPI_DDR_MODE_DISABLE;
	sCommand.DdrHoldHalfCycle  = QSPI_DDR_HHC_ANALOG_DELAY;
	sCommand.SIOOMode          = QSPI_SIOO_INST_EVERY_CMD;
	sCommand.NbData = nbytes;

	if(psramQSPI)
	{
		//QSPI mode
		sCommand.Instruction = write ? PSRAM_CMD_WRITE_QUAD : PSRAM_CMD_READ_FAST_QIO;
		sCommand.InstructionMode = QSPI_INSTRUCTION_4_LINES;
		sCommand.AddressSize = QSPI_ADDRESS_24_BITS;
		sCommand.AddressMode = QSPI_ADDRESS_4_LINES;
		sCommand.DataMode    = QSPI_DATA_4_LINES;
		sCommand.DummyCycles = write ? 0 : PSRAM_CMD_QPI_READ_FAST_QIO_WAIT;
	}else{
		//SPI mode
		sCommand.Instruction = write ? PSRAM_CMD_WRITE : PSRAM_CMD_READ_FAST;
		sCommand.InstructionMode = QSPI_INSTRUCTION_1_LINE;
		sCommand.AddressSize = QSPI_ADDRESS_24_BITS;
		sCommand.AddressMode = QSPI_ADDRESS_1_LINE;
		sCommand.DataMode    = QSPI_DATA_1_LINE;
		sCommand.DummyCycles = write ? 0 : PSRAM_CMD_READ_FAST_WAIT;
	}

	if(HAL_QSPI_Command(PSRAM_SPI, &sCommand, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
	{
		return -1;
	}

	if(write)
	{
		if (HAL_QSPI_Transmit(PSRAM_SPI, pBuffer, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
		{
			return -1;
		}

	}else{

		if (HAL_QSPI_Receive(PSRAM_SPI, pBuffer, HAL_QSPI_TIMEOUT_DEFAULT_VALUE) != HAL_OK)
		{
			return -1;
		}

	}

	return 0;
}


//Funzione usata da FatFs
int psram_sector_read_write(uint8_t write, uint32_t sector, uint32_t nsectors, uint8_t *pBuffer)
{
	int result = 0;
	uint8_t *wPtr = pBuffer;
	uint32_t address = sector * PSRAM_PAGE_SIZE;

	while(nsectors > 0)
	{
		result = psram_internal_read_write(write, address, PSRAM_PAGE_SIZE, wPtr);
		if(result < 0)return -1;
		address += PSRAM_PAGE_SIZE;
		wPtr += PSRAM_PAGE_SIZE;
		nsectors--;
	}

	return 0;
}



int psram_read_write(uint8_t write, uint32_t address, uint32_t nbytes, uint8_t *pBuffer)
{
	int result = 0;
	uint32_t trBytes = 0;
	uint8_t *wPtr = pBuffer;

	//Check indirizzo
	if(!psramInitDone || pBuffer==NULL)return -1;
	if(address + nbytes >= psramSize)return -2;

	while(nbytes > 0)
	{
		trBytes = nbytes > PSRAM_PAGE_SIZE ? PSRAM_PAGE_SIZE : nbytes;
		result = psram_internal_read_write(write, address, trBytes, wPtr);

		if(result < 0)return -1;

		address += trBytes;
		wPtr += trBytes;
		nbytes -= trBytes;
	}

	return 0;
}

int raw_psram_read_write(uint8_t write, uint32_t address, uint32_t nbytes, uint8_t *pBuffer)
{
	int result = 0;
	uint32_t trBytes = 0;
	uint8_t *wPtr = pBuffer;

	//Check indirizzo
	if(!psramInitDone || pBuffer==NULL)return -1;
	if(address + nbytes >= psramSize)return -2;

	trBytes = 1024 - address % 1024;
	while(nbytes > 0)
	{
		result = psram_internal_read_write(write, address, trBytes, wPtr);

		if(result < 0)return -1;

		address += trBytes;
		wPtr += trBytes;
		nbytes -= trBytes;
		trBytes = nbytes > PSRAM_PAGE_SIZE ? PSRAM_PAGE_SIZE : nbytes;
	}

	return 0;
}


int psram_read(uint32_t address, uint32_t nbytes, uint8_t *pBuffer)
{
	return psram_read_write(0, address, nbytes, pBuffer);
}

int psram_write(uint32_t address, uint32_t nbytes, uint8_t *pBuffer)
{
	return psram_read_write(1, address, nbytes, pBuffer);
}

int RAM_Write(uint32_t address, uint32_t nbytes, uint8_t *pBuffer)
{
	return raw_psram_read_write(1, address, nbytes, pBuffer);
}

int psram_is_initialized()
{
	return psramInitDone;
}

unsigned int psram_get_sector_size()
{
	return PSRAM_PAGE_SIZE;
}

unsigned int psram_get_sector_count()
{
	return psramNumPages;
}

unsigned int psram_get_size()
{
	return psramSize;
}

int psram_init()
{

	uint8_t density = 0xFF;

	psramInitDone = 0;

	if(psram_reset() < 0)return -1;

	memset(psramId, 0xFF, sizeof(psramId));

	if(psram_read_id(psramId, sizeof(psramId)) < 0)return -1;

	density = psramId[2] >> 5;

	if(psramId[0] == PSRAM_MANUFACTURER && psramId[1] == PSRAM_KGD && density <= PSRAM_DENSITY_64MB)
	{
		psramSize = PSRAM_DENSITY_64MB_EADDR;
		psramNumPages = psramSize / PSRAM_PAGE_SIZE;

		psram_qpi_mode(1);

		psramInitDone = 1;
		return 0;
	}else{
		return -1;
	}

}



