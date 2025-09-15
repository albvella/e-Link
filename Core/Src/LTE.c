/*
 * LTE.c
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#include "LTE.h"
#include "peripherals.h"
#include "global_variables.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*------INIZIALIZZAZIONE DEL MODULO LTE------*/
void LTE_Init(void)
{
	char command[256];
	char response[256];
	sprintf(sys.apn, "a");
	sprintf(sys.MQTT.clientID, "a");
	sprintf(sys.MQTT.server_name, "a");
	sprintf(sys.MQTT.port, "a");
	sprintf(sys.MQTT.username, "a");
	sprintf(sys.MQTT.password, "a");
	sprintf(sys.MQTT.topic, "a");

	LTE_Power_On();
	HAL_Delay(5000);

	LTE_Send_Command("AT+IPR=921600\r");                                                          //baudrate a 921600
	huart1.Init.BaudRate = 921600;
	HAL_UART_Init(LTE_UART);
	LTE_Send_Command("AT+IFC=0,0\r");                                                             //no flow control

	LTE_Send_Command("AT+CFUN=1\r");                                                              //full functionality

	LTE_Send_Command("AT+CNMP=38\r");                                                             //modalità solo LTE o NB-IoT

	LTE_Send_Command("AT+CMNB=2\r");                                                              //NB-IoT

	LTE_Send_Command("AT+NBSC=1\r");                                                              //abilitazione scrambling feature DA VEDERE SE L'OPERATORE LA RICHIEDE

	LTE_Send_Command("AT+CEREG?\r");                                                              //controllo registrazione alla rete
	LTE_Receive_Response(response);
	int stat = 0;
	if(strstr(response, "+CEREG: ") != NULL)
	{
		while(stat != 1)
		{
			if((response[10] == '1') || (response[10] == '5'))
			{
				stat = 1;
			}
			else
			{
				LTE_Send_Command("AT+CEREG?\r");
				LTE_Receive_Response(response);
				HAL_Delay(1000);
			}
		}

	}

	sprintf(command, "AT+CGDCONT=1,\"IP\",\"%s\"\r", sys.apn);                                    //configurazione APN
	LTE_Send_Command(command);

	LTE_Send_Command("AT+CNACT=1\r");                                                             //attivazione della rete
	LTE_Receive_Response(response);
	if(strstr(response, "+APP PDP: ACTIVE") == NULL)
	{
		while(strstr(response, "+APP PDP: ACTIVE") == NULL)
		{
			LTE_Send_Command("AT+CNACT=1\r");
			LTE_Receive_Response(response);
			HAL_Delay(1000);
		}
	}

	LTE_Send_Command("AT+CNACT?\r");                                                              //verifica indirizzo IP
	LTE_Receive_Response(response);
	if(strstr(response, "+CNACT: 1,") == NULL)
	{
		while(strstr(response, "+CNACT: 1,") == NULL)
		{
			LTE_Send_Command("AT+CNACT?\r");
			LTE_Receive_Response(response);
			HAL_Delay(1000);
		}
	}

	sprintf(command, "AT+SMCONF=\"URL\",\"%s\",%s\r", sys.MQTT.server_name, sys.MQTT.port);       //configurazione MQTT
	LTE_Send_Command(command);

	sprintf(command, "AT+SMCONF=\"CLIENTID\",\"%s\"\r", sys.MQTT.clientID);
	LTE_Send_Command(command);

	LTE_Send_Command("AT+SMCONF=\"KEEPTIME\",60\r");

	sprintf(command, "AT+SMCONF=\"USERNAME\",\"%s\"\r", sys.MQTT.username);
	LTE_Send_Command(command);

	sprintf(command, "AT+SMCONF=\"PASSWORD\",\"%s\"\r", sys.MQTT.password);
	LTE_Send_Command(command);

	LTE_Send_Command("AT+SMCONN\r");                                                              //connessione al server MQTT
	LTE_Send_Command("AT+SMSTATE?\r");                                                            //verifica connessione al server MQTT
	LTE_Receive_Response(response);
	if(strstr(response, "+SMSTATE: 1") == NULL)
	{
		while(strstr(response, "+SMSTATE: 1") == NULL)
		{
			LTE_Send_Command("AT+SMSTATE?\r");
			LTE_Receive_Response(response);
			HAL_Delay(1000);
		}
	}

	sprintf(command, "AT+SMSUB=\"%s\",1\r", sys.MQTT.topic);                                      //iscrizione al topic
	LTE_Send_Command(command);

}

/*------ACCENSIONE DEL MODULO LTE------*/
void LTE_Power_On(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(1000);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
}

/*------SPEGNIMENTO DEL MODULO LTE------*/
void LTE_Power_Off(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(1500);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
}

/*------RESET DEL MODULO LTE------*/
void LTE_Reset(void)
{
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_SET);
	HAL_Delay(300);
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_RESET);
}

/*------INVIO COMANDO AL MODULO LTE------*/
void LTE_Send_Command(char* command)
{
	uint16_t len = (uint16_t)strlen(command);

	HAL_UART_Transmit(LTE_UART, (uint8_t*)command, len, 100);
}

/*------RICEZIONE RISPOSTA DAL MODULO LTE------*/
void LTE_Receive_Response(char* response)
{
	uint16_t max_size = 256;
	uint16_t RxLen = 0;

	HAL_UARTEx_ReceiveToIdle(LTE_UART, (uint8_t *)response, max_size, &RxLen, 200);
}

/*------PUBBLICAZIONE MESSAGGIO MQTT------*/
void LTE_publish_MQTT_Message(const char* topic, const char* message)
{
    char command[256];
    uint16_t len = (uint16_t)strlen(message);

    sprintf(command, "AT+SMPUB=\"%s\",%d,1,1\r", topic, len);
    LTE_Send_Command(command);
    LTE_Send_Command((char*)message);
    LTE_Send_Command("\x1A");

}
