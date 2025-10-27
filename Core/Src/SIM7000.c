/*
 * LTE.c
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#include "peripherals.h"
#include "global_variables.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <SIM7000.h>
#include "battery_charger.h"
#include "DS18B20.h"
#include "process.h"
#include "leds.h"

/*------INIZIALIZZAZIONE DEL MODULO LTE------*/
int SIM_Init(void)
{
	char command[256];
	char response[256];
	sprintf(sys.apn, "sensor.net");
	strcpy(sys.TCP.IP_address, config.tcp_IPaddress);
	strcpy(sys.TCP.Port, config.tcp_Port);
//	sprintf(sys.TCP.IP_address, "a");
//	sprintf(sys.TCP.Port, "a");

	memset(response, 0, sizeof(response));

	if(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET)
	{
		SIM_Power_On();
		while(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET);            //Attesa accensione modulo
	}

	SIM_Send_Command("AT\r");                                                                     //Verifica comunicazione
	SIM_Receive_Response(response, 2000);
	if(strstr(response, "OK") == NULL)
	{
		if(huart1.Init.BaudRate != 921600)
		{
			huart1.Init.BaudRate = 921600;
			HAL_UART_Init(SIM_UART);
			SIM_Send_Command("AT+IPR=921600\r");               						              //Baudrate a 921600
			SIM_Wait_Response("OK");
		}
		else
		{
			huart1.Init.BaudRate = 38400;
			HAL_UART_Init(SIM_UART);
			return -1;
		}

	}

	huart1.Init.BaudRate = 921600;
	HAL_UART_Init(SIM_UART);

	SIM_Send_Command("ATE0\r");                                                                   //Non verbose mode
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CPSMS?\r");
	SIM_Receive_Response(response, 5000);

	SIM_Send_Command("AT+CFUN=1\r");                                                              //Full functionality
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CNMP=38\r");                                                             //Modalità solo LTE o NB-IoT
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CMNB=2\r");                                                              //1=CAT-M, 2=NB-IoT, 3=Automatico
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CLTS=1\r");                                                              //Abilitazione sincronizzazione orologio
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CPIN?\r");																  //Controllo PIN
	SIM_Receive_Response(response, 5000);
	if(strstr(response, "READY") == NULL)
	{
		if(strstr(response, "SIM PIN") != NULL)
		{
			SIM_Send_Command("AT+CPIN=0000\r");
			SIM_Receive_Response(response, 5000);
			if(SIM_Wait_Response("OK") != HAL_OK) return -1;
		}
		else
		{
			return -1;
		}
	}

	SIM_Send_Command("AT+CCID\r");                                                                // Verifica SIM card
	SIM_Receive_Response(response, 5000);

	SIM_Send_Command("AT+CGDCONT?\r");
	SIM_Receive_Response(response, 5000);
	if(strstr(response, sys.apn) == NULL || strstr(response, "IPV4V6") != NULL)
	{
		sprintf(command, "AT+CGDCONT=1,\"IP\",\"%s\"\r", sys.apn);                                //Configurazione APN
		SIM_Send_Command(command);
		SIM_Receive_Response(response, 5000);
	}

	SIM_Send_Command("AT+CEREG?\r");                                                              //Controllo registrazione alla rete
	SIM_Receive_Response(response, 5000);
	char* cereg_ptr = strstr(response, "+CEREG:");
	int n = 0, stat_value = 0;
	if(cereg_ptr && sscanf(cereg_ptr, "+CEREG: %d,%d", &n, &stat_value) >= 2)
	{
		if(stat_value == 1 || stat_value == 5)
		{
			goto CSQ_PDP;
		}
	}

	SIM_Send_Command("AT+COPS?\r");                                                               //Operatore attuale
	SIM_Receive_Response(response, 5000);
	char* cops_ptr = strstr(response, "+COPS:");
	int mode = 0, format = 0;
	if(cops_ptr && sscanf(cops_ptr, "+COPS: %d,%d", &mode, &format) >= 2)
	{
		if(strstr(cops_ptr, "vodafone") == NULL)
		{
			SIM_Send_Command("AT+COPS=2\r");                                                          // Deregistra dalla rete
			SIM_Wait_Response("OK");
			HAL_Delay(20000);
		}
	}

	SIM_Send_Command("AT+COPS=0\r");
	SIM_Wait_Response("OK");

	SIM_Send_Command("AT+CEREG?\r");                                                              //Controllo registrazione alla rete
	SIM_Receive_Response(response, 5000);
	int stat = 0;
	uint32_t cereg_start = HAL_GetTick();
	const uint32_t CEREG_TIMEOUT = 30000;
	while(stat != 1 && (HAL_GetTick() - cereg_start) < CEREG_TIMEOUT)
	{
		char* cereg_ptr = strstr(response, "+CEREG:");
		int n = 0, stat_value = 0;
		if(cereg_ptr && sscanf(cereg_ptr, "+CEREG: %d,%d", &n, &stat_value) >= 2)
		{
			if(stat_value == 1 || stat_value == 5)
			{
				stat = 1;
			}
			else
			{
				SIM_Send_Command("AT+CEREG?\r");
				SIM_Receive_Response(response, 5000);
				HAL_Delay(1000);
			}
		}
		else
		{
			SIM_Send_Command("AT+CEREG?\r");
			SIM_Receive_Response(response, 5000);
			HAL_Delay(1000);
		}
	}
	if(stat != 1)
	{
		SIM_Power_Off();
		return -1;  
	}

	SIM_Send_Command("AT+COPS?\r");                                                               //Operatore attuale
	SIM_Receive_Response(response, 5000);

	CSQ_PDP:
	SIM_Send_Command("AT+CSQ\r");																  //Controllo qualità connessione
	SIM_Receive_Response(response, 5000);
	if(strstr(response, "+CSQ: 99") != NULL)
	{
		SIM_Send_Command("AT+CFUN=0\r");     //Reset RF
		SIM_Wait_Response("OK");
		HAL_Delay(2000);
		SIM_Send_Command("AT+CFUN=1\r");
		SIM_Wait_Response("OK");
		HAL_Delay(3000);

		SIM_Send_Command("AT+CSQ\r");
		SIM_Receive_Response(response, 5000);

		if(strstr(response, "+CSQ: 99") != NULL)
		{
			SIM_Power_Off();                 //Power cycle fisico
			return -1;
		}
	}

	SIM_Send_Command("AT+CNACT?\r");                                                              //Verifica indirizzo IP
	SIM_Receive_Response(response, 5000);
	if(SIM_Check_IP(response))
	{
		goto TCP;
	}

	SIM_Send_Command("AT+CIPSHUT\r");
	SIM_Receive_Response(response, 65000);

//	sprintf(command, "AT+CNACT=1,\"%s\"\r", sys.apn);                                             //Attivazione contesto PDP
//	SIM_Send_Command(command);
//	SIM_Wait_Response("OK");
//	SIM_Receive_Response(response, 5000);
//	if(strstr(response, "+APP PDP: ACTIVE") == NULL)
//	{
//		uint32_t pdp_start = HAL_GetTick();
//    	const uint32_t PDP_TIMEOUT = 120000;
//		while(strstr(response, "+APP PDP: ACTIVE") == NULL && (HAL_GetTick() - pdp_start) < PDP_TIMEOUT)
//		{
//			sprintf(command, "AT+CNACT=1,\"%s\"\r", sys.apn);
//			SIM_Send_Command(command);
//			SIM_Wait_Response("OK");
//			SIM_Receive_Response(response, 5000);
//			HAL_Delay(1000);
//		}
//		if(strstr(response, "+APP PDP: ACTIVE") == NULL)
//		{
//			SIM_Power_Off();
//			return -1;
//		}
//	}
//
//	SIM_Send_Command("AT+CNACT?\r");                                                              //Verifica indirizzo IP
//	SIM_Receive_Response(response, 5000);
//	uint32_t ip_start = HAL_GetTick();
//	const uint32_t IP_TIMEOUT = 120000;
//	while(!SIM_Check_IP(response) && (HAL_GetTick() - ip_start) < IP_TIMEOUT)
//	{
//		SIM_Send_Command("AT+CNACT?\r");
//		SIM_Receive_Response(response, 5000);
//		HAL_Delay(1000);
//	}
//	if(!SIM_Check_IP(response))
//	{
//		return -1;
//	}
	
	TCP:
	SIM_Send_Command("AT+CIPRXGET=0\r");                                                         //Impostazione ricezione automatica da server TCP
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	sprintf(command, "AT+CSTT=\"%s\",\"\",\"\"\r", sys.apn);
	SIM_Send_Command(command);
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CIICR\r");
	SIM_Receive_Response(response, 65000);

	SIM_Send_Command("AT+CIFSR\r");
	SIM_Receive_Response(response, 65000);

	const uint32_t MAX_TCP_RETRIES = 3;
	uint32_t retry_count = 0;
	int tcp_connected = 0;
	while(!tcp_connected && retry_count < MAX_TCP_RETRIES)
	{
		sprintf(command, "AT+CIPSTART=\"TCP\",\"%s\",%s\r", sys.TCP.IP_address, sys.TCP.Port);   //Connessione al server TCP
		SIM_Send_Command(command);
		SIM_Wait_Response("OK");
		SIM_Receive_Response(response, 180000);
		
		if(strstr(response, "CONNECT OK") != NULL || strstr(response, "ALREADY CONNECT") != NULL)
		{
			tcp_connected = 1;
			break;
		}
		else if(strstr(response, "CONNECT FAIL") != NULL)
		{
			if(strstr(response, "PDP DEACT") != NULL)
			{
				SIM_Send_Command("AT+CIPSHUT\r");
				SIM_Receive_Response(response, 65000);
			}
			else if(strstr(response, "TCP CLOSED") != NULL)
			{
				return -1;
			}
			else
			{
				SIM_Send_Command("AT+CNACT?\r");
				SIM_Receive_Response(response, 5000);
				if(!SIM_Check_IP(response))
				{
					return -1;  
				}
			}
			
			HAL_Delay(5000);  
			retry_count++;
		}
	}

	if(!tcp_connected)
	{
		return -1;  
	}

//	SIM_Send_Command("AT+CIPSTATUS\r");                                                        //Verifica connessione al server TCP
//	SIM_Wait_Response("OK");
//	SIM_Receive_Response(response, 5000);
//	uint32_t status_start = HAL_GetTick();
//	const uint32_t CIPSTATUS_TIMEOUT = 30000;
//
//	while(!SIM_Check_TCP_State(response) && (HAL_GetTick() - status_start) < CIPSTATUS_TIMEOUT)
//	{
//		SIM_Send_Command("AT+CIPSTATUS\r");
//		SIM_Receive_Response(response, 5000);
//		HAL_Delay(1000);
//	}
//
//	if(!SIM_Check_TCP_State(response))
//	{
//		return -1;
//	}

	return 0;
}

