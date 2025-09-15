/*
 * LTE.h
 *
 *  Created on: Sep 14, 2024
 *      Author: albve
 */

#ifndef INC_LTE_H_
#define INC_LTE_H_

#include "main.h"

void LTE_Power_On(void);
void LTE_Power_Off(void);
void LTE_Reset(void);
void LTE_Init(void);
void LTE_Send_Command(char* command);
void LTE_Receive_Response(char* response);
int LTE_Check_IP(const char* response);
int LTE_Check_MQTT_State(const char* response);
void LTE_publish_MQTT_Message(const char* topic, const char* message);
#endif /* INC_LTE_H_ */
