/*
 * extflash.h
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 *
 *
 *  Driver memoria flash esterna ISSI
 */

#ifndef INC_EXTFLASH_HAL_H_
#define INC_EXTFLASH_HAL_H_


int extflash_init();
int extflash_is_initialized();

unsigned int extflash_get_sector_size(); //Dimensione settore in bytes
unsigned int extflash_get_sector_count(); //Numero totale di settori
unsigned int extflash_get_size(); //Dimensione totale in bytes


int extflash_sector_read(uint32_t sector, uint32_t nsectors, uint8_t *pBuffer);
int extflash_sector_write(uint32_t sector, uint32_t nsectors, const uint8_t *pBuffer);


#endif /* INC_EXTFLASH_HAL_H_ */
