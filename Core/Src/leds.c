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
void LED_Start(uint32_t LED, uint8_t freq, uint8_t duty)
{
    TIM_HandleTypeDef *htim = LED_TIMER;
	uint16_t pulse = 0;

    uint16_t prescaler = (uint16_t)(SystemCoreClock / 5000 - 1);
    uint16_t period = 0;

    switch(freq)
    {
        case FAST:  
            period = (uint16_t)((prescaler / 2) - 1);
            break;
        case MEDIUM:
            period = (uint16_t)(prescaler / 1 - 1);
            break;
        case SLOW:
            prescaler = (uint16_t)(SystemCoreClock / 0.5 - 1);
            break;
        case VERY_SLOW:
            prescaler = (uint16_t)(SystemCoreClock / 0.1 - 1);
            break;
        default:
            return;
    }

	switch(duty)
	{
		case FULL:
			pulse = period; 
		    break;
        case HIGH:
			pulse = period * 3 / 4;
			break;
		case HALF:
			pulse = period / 2;
			break;
		case LOW:
			pulse = period / 4;
			break;
        default:
            return;
	}

    // Imposta periodo e prescaler
    htim->Instance->PSC = prescaler;
    htim->Instance->ARR = period;
    htim->Instance->CCR1 = (LED == GRN_LED) ? pulse : htim->Instance->CCR1;
    htim->Instance->CCR2 = (LED == ORG_LED) ? pulse : htim->Instance->CCR2;
    htim->Instance->CCR3 = (LED == RED_LED) ? pulse : htim->Instance->CCR3;

    // Avvia PWM solo se non già attivo
    switch(LED)
    {
        case GRN_LED:
            htim->Instance->CCER |= TIM_CCER_CC1E;
            break;
        case ORG_LED:
            htim->Instance->CCER |= TIM_CCER_CC2E;
            break;
        case RED_LED:
            htim->Instance->CCER |= TIM_CCER_CC3E;
            break;
    }
}

/*------SPEGNIMENTO LED------*/
void LED_Stop(uint32_t LED)
{
	HAL_TIM_PWM_Stop(LED_TIMER, LED);
}
