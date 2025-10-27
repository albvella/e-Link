/*
 * DS18B20.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#include "DS18B20.h"
#include "global_variables.h"
#include "peripherals.h"
#include "stm32l4xx_ll_usart.h"
#include "main.h"


/*------INIZIALIZZAZIONE SENSORE DI TEMPERATURA------*/
void Temp_Sensor_Init(void)
{
	uint8_t data = 0xF0;

	LL_USART_SetBaudRate(huart4.Instance, HAL_RCC_GetPCLK1Freq(), UART_OVERSAMPLING_16, 9600);
//	UART4->CR1 &= ~(USART_CR1_UE);  // Disabilita UART
//	UART4->BRR = 9600;       // Imposta nuovo baud rate
//	UART4->CR1 |= USART_CR1_UE;      // Riabilita UART

	HAL_UART_Transmit(TEMP_UART, &data, 1, 100);  // low for 500+us
	if (HAL_UART_Receive(TEMP_UART, &data, 1, 1000) != HAL_OK)
		while(1);

	LL_USART_SetBaudRate(huart4.Instance, HAL_RCC_GetPCLK1Freq(), UART_OVERSAMPLING_16, 115200);
//	UART4->CR1 &= ~(USART_CR1_UE);  // Disabilita UART
//	UART4->BRR = 115200;       // Imposta nuovo baud rate
//	UART4->CR1 |= USART_CR1_UE;      // Riabilita UART

	if (data == 0xF0)
		while(1);
}

/*------SCRITTURA SU SENSORE DI TEMPERATURA------*/
void Temp_Sensor_Write(uint8_t data)
{
	uint8_t buffer[8];

	for (int i=0; i<8; i++)
	{
		if ((data & (1<<i))!=0)  // if the bit is high
		{
			buffer[i] = 0xFF;  // write 1
		}
		else  // if the bit is low
		{
			buffer[i] = 0;  // write 0
		}
	}

	HAL_UART_Transmit(TEMP_UART, buffer, 8, 100);
}

/*------LETTURA BYTE DA SENSORE DI TEMPERATURA------*/
uint8_t Temp_Sensor_ReadByte(void)
{
	uint8_t RxByte = 0;
	for (uint8_t i = 0; i < 8; i++)
	{
		RxByte >>= 1;
		if (Temp_Sensor_ReadBit())
		{
			RxByte |= 0x80;
		}
	}
	return RxByte;
}

/*------LETTURA BIT DA SENSORE DI TEMPERATURA------*/
uint8_t Temp_Sensor_ReadBit(void)
{
    uint8_t ReadBitCMD = 0xFF;
    uint8_t RxBit;

    // Send Read Bit CMD
    HAL_UART_Transmit(TEMP_UART, &ReadBitCMD, 1, 100);
    // Receive The Bit
    HAL_UART_Receive(TEMP_UART, &RxBit, 1, 1000);

    return (RxBit & 0x01);
}

/*-----INIZIO CONVERSIONE-----*/
void Temp_Start_Conversion(void)
{
	Temp_Sensor_Init();
	Temp_Sensor_Write(0xCC);  // skip ROM
	Temp_Sensor_Write(0x44);  // convert T
}

/*------INIZIALIZZAZIONE E LETTURA TEMPERATURA------*/
uint16_t Temperature_Init(void)
{
	Temp_Start_Conversion();
	HAL_Delay(2000);
	return Read_Temperature();
}



/*------LETTURA TEMPERATURA------*/
uint16_t Read_Temperature(void)
{
	uint8_t Temp_LSB = 0;
	uint8_t Temp_MSB = 0;
	uint16_t Temp = 0;

	Temp_Sensor_Init();
	Temp_Sensor_Write(0xCC);  // skip ROM
	Temp_Sensor_Write(0xBE);         // read Scratch-pad
	Temp_LSB = Temp_Sensor_ReadByte();
	Temp_MSB = Temp_Sensor_ReadByte();
	Temp = ((Temp_MSB << 8)) | Temp_LSB;
	if (Temp != 0x0550 && Temp != 0x0000 && Temp != 0xFFFF)
	{
		Temp_Start_Conversion();
		return Temp;
	}

	return 0;
}