/*------ACCENSIONE DEL MODULO LTE------*/
void SIM_Power_On(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(1500);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
	uint32_t timeout = HAL_GetTick();
    while(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET)
    {
        if(HAL_GetTick() - timeout > 5000) break; 
        HAL_Delay(100);
    }
    HAL_Delay(2000); 
}

/*------SPEGNIMENTO DEL MODULO LTE------*/
void SIM_Power_Off(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(3000);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
	uint32_t timeout = HAL_GetTick();
    while(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_RESET)
    {
        if(HAL_GetTick() - timeout > 5000) break; 
        HAL_Delay(100);
    }
}

/*------RESET DEL MODULO LTE------*/
void SIM_Reset(void)
{
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_SET);
	HAL_Delay(300);
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_RESET);
	while(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET);
}

/*-----SEQUENZA DI ACCENSIONE-----*/
void SIM_Startup_Seq(void)
{
	if(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET)
	{
		SIM_Power_On();
		while(HAL_GPIO_ReadPin(LTE_STATUS_GPIO_Port, LTE_STATUS_Pin) != GPIO_PIN_SET);            //Attesa accensione modulo

	}
	SIM_Reset();
}

/*------INVIO COMANDO AL MODULO LTE------*/
void SIM_Send_Command(char* command)
{
	uint16_t len = (uint16_t)strlen(command);

	HAL_UART_Transmit(SIM_UART, (uint8_t*)command, len, 100);
}

