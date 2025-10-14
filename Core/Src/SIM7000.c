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
	sprintf(sys.apn, "iot.1nce.net");
	strcpy(sys.TCP.IP_address, config.tcp_IPaddress);
	strcpy(sys.TCP.Port, config.tcp_Port);
	sprintf(sys.TCP.IP_address, "a");
	sprintf(sys.TCP.Port, "a");

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
	SIM_Wait_Response("OK");


	SIM_Send_Command("AT+CFUN=1\r");                                                              //Full functionality
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CNMP=38\r");                                                             //Modalità solo LTE o NB-IoT
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CMNB=1\r");                                                              //1=CAT-M, 2=NB-IoT, 3=Automatico
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
			SIM_Send_Command("AT+CFUN=1,1\r");   // Software reset
			HAL_Delay(12000);          
			memset(response, 0, sizeof(response));           
			
			SIM_Send_Command("AT+CSQ\r");
			SIM_Receive_Response(response, 5000);
			if(strstr(response, "+CSQ: 99") != NULL)
			{
				SIM_Power_Off();                 //Power cycle fisico
				return -1;
			}
		}
	}

	SIM_Send_Command("AT+CEREG?\r");                                                              //Controllo registrazione alla rete
	SIM_Receive_Response(response, 5000);
	char* cereg_ptr = strstr(response, "+CEREG:");
	int n = 0, stat_value = 0;
	if(cereg_ptr && sscanf(cereg_ptr, "+CEREG: %d,%d", &n, &stat_value) >= 2)
	{
		if(stat_value == 1 || stat_value == 5)
		{
			goto APN;
		}
	}

	SIM_Send_Command("AT+COPS?\r");																  //Controllo modalità di connessione
	SIM_Receive_Response(response, 5000);

	SIM_Send_Command("AT+COPS=?\r");
	SIM_Receive_Response(response, 120000);

	SIM_Send_Command("AT+COPS=0,0\r");                                                            // Miglior operatore disponibile. In caso di operatore fisso: AT+COPS=1,2,\"22201\" ---- 22201: TIM,  22210: Vodafone
	SIM_Receive_Response(response, 180000);
//	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CEREG?\r");                                                              //Controllo registrazione alla rete
	SIM_Receive_Response(response, 5000);
	int stat = 0;
	while(stat != 1)
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

	APN:
	SIM_Send_Command("AT+CNACT?\r");                                                              //Verifica indirizzo IP
	SIM_Receive_Response(response, 5000);
	if(SIM_Check_IP(response))
	{
		goto TCP;
	}

	sprintf(command, "AT+CGDCONT=1,\"IP\",\"%s\"\r", sys.apn);                                    //Configurazione APN
	SIM_Send_Command(command);
	SIM_Receive_Response(response, 5000);
	if(strstr(response, "ERROR") != NULL)
	{
		return -1;
	}

	SIM_Send_Command("AT+CNACT=1\r");                                                             //Attivazione della rete
	SIM_Receive_Response(response, 5000);
	if(strstr(response, "+APP PDP: ACTIVE") == NULL)
	{
		while(strstr(response, "+APP PDP: ACTIVE") == NULL)
		{
			SIM_Send_Command("AT+CNACT=1\r");
			SIM_Receive_Response(response, 5000);
			HAL_Delay(1000);
		}
	}

	SIM_Send_Command("AT+CNACT?\r");                                                              //Verifica indirizzo IP
	SIM_Receive_Response(response, 5000);
	while(!SIM_Check_IP(response))
	{
		SIM_Send_Command("AT+CNACT?\r");
		SIM_Receive_Response(response, 5000);
		HAL_Delay(1000);
	}
	
	TCP:
	SIM_Send_Command("AT+CIPRXGET=0\r");                                                         //Impostazione ricezione automatica da server TCP
	if(SIM_Wait_Response("OK") != HAL_OK) return -1;

	sprintf(command, "AT+CIPSTART=\"TCP\",\"%s\",%s\r", sys.TCP.IP_address, sys.TCP.Port);       //Connessione TCP
	SIM_Send_Command(command);
	if(SIM_Wait_Response("CONNECT OK") != HAL_OK) return -1;

	SIM_Send_Command("AT+CIPSTATUS=0\r");                                                        //Verifica connessione al server TCP
	SIM_Receive_Response(response, 5000);
	while(!SIM_Check_TCP_State(response))
	{
		SIM_Send_Command("AT+CIPSTATUS=0\r");
		SIM_Receive_Response(response, 5000);
		HAL_Delay(1000);
	}

	return 0;
}

/*------ACCENSIONE DEL MODULO LTE------*/
void SIM_Power_On(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(1500);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
}

