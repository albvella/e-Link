/*
 * LTE.h
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#ifndef INC_SIM7000_H_
#define INC_SIM7000_H_

#include "main.h"

void SIM_Power_On(void);
void SIM_Power_Off(void);
void SIM_Reset(void);
int SIM_Init(void);
void SIM_Send_Command(char* command);
void SIM_Send_Command_DMA(char* command);
uint16_t SIM_Receive_Response(char* response, uint32_t timeout_ms);
int SIM_Check_IP(const char* response);
int SIM_Check_MQTT_State(const char* response);
int SIM_Check_TCP_State(const char* response);
void SIM_Parse_Command(void);
void SIM_Parse_Cfg(char* cmd_start);
void SIM_Get_Cfg(char* cmd_start);
void SIM_publish_MQTT_Message_DMA(const char* topic, const char* message);
void SIM_publish_MQTT_Message(const char* topic, const char* message);
void SIM_Send_TCP(uint8_t* data);
void SIM_Send_TCP_Chunk_DMA(uint16_t size);
void SIM_Send_Infos(void);
int SIM_Wait_Response(const char* expected);
void SIM_Check_Connection(void);

#endif /* INC_SIM7000_H_ */
