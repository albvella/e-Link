/*
 * callbacks.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */


#include "main.h"
#include "global_variables.h"
#include "peripherals.h"

/* ------CALLBACK TIMER FLUSSO------*/
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef* htim)
{
	T_current = TIM2->CCR1;
	V_Period = T_current - T_prev;

	if(T_current < T_prev)
	{
		V_Period = 4294967295 - T_prev + T_current;
	}

	Volume_Period[Period_cnt] = V_Period;
	T_prev = T_current;
	Period_cnt++;
}

/* ------CALLBACK GPIO------*/
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
	switch(GPIO_Pin)
	{
	case BTN_INTERRUPT:

		break;
	case BC_INTERRUPT:
		flags.BC_Interrupt = 1;
		break;
	case ACC_INTERRUPT:
		lsm6dsv16x_fifo_status_get(&acc, &fifo_status);
		num = fifo_status.fifo_level;
		if (num > ACC_FIFO_WATERMARK)
		{
			num = ACC_FIFO_WATERMARK;
		}
		lsm6dsv16x_read_reg(&acc, LSM6DSV16X_FIFO_DATA_OUT_TAG, (uint8_t*)&Acceleration, 7*num);
		flags.ACC_Complete=1;
		break;
	case RI_INTERRUPT:

		break;
	default:
		break;
	}
}

/* ------CALLBACK UART RX IDLE------*/
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
	if (huart == LTE_UART)
	{

	}

}

/* ------CALLBACK UART RX COMPLETE------*/
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if (huart == LTE_UART)
	{

	}

}

/* ------CALLBACK UART TX COMPLETE------*/
void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)
{
	if (huart == LTE_UART)
	{

	}

}

/* ------CALLBACK HALF ADC------*/
void HAL_ADC_ConvHalfCpltCallback(ADC_HandleTypeDef *hadc)
{
	if(hadc == PRESSURE_ADC)
	{
		flags.ADC_Complete = 1;
		flags.ADC_Half_Buffer = 1;
	}
}

/*------CALLBACK FULL ADC------*/
void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef *hadc)
{
	if(hadc == PRESSURE_ADC)
	{
		flags.ADC_Complete = 1;
		flags.ADC_Full_Buffer = 1;
	}
}

/*------CALLBACK RTC CAMBIO ORA------*/
void HAL_RTC_AlarmAEventCallback(RTC_HandleTypeDef *hrtc)
{
	RTC_TimeTypeDef gTime;

	HAL_RTC_GetTime(hrtc, &gTime, RTC_FORMAT_BIN);

	sys.Low_th = Low_TH[gTime.Hours];
	sys.High_th = High_TH[gTime.Hours];
}
