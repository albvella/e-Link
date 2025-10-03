/*
 * leds.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */
#include "main.h"
#include "leds.h"
#include "peripherals.h"


/*-----INIZIALIZZAZIONE LEDs-----*/
void LED_Init(void)
{
    LED_TIMER->Instance->CCR1 = 0;
    LED_TIMER->Instance->CCR2 = 0;
    LED_TIMER->Instance->CCR3 = 0;
	HAL_TIM_PWM_Start(LED_TIMER, GRN_LED);
	HAL_TIM_PWM_Start(LED_TIMER, ORG_LED);
	HAL_TIM_PWM_Start(LED_TIMER, RED_LED);
}

/*------ACCENSIONE LED------*/
void LED_Start(uint32_t LED, uint8_t freq, uint8_t duty)
{
    TIM_HandleTypeDef *htim = LED_TIMER;
	uint16_t pulse = 0;

    uint16_t prescaler = (uint16_t)(80000000 / 5000 - 1);
    uint16_t period = 0;

    switch(freq)
    {
        case FAST:  
            period = (uint16_t)((80000000 / prescaler / 4) - 1);
            break;
        case MEDIUM:
            period = (uint16_t)((80000000 / prescaler / 1) - 1);
            break;
        case SLOW:
            period = (uint16_t)((80000000 / prescaler / 0.5) - 1);
            break;
        case VERY_SLOW:
            period = (uint16_t)((80000000 / prescaler / 0.1) - 1);
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
	switch(LED)
    {
    case GRN_LED:
        LED_TIMER->Instance->CCR3 = pulse;
        break;
    case ORG_LED:
        LED_TIMER->Instance->CCR1 = pulse;
        break;
    case RED_LED:
        LED_TIMER->Instance->CCR2 = pulse;
        break;
    }
}

/*------SPEGNIMENTO LED------*/
void LED_Stop(uint32_t LED)
{
	switch(LED)
    {
    case GRN_LED:
        LED_TIMER->Instance->CCR3 = 0;
        break;
    case ORG_LED:
        LED_TIMER->Instance->CCR1 = 0;
        break;
    case RED_LED:
        LED_TIMER->Instance->CCR2 = 0;
        break;
    }
}
