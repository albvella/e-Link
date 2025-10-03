/*
 * RTC.c
 *
 *  Created on: Sep 17, 2025
 *      Author: albve
 */
#include "RTC.h"


/*-----INIZiALIZZAZIONE ORA RTC-----*/
void RTC_Init(void)
{
	for (int retry = 0; retry < 3; retry++)
	{
		if (Get_DateTime_From_Network())
		{
			return;
		}
		HAL_Delay(1000);
	}
	Set_Default_DateTime();
}

/*-----SINCRONIZZAZIONE RTC DA RETE-----*/
int Get_DateTime_From_Network(void)
{
	char response[100] = {0};
	RTC_DateTypeDef sDate = {0};
	RTC_TimeTypeDef sTime = {0};

	SIM_Send_Command("AT+CCLK?\r");
	SIM_Receive_Response(response, 5000);

    char* cclk_pos = strstr(response, "+CCLK: \"");
    if (cclk_pos == NULL)
	{
        return 0;
    }

    char* time_start = cclk_pos + 8;

    if (strlen(time_start) < 17)
	{
		return 0;
	}

	sDate.Year = (time_start[0] - '0') * 10 + (time_start[1] - '0');
	sDate.Month = (time_start[3] - '0') * 10 + (time_start[4] - '0');
	sDate.Date = (time_start[6] - '0') * 10 + (time_start[7] - '0');

	sTime.Hours = (time_start[9] - '0') * 10 + (time_start[10] - '0');
	sTime.Minutes = (time_start[12] - '0') * 10 + (time_start[13] - '0');
	sTime.Seconds = (time_start[15] - '0') * 10 + (time_start[16] - '0');

	if (sDate.Month < 1 || sDate.Month > 12 ||
        sDate.Date < 1 || sDate.Date > 31 ||
        sTime.Hours > 23 || sTime.Minutes > 59 || sTime.Seconds > 59) {
        return 0;
    }

	sDate.WeekDay = Calculate_Weekday(sDate.Year + 2000, sDate.Month, sDate.Date);
	sTime.DayLightSaving = RTC_DAYLIGHTSAVING_NONE;
	sTime.StoreOperation = RTC_STOREOPERATION_RESET;

	HAL_RTC_SetDate(&hrtc, &sDate, RTC_FORMAT_BIN);
	HAL_RTC_SetTime(&hrtc, &sTime, RTC_FORMAT_BIN);

    sys.onDate = sDate;
    sys.onTime = sTime;
    
	return 1;
}

/*-----DATA E ORA DI DEFAULT 1/1/2020 00:00:00-----*/
void Set_Default_DateTime(void)
{
    RTC_DateTypeDef sDate = {0};
    RTC_TimeTypeDef sTime = {0};

    // Default: 01/01/2020 00:00:00
    sDate.Year = 20;  // 2020
    sDate.Month = RTC_MONTH_JANUARY;
    sDate.Date = 1;
    sDate.WeekDay = RTC_WEEKDAY_WEDNESDAY; // 1 Jan 2020 era mercoledì

    sTime.Hours = 0;
    sTime.Minutes = 0;
    sTime.Seconds = 0;
    sTime.DayLightSaving = RTC_DAYLIGHTSAVING_NONE;
    sTime.StoreOperation = RTC_STOREOPERATION_RESET;

    HAL_RTC_SetDate(&hrtc, &sDate, RTC_FORMAT_BIN);
    HAL_RTC_SetTime(&hrtc, &sTime, RTC_FORMAT_BIN);

    sys.onDate = sDate;
    sys.onTime = sTime;
}

/*-----CALCOLO GIORNO SETTIMANA-----*/
uint8_t Calculate_Weekday(uint16_t year, uint8_t month, uint8_t day)
{
    // Algoritmo di Zeller per calcolo giorno settimana
    if (month < 3) {
        month += 12;
        year--;
    }
    uint8_t zeller_day = (day + ((13 * (month + 1)) / 5) + year + (year / 4) - (year / 100) + (year / 400)) % 7;

    uint8_t hal_weekday_map[] = {RTC_WEEKDAY_SATURDAY, RTC_WEEKDAY_SUNDAY, RTC_WEEKDAY_MONDAY,
                                 RTC_WEEKDAY_TUESDAY, RTC_WEEKDAY_WEDNESDAY, RTC_WEEKDAY_THURSDAY, RTC_WEEKDAY_FRIDAY};

    return hal_weekday_map[zeller_day];
}


