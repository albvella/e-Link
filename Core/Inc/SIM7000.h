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
void SIM_Init(void);
void SIM_Send_Command(char* command);
void SIM_Send_Command_DMA(char* command);
void SIM_Receive_Response(char* response);
int SIM_Check_IP(const char* response);
int SIM_Check_MQTT_State(const char* response);
int SIM_Check_TCP_State(const char* response);
void SIM_Parse_Command(void);
void SIM_Parse_Cfg(char* cmd_start, char* cmd_end);
void SIM_publish_MQTT_Message(const char* topic, const char* message);
void SIM_Send_TCP_Chunk(uint8_t* data, uint16_t size);
void SIM_Wait_Response(const char* expected);
#endif /* INC_SIM7000_H_ */
