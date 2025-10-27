/*
 * callbacks.c
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */


#include "main.h"
#include "global_variables.h"
#include "peripherals.h"
#include "string.h"

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
	
	if(Period_cnt >= MAX_VOLUME_SAMPLES)
	{
		Period_cnt = 0;
	}
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
	if(huart == SIM_UART)
	{
		if(*(uint32_t*)sim_rx_buffer == PROMPT)
		{
			if(flags.Log_TransferInProgress)
			{
				flags.Log_ReadytoSend = 1;
				sys.SIM_Prompt_Status = 0;
			}
			else if(flags.CMD.Measure_Request)
			{
				flags.Measure_ReadytoSend = 1;
				sys.SIM_Prompt_Status = 0;
			}
		}

		else if(*(uint32_t*)sim_rx_buffer == SENDOK_H &&
				   *(uint32_t*)(sim_rx_buffer + 4) == SENDOK_L)
		{
			if(flags.Log_TransferInProgress)
			{
				flags.Log_TransferInProgress = 0;
			}
			else if(flags.Meas_TransferInProgress)
			{
				flags.Meas_TransferInProgress = 0;
			}
		}

		else if(*(uint32_t*)sim_rx_buffer == ERROR)
		{
			flags.Log_ReadytoSend = 0;
			sys.SIM_Prompt_Status = 0;
		}

		else if(*(uint32_t*)sim_rx_buffer == COMMAND)
		{     
			flags.Message_Rx = 1;
		}

		else if(strstr(sim_rx_buffer, "CLOSED") != NULL)
		{
			HAL_NVIC_SystemReset();
		}


	}
	
	HAL_UARTEx_ReceiveToIdle_DMA(SIM_UART, sim_rx_buffer, SIM_RXBUFFER_SIZE);
}

/* ------CALLBACK UART RX COMPLETE------*/
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if (huart == SIM_UART)
	{

	}

}

/* ------CALLBACK UART TX COMPLETE------*/
void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)
{
	if (huart == SIM_UART)
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
	RTC_AlarmTypeDef sAlarm = {0};

	HAL_RTC_GetTime(hrtc, &gTime, RTC_FORMAT_BIN);

	sys.Low_th = Low_TH_Array[gTime.Hours];
	sys.High_th = High_TH_Array[gTime.Hours];

	sAlarm.AlarmTime.Hours = 0;
    sAlarm.AlarmTime.Minutes = 0;
    sAlarm.AlarmTime.Seconds = 0;
    sAlarm.AlarmMask = RTC_ALARMMASK_DATEWEEKDAY | RTC_ALARMMASK_HOURS | RTC_ALARMMASK_SECONDS;
    sAlarm.AlarmSubSecondMask = RTC_ALARMSUBSECONDMASK_ALL;
    sAlarm.AlarmDateWeekDaySel = RTC_ALARMDATEWEEKDAYSEL_DATE;
    sAlarm.AlarmDateWeekDay = 1;
    sAlarm.Alarm = RTC_ALARM_A;
    
    HAL_RTC_SetAlarm_IT(hrtc, &sAlarm, RTC_FORMAT_BIN);
}
