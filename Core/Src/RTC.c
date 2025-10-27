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

    if (strlen(time_start) < 20)
	{
		return 0;
	}

	sDate.Year = (time_start[0] - '0') * 10 + (time_start[1] - '0');
	sDate.Month = (time_start[3] - '0') * 10 + (time_start[4] - '0');
	sDate.Date = (time_start[6] - '0') * 10 + (time_start[7] - '0');

	sTime.Hours = (time_start[9] - '0') * 10 + (time_start[10] - '0');
	sTime.Minutes = (time_start[12] - '0') * 10 + (time_start[13] - '0');
	sTime.Seconds = (time_start[15] - '0') * 10 + (time_start[16] - '0');

    int8_t timezone_quarters = 0;
    if (time_start[17] == '+' || time_start[17] == '-')
    {
        int8_t sign = (time_start[17] == '+') ? 1 : -1;
        timezone_quarters = sign * ((time_start[18] - '0') * 10 + (time_start[19] - '0'));
    }
    int8_t italy_timezone_quarters = Calculate_Italy_Timezone(sDate.Year + 2000, sDate.Month, sDate.Date);
    int8_t timezone_diff = italy_timezone_quarters - timezone_quarters;
    int16_t correction_minutes = timezone_diff * 15;
    Apply_Timezone_Correction(&sDate, &sTime, correction_minutes);

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

/*-----CALCOLA FUSO ORARIO ITALIA (CET/CEST)-----*/
int8_t Calculate_Italy_Timezone(uint16_t year, uint8_t month, uint8_t day)
{
    // CET: GMT+1 (4 quarti d'ora)
    // CEST: GMT+2 (8 quarti d'ora) - ultima domenica marzo → ultima domenica ottobre
    
    if (month < 3 || month > 10)
    {
        return 4;  // CET (inverno)
    }
    else if (month > 3 && month < 10)
    {
        return 8;  // CEST (estate)
    }
    else
    {
        // Marzo o Ottobre - calcola ultima domenica
        if (month == 3)
        {
            uint8_t last_sunday_march = Calculate_Last_Sunday(year, 3);
            return (day >= last_sunday_march) ? 8 : 4;
        }
        else  // month == 10
        {
            uint8_t last_sunday_october = Calculate_Last_Sunday(year, 10);
            return (day < last_sunday_october) ? 8 : 4;
        }
    }
}

/*-----CALCOLA ULTIMA DOMENICA DEL MESE-----*/
uint8_t Calculate_Last_Sunday(uint16_t year, uint8_t month)
{
    uint8_t days_in_month = (month == 3) ? 31 : 31;  // Marzo e Ottobre hanno 31 giorni
    
    for (uint8_t day = days_in_month; day >= 25; day--)
    {
        uint8_t weekday = Calculate_Weekday(year, month, day);
        if (weekday == RTC_WEEKDAY_SUNDAY)
        {
            return day;
        }
    }
    return 31;  // Fallback
}

/*-----APPLICA CORREZIONE TIMEZONE-----*/
void Apply_Timezone_Correction(RTC_DateTypeDef* sDate, RTC_TimeTypeDef* sTime, int16_t correction_minutes)
{
    if (correction_minutes == 0) return;
    
    // Converti tutto in minuti totali
    int32_t total_minutes = sTime->Hours * 60 + sTime->Minutes + correction_minutes;
    int16_t day_correction = 0;
    
    // Gestisci overflow/underflow giorni
    while (total_minutes >= 1440)  // 24 ore = 1440 minuti
    {
        total_minutes -= 1440;
        day_correction++;
    }
    while (total_minutes < 0)
    {
        total_minutes += 1440;
        day_correction--;
    }
    
    // Aggiorna ora
    sTime->Hours = total_minutes / 60;
    sTime->Minutes = total_minutes % 60;
    
    // Aggiorna data se necessario
    if (day_correction != 0)
    {
        Adjust_Date(sDate, day_correction);
    }
}

/*-----AGGIUSTA DATA CON CORREZIONE GIORNI-----*/
void Adjust_Date(RTC_DateTypeDef* sDate, int16_t day_correction)
{
    uint8_t days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    uint16_t full_year = sDate->Year + 2000;
    
    // Anno bisestile
    if ((full_year % 4 == 0 && full_year % 100 != 0) || (full_year % 400 == 0))
    {
        days_in_month[1] = 29;
    }
    
    sDate->Date += day_correction;
    
    // Gestisci overflow mese
    while (sDate->Date > days_in_month[sDate->Month - 1])
    {
        sDate->Date -= days_in_month[sDate->Month - 1];
        sDate->Month++;
        if (sDate->Month > 12)
        {
            sDate->Month = 1;
            sDate->Year++;
            full_year++;
            // Ricalcola giorni per anno bisestile
            if ((full_year % 4 == 0 && full_year % 100 != 0) || (full_year % 400 == 0))
            {
                days_in_month[1] = 29;
            }
            else
            {
                days_in_month[1] = 28;
            }
        }
    }
    
    // Gestisci underflow mese
    while (sDate->Date < 1)
    {
        sDate->Month--;
        if (sDate->Month < 1)
        {
            sDate->Month = 12;
            sDate->Year--;
            full_year--;
            // Ricalcola giorni per anno bisestile
            if ((full_year % 4 == 0 && full_year % 100 != 0) || (full_year % 400 == 0))
            {
                days_in_month[1] = 29;
            }
            else
            {
                days_in_month[1] = 28;
            }
        }
        sDate->Date += days_in_month[sDate->Month - 1];
    }
    
    // Ricalcola giorno settimana
    sDate->WeekDay = Calculate_Weekday(sDate->Year + 2000, sDate->Month, sDate->Date);
}

