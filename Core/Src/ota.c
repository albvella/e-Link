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
#include "base64.h"


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

	sys.OTA_File_isOpen = 1;
	return 0;
}

/*-----RICEZIONE FILE OTA-----*/
int OTA_Receive(void)
{
    uint8_t rx_buffer[800];
    uint8_t len_buffer[5];  
    UINT bytes_written = 0;
    uint8_t bin_buffer[512];
    uint16_t Rx_Len = 0;
    uint16_t expected_len = 0;

    if (!sys.OTA_File_isOpen) 
    {
        return -1; 
    }

    while (1)
    {
        Rx_Len = SIM_Receive_OTA((char*)len_buffer, 10000);
        if (Rx_Len == 0)
        {
            f_close(&sys.OTA_File);
            sys.OTA_File_isOpen = 0;
            return -1;
        }
        
        len_buffer[4] = '\0';
        
        if(strncmp((char*)len_buffer, "EOF", 3) == 0)
        {
            break;
        }

        expected_len = atoi((char*)len_buffer);
        if (expected_len == 0 || expected_len > 512)
        {
            f_close(&sys.OTA_File);
            sys.OTA_File_isOpen = 0;
            return -1;
        }

        uint16_t expected_base64_len = ((expected_len + 2) / 3) * 4;
        uint16_t total_received = 0;
        memset(rx_buffer, 0, sizeof(rx_buffer));
        
        while (total_received < expected_base64_len)
        {
            Rx_Len = SIM_Receive_OTA((char*)&rx_buffer[total_received], 10000);
            
            if (Rx_Len == 0)
            {
                f_close(&sys.OTA_File);
                sys.OTA_File_isOpen = 0;
                return -1;
            }
            
            total_received += Rx_Len;
        }
        
        rx_buffer[expected_base64_len] = '\0';  // Termina stringa
        
        Base64_Decode((char*)rx_buffer, bin_buffer, sizeof(bin_buffer));

        f_write(&sys.OTA_File, bin_buffer, expected_len, &bytes_written);
        if (bytes_written != expected_len)
        {
            f_close(&sys.OTA_File);
            sys.OTA_File_isOpen = 0;
            return -1;
        }
        
        f_sync(&sys.OTA_File);
        SIM_Send_TCP("R:ACK");
    }

    f_close(&sys.OTA_File);
    sys.OTA_File_isOpen = 0;
    return 0;
}

int OTA_CRC_Check(void)
{
	FRESULT fRes = 0;
	UINT read = 0;
	uint32_t ota_crc = 0;
	uint8_t rx_buffer[64];
	uint32_t calc_crc = 0;

	SIM_Receive_Response((char*)rx_buffer, 5000);
	uint8_t crc_bin[4];
	size_t crc_len = Base64_Decode((char*)rx_buffer, crc_bin, sizeof(crc_bin));
	if (crc_len == 4)
	{
		ota_crc = (crc_bin[0] << 24) | (crc_bin[1] << 16) | (crc_bin[2] << 8) | crc_bin[3];
	}
	else
	{
		return -1;
	}

	fRes = f_open(&sys.OTA_File, OTA_FILE_NAME, FA_READ);
	if (fRes != FR_OK)
	{
		return -1;
	}
	sys.OTA_File_isOpen = 1;

	uint32_t size = f_size(&sys.OTA_File);

	__HAL_CRC_DR_RESET(HCRC);
    HAL_CRCEx_Polynomial_Set(HCRC, 0x04c11db7, CRC_POLYLENGTH_32B);
    HAL_CRCEx_Input_Data_Reverse(HCRC, CRC_INPUTDATA_INVERSION_BYTE);
    HAL_CRCEx_Output_Data_Reverse(HCRC, CRC_OUTPUTDATA_INVERSION_ENABLE);
    HCRC->Instance->INIT = 0xFFFFFFFF;
	__HAL_CRC_DR_RESET(HCRC);

	while (size > 0)
	{
		uint8_t buffer[1024];
		UINT to_read = (size > sizeof(buffer)) ? sizeof(buffer) : size;
		if (f_read(&sys.OTA_File, buffer, to_read, &read) != FR_OK || read == 0)
		{
			f_close(&sys.OTA_File);
			return -1;
		}
		for (UINT i = 0; i < read; i++)
        {
            calc_crc = HAL_CRC_Accumulate(HCRC, (uint32_t*)&buffer[i], 1);
        }
		size -= read;
	}

	f_close(&sys.OTA_File);
	sys.OTA_File_isOpen = 0;

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


