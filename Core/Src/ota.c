/*
 * ota.c
 *
 *  Created on: Sep 26, 2025
 *      Author: albve
 */


#include "ota.h"
#include "global_variables.h"
#include "peripherals.h"
#include "FatFs/ff.h"
#include "SIM7000.h"
#include "stdlib.h"
#include "string.h"


/*-----INIZIALIZZAZIONE OTA-----*/
int OTA_Init(void)
{
	FRESULT fRes = 0;

	if (sys.OTA_File_isOpen)
	{
		f_close(&sys.OTA_File);
	}

	sys.OTA_File_isOpen = 0;

	fRes = f_open(&sys.OTA_File, OTA_FILE_NAME, FA_READ | FA_WRITE | FA_CREATE_ALWAYS);

	if (fRes != FR_OK)
	{
		return -1;
	}

	return 0;
}

/*-----RICEZIONE FILE OTA-----*/
int OTA_Receive(void)
{
	uint8_t rx_buffer[1200];
	uint16_t rx_len = 0;
	UINT bytes_written = 0;
	
	SIM_Wait_Response("+CIPRXGET: 1");

	while(1)
	{
		SIM_Send_Command("AT+CIPRXGET=2,1024\r");
		rx_len = SIM_Receive_Response((char*)rx_buffer);

		char *info = strstr((char*)rx_buffer, "+CIPRXGET: 2,");
		if (info) 
		{
			int actual_len = atoi(info + strlen("+CIPRXGET: 2,"));
			char *data_start = strstr(info, "\r\n");
			if (actual_len == 0)
            {
                break;           // Fine file
            }
			if (data_start) 
			{
				data_start += 2; // Salta "\r\n"
				SIM_Wait_Response("OK");
				SIM_Wait_Response("+CIPRXGET: 1");
				f_write(&sys.OTA_File, data_start, actual_len, &bytes_written);
				if(bytes_written != actual_len)
				{
					f_close(&sys.OTA_File);
					return -1; 
				}
			}
			else
			{
				f_close(&sys.OTA_File);
				return -1; 
			}
		}
	}

	f_close(&sys.OTA_File);
    sys.OTA_File_isOpen = 0;
	return 0;
}

int OTA_CRC_Check(void)
{
	FRESULT fRes = 0;
	UINT read = 0;
	uint16_t ota_crc = 0;
	uint8_t rx_buffer[20];

	SIM_Wait_Response("+CIPRXGET: 1");
	SIM_Send_Command("AT+CIPRXGET=2,2\r");
	SIM_Receive_Response((char*)rx_buffer);
	char *info = strstr((char*)rx_buffer, "+CIPRXGET: 2,");

	if (info)
	{
		ota_crc = atoi(info + strlen("+CIPRXGET: 2,"));
	}

	fRes = f_open(&sys.OTA_File, OTA_FILE_NAME, FA_READ);
	if (fRes != FR_OK)
	{
		return -1;
	}
	uint32_t size = f_size(&sys.OTA_File);
	uint16_t calc_crc = HAL_CRC_Calculate(&hcrc, (uint32_t *)&size, 1);
	while (size > 0)
	{
		uint8_t buffer[256];
		UINT to_read = (size > sizeof(buffer)) ? sizeof(buffer) : size;
		if (f_read(&sys.OTA_File, buffer, to_read, &read) != FR_OK || read == 0)
		{
			f_close(&sys.OTA_File);
			return -1;
		}
		calc_crc = HAL_CRC_Calculate(&hcrc, (uint32_t *)buffer, read / 4 + (read % 4 != 0));
		size -= read;
	}

	f_close(&sys.OTA_File);

	if (calc_crc != ota_crc)
	{
		return -1; // CRC non corrisponde
	}
	
	return 0; // CRC OK
}


/*-----APPLICAZIONE UPDATE-----*/
int OTA_Apply(void)
{
	FRESULT fRes = 0;
	int32_t result = 0;
	uint8_t ota_bank = 0;
	uint32_t faddr = 0;
	uint32_t size = 0;
	uint64_t pword = 0;
	uint32_t faddr_off = 0;
	uint16_t crc = 0;
	UINT read = 0;
	uint32_t PageError = 0;
	FLASH_EraseInitTypeDef erase_cfg = {0};

	const uint32_t BANKSIZE = FLASH_SIZE >> 1;

	FLASH_OBProgramInitTypeDef ob = {0};

	HAL_FLASHEx_OBGetConfig(&ob);

	if ((ob.USERConfig & FLASH_OPTR_DUALBANK) == 0)
	{
		return -1;
	}

	ota_bank = (ob.USERConfig & FLASH_OPTR_BFB2) ? FLASH_BANK_1 : FLASH_BANK_2;

	// L'indirizzo deve essere sempre quello del banco 2 (se fa il boot da BANK2 il BANK1 viene rimappato)
	faddr = FLASH_BASE + BANKSIZE;

	if (HAL_FLASH_Unlock() != HAL_OK)
	{
		return -1;
	}

	f_close(&sys.OTA_File);
	fRes = f_open(&sys.OTA_File, OTA_FILE_NAME, FA_READ);

	if (fRes != FR_OK)
	{
		result = -1;
		goto DONE;
	}

	if ((size = f_size(&sys.OTA_File)) > BANKSIZE)
	{
		result = -1;
		goto DONE;
	}

	erase_cfg.TypeErase = FLASH_TYPEERASE_MASSERASE;
	erase_cfg.Banks = ota_bank;

	if (HAL_FLASHEx_Erase(&erase_cfg, &PageError) != HAL_OK)
	{
		result = -1;
		goto DONE;
	}

	while (size > 0)
	{
		pword = 0;
		if (f_read(&sys.OTA_File, (uint8_t *)&pword, sizeof(pword), &read) < 0)
			break;
		if (read == 0)
			break;
		if (HAL_FLASH_Program(FLASH_TYPEPROGRAM_DOUBLEWORD, faddr + faddr_off, pword) != HAL_OK)
			break;
		faddr_off += sizeof(pword);
		size -= read;
	}

	if (size > 0)
	{
		result = -1;
		goto DONE;
	}

	HAL_FLASH_Lock();

	HAL_FLASHEx_OBGetConfig(&ob);
	HAL_FLASH_Unlock();
	HAL_FLASH_OB_Unlock();

	ob.OptionType = OPTIONBYTE_USER;
	ob.USERType = OB_USER_BFB2;
	ob.USERConfig = (ota_bank == FLASH_BANK_2) ? FLASH_OPTR_BFB2 : 0;

	if (HAL_FLASHEx_OBProgram(&ob) != HAL_OK)
	{
		HAL_FLASH_OB_Lock();
		HAL_FLASH_Lock();
		result = -1;
		goto DONE;
	}

	HAL_FLASH_OB_Launch();
	HAL_FLASH_OB_Lock();
	HAL_FLASH_Lock();

	DONE:

	f_close(&sys.OTA_File);

	HAL_FLASH_Lock();

	return result;
}