/*------INVIO COMANDO AL MODULO LTE (DMA)------*/
void SIM_Send_Command_DMA(char* command)
{
	uint16_t len = (uint16_t)strlen(command);

	HAL_UART_Transmit_DMA(SIM_UART, (uint8_t*)command, len);
}

/*------RICEZIONE RISPOSTA DAL MODULO LTE------*/
uint16_t SIM_Receive_Response(char* rx, uint32_t timeout_ms)
{
	uint16_t RxLen = 0;
	uint32_t start_time = HAL_GetTick();

	while ((HAL_GetTick() - start_time) < timeout_ms)
	{
		HAL_UARTEx_ReceiveToIdle(SIM_UART, (uint8_t *)rx, 256, &RxLen, 500);
		if (RxLen > 0)
			break;
	}
	return RxLen;
}

/*------CONTROLLO INDIRIZZO IP------*/
int SIM_Check_IP(const char* response)
{
	char* cnact_pos = strstr(response, "+CNACT:");
	if(cnact_pos != NULL) 
	{
		int status;
		char ip_addr[32] = {0};
		if(sscanf(cnact_pos, "+CNACT: %d,%31s", &status, ip_addr) == 2)
		{
			return (status == 1 && strlen(ip_addr) > 0) ? 1 : 0;
		}
	}
	return 0;
}