/*------SPEGNIMENTO DEL MODULO LTE------*/
void SIM_Power_Off(void)
{
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_SET);
	HAL_Delay(1500);
	HAL_GPIO_WritePin(LTE_POWER_ON_GPIO_Port, LTE_POWER_ON_Pin, GPIO_PIN_RESET);
}

/*------RESET DEL MODULO LTE------*/
void SIM_Reset(void)
{
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_SET);
	HAL_Delay(300);
	HAL_GPIO_WritePin(LTE_RESET_GPIO_Port, LTE_RESET_Pin, GPIO_PIN_RESET);
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
        if(strstr(cipstatus_pos, "CONNECTED") != NULL) {
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
		while(pos[i] != ',' && pos[i] != '\0' && i < 7) 
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
				flags.CMD.Data_Request = 1;
			}
			else if(strcmp(data_pos, "0") == 0)
			{
				flags.CMD.Data_Request = 0;
			}
		} 
		else if(strcmp(cmd_str, "MSR") == 0) 
		{
			if(!flags.CMD.Measure_Request) 
			{
				LED_Start(RED_LED, FAST, LOW);
				Send_Measure_Addr = Saved_Bytes;
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
    
	char* pos = cmd_start + 4; // Salta "SET,"

	// Prima virgola (dopo SET)
	char* comma1 = strchr(pos, ',');
	if(!comma1) return;

	// Seconda virgola
	char* comma2 = strchr(comma1 + 1, ',');
	if(!comma2) return;

	// Terza virgola
	char* comma3 = strchr(comma2 + 1, ',');
	if(!comma3) return;

	// Estrai cfg_var (tra SET, e prima virgola)
	int var_len = comma2 - comma1 - 1;
	if(var_len > 0 && var_len < sizeof(cfg_var)) 
	{
		strncpy(cfg_var, comma1 + 1, var_len);
		cfg_var[var_len] = '\0';
	}

	// Estrai cfg_idx
	cfg_idx = atoi(comma2 + 1);

	// Estrai new_cfg_val
	int val_len = strlen(comma3 + 1);
	if(val_len > 0 && val_len < sizeof(new_cfg_val)) 
	{
		strncpy(new_cfg_val, comma3 + 1, val_len);
		new_cfg_val[val_len] = '\0';
	}
}

/*-----RECUPERO VALORE DI CONFIGURAZIONE-----*/
void SIM_Get_Cfg(char* cmd_start)
{   
	memset(cfg_var, 0, sizeof(cfg_var));
	memset(new_cfg_val, 0, sizeof(new_cfg_val));
	
	char* pos = cmd_start + 4; // Salta "GET,"

	// Prima virgola (dopo GET)
	char* comma1 = strchr(pos, ',');
	if(!comma1) return;

	// Seconda virgola
	char* comma2 = strchr(comma1 + 1, ',');
	if(!comma2) return;

	// Estrai cfg_var (tra GET, e prima virgola)
	int var_len = comma2 - comma1 - 1;
	if(var_len > 0 && var_len < sizeof(cfg_var)) 
	{
		strncpy(cfg_var, comma1 + 1, var_len);
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
    char cmd[50];

    sprintf(cmd, "AT+CIPSEND=%u\r", size);
    SIM_Send_Command_DMA(cmd);
}

/*-----INVIO INFORMAZIONI AL SERVER MQTT-----*/
void SIM_Send_Infos(void)
{
	uint16_t len = 0;
	char command[128];
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
}

/*-----ATTESA RISPOSTA-----*/
int SIM_Wait_Response(const char* expected)
{
    char rx[256];
    memset(rx, 0, sizeof(rx));
    uint16_t timeout = 10000; // 10 secondi
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
	char command_sim[256];
	char response_sim[256];
	uint32_t start_time;
    const uint32_t CEREG_TIMEOUT = 180000;  
    const uint32_t TCP_TIMEOUT = 120000;     
    const uint32_t MAX_TCP_ATTEMPTS = 5;    

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

	SIM_Send_Command("AT+CIPSTATUS=0\r");                                                        
	SIM_Receive_Response(response_sim, 5000);
	start_time = HAL_GetTick();
    uint32_t tcp_attempts = 0;
	while(!SIM_Check_TCP_State(response_sim) && (HAL_GetTick() - start_time) < TCP_TIMEOUT && tcp_attempts < MAX_TCP_ATTEMPTS)
	{
		sprintf(command_sim, "AT+CIPSTART=\"TCP\",\"%s\",%s\r", sys.TCP.IP_address, sys.TCP.Port);       
		SIM_Send_Command(command_sim);
		SIM_Wait_Response("CONNECT OK");
		SIM_Send_Command("AT+CIPSTATUS=0\r");                                                        
		SIM_Receive_Response(response_sim, 5000);
		tcp_attempts++;
		HAL_Delay(2000);
	}

	if(!SIM_Check_TCP_State(response_sim)) 
	{
        HAL_NVIC_SystemReset();
    }
}
