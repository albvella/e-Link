/*
 * leds.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */
#include "main.h"
#include "leds.h"
#include "peripherals.h"

/*------ACCENSIONE LED------*/
void LED_Start(uint32_t LED, uint8_t mode)
{
	TIM_OC_InitTypeDef sConfigOC = {0};
	sConfigOC.OCMode = TIM_OCMODE_TIMING;
	sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
	sConfigOC.OCNPolarity = TIM_OCNPOLARITY_HIGH;
	sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
	sConfigOC.OCIdleState = TIM_OCIDLESTATE_RESET;
	sConfigOC.OCNIdleState = TIM_OCNIDLESTATE_RESET;

	switch(mode)
	{
	case ON:
		sConfigOC.Pulse = 49999;
		break;
	case FAST:
		sConfigOC.Pulse = 24999;
		break;
	case SLOW:
		sConfigOC.Pulse = 12499;
		break;
	}

	HAL_TIM_Base_Init(LED_TIMER);
	HAL_TIM_PWM_Init(LED_TIMER);

	switch(LED)
	{
	case GRN_LED:
		HAL_TIM_PWM_ConfigChannel(LED_TIMER, &sConfigOC, LED);
		HAL_TIM_PWM_Start(LED_TIMER, LED);
		break;
	case RED_LED:
		HAL_TIM_PWM_ConfigChannel(LED_TIMER, &sConfigOC, LED);
		HAL_TIM_PWM_Start(LED_TIMER, LED);
		break;
	case ORG_LED:
		HAL_TIM_PWM_ConfigChannel(LED_TIMER, &sConfigOC, LED);
		HAL_TIM_PWM_Start(LED_TIMER, LED);
		break;
	}
}

/*------SPEGNIMENTO LED------*/
void LED_Stop(uint32_t LED)
{
	HAL_TIM_PWM_Stop(LED_TIMER, LED);
}