/*------CONTROLLO STATO CONNESSIONE MQTT------*/
int SIM_Check_MQTT_State(const char* response)
{
    char* smstate_pos = strstr(response, "+SMSTATE:");
    if(smstate_pos != NULL) {
        int mqtt_state;
        if(sscanf(smstate_pos, "+SMSTATE: %d", &mqtt_state) >= 1) {
            return (mqtt_state == 1) ? 1 : 0;
        }
    }
    return 0;
}

/*------CONTROLLO STATO CONNESSIONE TCP------*/
int SIM_Check_TCP_State(const char* response)
{
    char* cipstatus_pos = strstr(response, "+CIPSTATUS: 0");
    if(cipstatus_pos != NULL) {
        // Cerca "CONNECTED" nella stessa riga
        if(strstr(cipstatus_pos, "CONNECT OK") != NULL) {
            return 1;
        }
    }
    return 0;
}

/*------PARSING MESSAGGIO MQTT------*/
void SIM_Parse_Command(void)
{
	char* buf = (char*)sim_rx_buffer;

	if(strncmp(buf, "+CMD,", 5) == 0)
	{
		char* pos = buf + 5;
		// Estrai il valore del comando (cmd_val) come stringa
		char cmd_str[8] = {0};
		int i = 0;
		while(pos[i] != ',' && pos[i] != '\0' && i < 3)
		{
			cmd_str[i] = pos[i];
			i++;
		}
		cmd_str[i] = '\0';

		// Avanza oltre la virgola per eventuale parsing successivo
		char* data_pos = pos + i;
		if(*data_pos == ',') data_pos++;

		if(strcmp(cmd_str, "IDL") == 0)
		{
			flags.CMD.Idle = 1;
		} 
		else if(strcmp(cmd_str, "SRT") == 0) 
		{
			flags.CMD.Start_Meas = 1;
		} 
		else if(strcmp(cmd_str, "PNG") == 0) 
		{
			flags.CMD.Ping = 1;
		} 
		else if(strcmp(cmd_str, "SND") == 0) 
		{
			if(strcmp(data_pos, "1") == 0)
			{
				sys.Log_Request = 1;
			}
			else if(strcmp(data_pos, "0") == 0)
			{
				sys.Log_Request = 0;
			}
		} 
		else if(strcmp(cmd_str, "MSR") == 0) 
		{
			if(!flags.CMD.Measure_Request) 
			{
				LED_Start(RED_LED, FAST, LOW);
				Send_Measure_Addr = sys.Current_RAM_Address;
				flags.CMD.Measure_Request = 1;
				Switch_Buffer();
			}
		} 
		else if(strcmp(cmd_str, "OTA") == 0) 
		{
			if(state == IDLE) 
			{
				flags.CMD.Start_OTA = 1;
			}
		} 
		else if(strcmp(cmd_str, "SET") == 0) 
		{
			if(state == IDLE) 
			{
				flags.CMD.Set_Config = 1;
				SIM_Parse_Cfg(data_pos); 
			}
		} 
		else if(strcmp(cmd_str, "GET") == 0) 
		{
			if(state == IDLE) 
			{
				flags.CMD.Get_Config = 1;
				SIM_Get_Cfg(data_pos);
			}
		} 
		else if(strcmp(cmd_str, "RST") == 0) 
		{
			HAL_NVIC_SystemReset();
		}
	}
}

