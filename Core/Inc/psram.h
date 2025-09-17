/*
 * psram.h
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#ifndef INC_PSRAM_H_
#define INC_PSRAM_H_


int psram_init();
int psram_is_initialized();
int psram_read(uint32_t address, uint32_t nbytes, uint8_t *pBuffer);
int psram_write(uint32_t address, uint32_t nbytes, uint8_t *pBuffer);
int RAM_Write(uint32_t address, uint32_t nbytes, uint8_t *pBuffer);

int psram_sector_read_write(uint8_t write, uint32_t sector, uint32_t nsectors, uint8_t *pBuffer);

unsigned int psram_get_sector_size(); //Dimensione pagina in bytes
unsigned int psram_get_sector_count(); //Numero totale di pagine
unsigned int psram_get_size(); //Dimensione totale in bytes

#endif /* INC_PSRAM_H_ */
