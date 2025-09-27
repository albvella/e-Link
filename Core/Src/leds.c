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
void LED_Start(uint32_t LED, uint32_t freq_hz, uint8_t mode)
{
    TIM_HandleTypeDef *htim = LED_TIMER;
    uint32_t prescaler = (uint32_t)(SystemCoreClock / 1000000 - 1);
    uint32_t period = (prescaler / freq_hz) - 1;
	uint32_t pulse = 0;

	switch(mode)
	{
		case ON:
			pulse = period; 
		    break;
		case FAST:
			pulse = period / 2;
			break;
		case SLOW:
			pulse = period / 4;
			break;
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