/*-----PARSING CONFIGURAZIONE-----*/
void SIM_Parse_Cfg(char* cmd_start)
{   
    memset(cfg_var, 0, sizeof(cfg_var));
    memset(new_cfg_val, 0, sizeof(new_cfg_val));
    
    char* pos = cmd_start; // cmd_start arriva già dopo "SET,"

    // Prima virgola
    char* comma1 = strchr(pos, ',');
    if(!comma1) return;

    // Seconda virgola
    char* comma2 = strchr(comma1 + 1, ',');
    if(!comma2) return;

    // Estrai cfg_var (dall'inizio alla prima virgola)
    int var_len = comma1 - pos;
    if(var_len > 0 && var_len < sizeof(cfg_var)) 
    {
        strncpy(cfg_var, pos, var_len);
        cfg_var[var_len] = '\0';
    }

    // Estrai cfg_idx (dalla prima virgola alla seconda)
    cfg_idx = atoi(comma1 + 1);

    // Estrai new_cfg_val (dalla seconda virgola in poi)
    int val_len = strlen(comma2 + 1);
    if(val_len > 0 && val_len < sizeof(new_cfg_val)) 
    {
        strncpy(new_cfg_val, comma2 + 1, val_len);
        new_cfg_val[val_len] = '\0';
    }
}

/*-----RECUPERO VALORE DI CONFIGURAZIONE-----*/
void SIM_Get_Cfg(char* cmd_start)
{   
	memset(cfg_var, 0, sizeof(cfg_var));
	memset(new_cfg_val, 0, sizeof(new_cfg_val));
	
	char* pos = cmd_start;

	// Prima virgola (dopo GET)
	char* comma1 = strchr(pos, ',');
	if(!comma1) return;

	// Seconda virgola
	char* comma2 = strchr(comma1 + 1, ',');
	if(!comma2) return;

	// Estrai cfg_var (tra GET, e prima virgola)
	int var_len = comma1 - pos;
	if(var_len > 0 && var_len < sizeof(cfg_var)) 
	{
		strncpy(cfg_var, pos, var_len);
		cfg_var[var_len] = '\0';
	}

	// Estrai cfg_idx
	cfg_idx = atoi(comma2 + 1);
}

/*------PUBBLICAZIONE MESSAGGIO MQTT IN MODALITA' DMA------*/
void SIM_publish_MQTT_Message_DMA(const char* topic, const char* message)
{
    char command[256];
    uint16_t len = (uint16_t)strlen(message);

    if(topic != NULL && strlen(topic) > 0)
	{
        sprintf(command, "AT+SMPUB=\"%s\",%d,1,0\r", topic, len);
    } 
	else 
	{
        sprintf(command, "AT+SMPUB=%d\r", len);
    }
    
    SIM_Send_Command_DMA(command);
}

/*-----PUBBLICAZIONE MESSAGGIO MQTT-----*/
void SIM_publish_MQTT_Message(const char* topic, const char* message)
{
	char command[256];
	uint16_t len = (uint16_t)strlen(message);

	if(topic != NULL && strlen(topic) > 0)
	{
		sprintf(command, "AT+SMPUB=\"%s\",%d,1,0\r", topic, len);
	} 
	else 
	{
		sprintf(command, "AT+SMPUB=%d\r", len);
	}
	
	SIM_Send_Command(command);
	SIM_Wait_Response(">");                       
	HAL_UART_Transmit(SIM_UART, (uint8_t*)message, strlen(message), 1000);
    SIM_Wait_Response("OK");
}

/*-----INVIO DATI AL SERVER TCP-----*/
void SIM_Send_TCP(char* data)
{
    char cmd[50];
	uint16_t size = (uint16_t)strlen(data);

    sprintf(cmd, "AT+CIPSEND=%u\r", size);
    SIM_Send_Command(cmd);

    SIM_Wait_Response(">");

    HAL_UART_Transmit(SIM_UART, (uint8_t*)data, size, 1000);
    
    SIM_Wait_Response("SEND OK");
}

/*-----INVIO DATI AL SERVER TCP CON DMA-----*/
void SIM_Send_TCP_Chunk_DMA(uint16_t size)
{
    char cmd[18];

    sprintf(cmd, "AT+CIPSEND=%u\r", size);
    SIM_Send_Command_DMA(cmd);
}

/*-----INVIO DATI AL SERVER TCP SENZA DMA-----*/
void SIM_Send_TCP_Chunk(uint16_t size)
{
    char cmd[18];

    sprintf(cmd, "AT+CIPSEND=%u\r", size);
    SIM_Send_Command(cmd);
}

/*-----INVIO INFORMAZIONI AL SERVER MQTT-----*/
void SIM_Send_Infos(void)
{
	uint16_t len = 0;
	char command[18];
	char infos[512];
	uint16_t new_temp = 0;

	BC_MultiRead_Reg(REG3B_VBAT_ADC, &Vbatt);
	INA3221_Read_Measure(&Supply);
	if((new_temp = Read_Temperature()) != 0)
	{
		Temperature = new_temp;
	}
	uint16_t fw_ver = FW_VERSION;

	sprintf(infos, "R:%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u,%u", config.device_id, fw_ver, sys.onDate.Year, sys.onDate.Month, sys.onDate.Date, sys.onTime.Hours, sys.onTime.Minutes, sys.onTime.Seconds, Vbatt, config.samp_freq, config.buffering_secs, Supply.v1, Supply.v2, Supply.v3, Supply.i1, Supply.i2, Supply.i3, Temperature);
	len = (uint16_t)strlen(infos);

	sprintf(command, "AT+CIPSEND=%u\r",len);
	SIM_Send_Command(command);
	SIM_Wait_Response(">");
	HAL_UART_Transmit(SIM_UART, (uint8_t*)infos, len, 100);
	SIM_Wait_Response("OK");
	memset(sim_rx_buffer, 0, sizeof(sim_rx_buffer));
}

/*-----ATTESA RISPOSTA-----*/
int SIM_Wait_Response(const char* expected)
{
    char rx[256];
    memset(rx, 0, sizeof(rx));
    uint16_t timeout = 2000; // 2 secondi
    uint32_t start_time = HAL_GetTick();

    while((HAL_GetTick() - start_time) < timeout)
    {
        uint16_t RxLen = 0;
        HAL_UARTEx_ReceiveToIdle(SIM_UART, (uint8_t*)rx, sizeof(rx), &RxLen, 500);
        
        if(RxLen > 0)
        {
        	if(strstr(rx, expected))
        	{
        		return 0;
        	}
        }
        
        HAL_Delay(10);
    }
	return -1;
}

/*-----CONTROLLA STATO CONNESSIONE-----*/
void SIM_Check_Connection(void)
{
	char command[6];
	char response_sim[256];
	uint32_t start_time;
    const uint32_t CEREG_TIMEOUT = 180000;  
    const uint32_t TCP_TIMEOUT = 120000;     
    const uint32_t MAX_TCP_ATTEMPTS = 5;    


    HAL_UART_DMAStop(SIM_UART);
	memset(sim_rx_buffer, 0, sizeof(sim_rx_buffer));

	int registered = 0;
	start_time = HAL_GetTick();
    while(!registered && (HAL_GetTick() - start_time) < CEREG_TIMEOUT)
    {
        SIM_Send_Command("AT+CEREG?\r");
        SIM_Receive_Response(response_sim, 5000);
        int n = 0, stat_value = 0;
        char* cereg_ptr = strstr(response_sim, "+CEREG:");
        if(cereg_ptr && sscanf(cereg_ptr, "+CEREG: %d,%d", &n, &stat_value) >= 2 && (stat_value == 1 || stat_value == 5))
        {
            registered = 1;
        }
        else
        {
            HAL_Delay(2000);
        }
    }

	if(!registered) 
	{
        HAL_NVIC_SystemReset(); 
    }

	int connected = 0;
	start_time = HAL_GetTick();
    uint32_t tcp_attempts = 0;
    sprintf(command, "H:%u", config.device_id);
	while(!connected && (HAL_GetTick() - start_time) < TCP_TIMEOUT && tcp_attempts < MAX_TCP_ATTEMPTS)
	{
		SIM_Send_Command("AT+CIPSEND=3\r");
		SIM_Wait_Response(">");
		SIM_Send_Command(command);
		SIM_Receive_Response(response_sim, 5000);

		if(strstr(response_sim, "SEND OK") != NULL)
		{
			connected = 1;
		}
		else
		{
			tcp_attempts++;
			HAL_Delay(2000);
		}
	}

	if(!connected)
	{
        HAL_NVIC_SystemReset();
    }

	HAL_UARTEx_ReceiveToIdle_DMA(SIM_UART, (uint8_t *)sim_rx_buffer, SIM_RXBUFFER_SIZE);
}
