/*
 * init.c
 *
 *  Created on: Sep 17, 2024
 *      Author: albve
 */

#include <SIM7000.h>
#include "init.h"
#include "peripherals.h"
#include "global_variables.h"
#include "leds.h"
#include "FatFs/ff.h"
#include "battery_charger.h"
#include "string.h"
#include "lsm6dsv16x_reg.h"
#include "lsm6dsv16x_rw.h"
#include "DS18B20.h"

/*-----INIZiALIZZAZIONE SISTEMA-----*/
void System_Init(void)
{
	acc.write_reg = acc_write;
	acc.read_reg = acc_read;
	acc.handle = &hspi3;

	LED_Init();	
	LED_Start(GRN_LED, FAST, HIGH);

	BC_Init();
	INA3221_Init();
	FatFS_Init();
	Config_Init();
	Acc_Init(&acc, config.samp_freq);
	Temperature = Temperature_Init();

	LED_Start(ORG_LED, FAST, HALF);
	SIM_Startup_Seq();
	while(SIM_Init() != HAL_OK);
	LED_Stop(ORG_LED);

	RTC_Init();

	HAL_UARTEx_ReceiveToIdle_DMA(SIM_UART, sim_rx_buffer, SIM_RXBUFFER_SIZE);
	LED_Start(GRN_LED, MEDIUM, HALF);
	sys.SIM_Connection_Status = HAL_GetTick();
	sys.Log_Request = 1;
	sys.Low_th = 0;
	sys.High_th = 4096;
}

/*-----INIZiALIZZAZIONE MEMORIE-----*/
void FatFS_Init(void)
{
	FRESULT fRes = 0;
	MKFS_PARM mkfs_opt = {0};

	do
	{
		sys.RAM_Mounted = 0;
		
		mkfs_opt.fmt = FM_FAT;
		mkfs_opt.au_size = 1024;
		mkfs_opt.n_fat = 1;
		mkfs_opt.align = 1;

		fRes = f_mkfs("/ram", &mkfs_opt, psram_fs.win, sizeof(psram_fs.win));
		if (fRes != FR_OK)
		{
			break;
		}

		fRes = f_mount(&psram_fs, "/ram", 1);

		if (fRes != FR_OK)
		{
			break;
		}

		sys.RAM_Mounted = 1;

		break;
	} while (1);

	do
	{
		sys.FLASH_Mounted = 0;
		fRes = f_mount(&flash_fs, "/flash", 1);

		if (fRes == FR_NO_FILESYSTEM)
		{
			memset((void *)&mkfs_opt, 0, sizeof(mkfs_opt));
			mkfs_opt.fmt = FM_FAT;
			mkfs_opt.au_size = 4096;    
			mkfs_opt.n_fat = 1;
			mkfs_opt.align = 1;

			fRes = f_mkfs("/flash", &mkfs_opt, flash_fs.win, sizeof(flash_fs.win));
			if (fRes != FR_OK)
			{
				break;
			}

			fRes = f_mount(&flash_fs, "/flash", 1);
			if (fRes != FR_OK)
			{
				break;
			}
		}

		sys.FLASH_Mounted = 1;

		break;
	} while (1);


}

/*-----INIZiALIZZAZIONE ACCELEROMETRO-----*/
int Acc_Init(stmdev_ctx_t* acc, uint16_t fs)
{
	lsm6dsv16x_reset_t rst;
	lsm6dsv16x_pin_int_route_t pin_int = {0};
	uint8_t acc_whoamI = 0;
	uint8_t wmi_cnt = 0;

	pin_int.fifo_th = PROPERTY_ENABLE;


	lsm6dsv16x_device_id_get(acc, &acc_whoamI);
	if (acc_whoamI != LSM6DSV16X_ID)
		while (acc_whoamI != LSM6DSV16X_ID)
		{
			lsm6dsv16x_device_id_get(acc, &acc_whoamI);
			wmi_cnt++;
			if (wmi_cnt == 3)
			{
				sys.ACC_Present = 0;
				flags.ACC_Complete = 1;
				return 0;
			}
		}
	sys.ACC_Present = 1;
	lsm6dsv16x_reset_set(acc, LSM6DSV16X_GLOBAL_RST);
	do {
		lsm6dsv16x_reset_get(acc, &rst);
		HAL_Delay(10);
	} while (rst != LSM6DSV16X_READY);

	lsm6dsv16x_block_data_update_set(acc, PROPERTY_ENABLE);
	lsm6dsv16x_ui_i2c_i3c_mode_set(acc, LSM6DSV16X_I2C_I3C_DISABLE);
	lsm6dsv16x_xl_mode_set(acc, LSM6DSV16X_XL_HIGH_PERFORMANCE_MD);
	lsm6dsv16x_gy_mode_set(acc, LSM6DSV16X_GY_HIGH_PERFORMANCE_MD);
	if(fs == 1600)
	{
		lsm6dsv16x_fifo_xl_batch_set(acc, LSM6DSV16X_XL_BATCHED_AT_1920Hz);
	}
	else if(fs == 800)
	{
		lsm6dsv16x_fifo_xl_batch_set(acc, LSM6DSV16X_XL_BATCHED_AT_960Hz);
	}
	else
	{
		return -1;
	}
	lsm6dsv16x_fifo_gy_batch_set(acc, LSM6DSV16X_GY_NOT_BATCHED);
	lsm6dsv16x_fifo_mode_set(acc, LSM6DSV16X_BYPASS_MODE);
	lsm6dsv16x_xl_data_rate_set(acc, LSM6DSV16X_ODR_OFF);
	lsm6dsv16x_gy_data_rate_set(acc, LSM6DSV16X_ODR_OFF);
	if(fs == 1600)
	{
		lsm6dsv16x_odr_trig_cfg_set(acc, 32);  //800SPS
	}
	else if(fs == 800)
	{
		lsm6dsv16x_odr_trig_cfg_set(acc, 16);  //800SPS
	}
	else
	{
		return -1;
	}
	lsm6dsv16x_xl_mode_set(acc, LSM6DSV16X_XL_ODR_TRIGGERED_MD);
	lsm6dsv16x_gy_mode_set(acc, LSM6DSV16X_GY_ODR_TRIGGERED_MD);
	lsm6dsv16x_den_polarity_set(acc, LSM6DSV16X_DEN_ACT_HIGH);
	lsm6dsv16x_xl_data_rate_set(acc, LSM6DSV16X_ODR_AT_960Hz);
	lsm6dsv16x_xl_full_scale_set(acc, LSM6DSV16X_2g);
	lsm6dsv16x_gy_full_scale_set(acc, LSM6DSV16X_2000dps);
	lsm6dsv16x_fifo_watermark_set(acc, ACC_FIFO_WATERMARK);
	lsm6dsv16x_pin_int1_route_set(acc, &pin_int);


	__HAL_GPIO_EXTI_CLEAR_IT(ACC_INTERRUPT);
	return 0;
}

/*-----INIZiALIZZAZIONE CONFIGURAZIONE-----*/
void Config_Init(void)
{
    FIL config_file;
    UINT bytes_read;
    UINT bytes_written;

	f_unlink(CONFIG_FILE); //DA RIMUOVERE DOPO I TEST
    if (f_open(&config_file, CONFIG_FILE, FA_READ) == FR_OK) 
	{
        if (f_read(&config_file, &config, sizeof(config), &bytes_read) == FR_OK && bytes_read == sizeof(config))
		{
			f_close(&config_file);
			return;
        }
        f_close(&config_file);
    }

    config.device_id = 1;
	config.samp_freq = 800;
	config.buffering_secs = 10;
	config.connection_timeout_ms = 60000;
	config.log_period_ms = 10000;
	config.hammer_th = 4096;
    for(int i = 0; i < 24; i++) 
	{
        config.low_th[i] = 0;
        config.high_th[i] = 4096;
    }
    strcpy(config.tcp_IPaddress, "esdplab.unipa.it");
    strcpy(config.tcp_Port, "21001");

    if (f_open(&config_file, CONFIG_FILE, FA_WRITE | FA_CREATE_ALWAYS) != FR_OK)
    {
        return;
    }

    if (f_write(&config_file, &config, sizeof(Config_Typedef), &bytes_written) != FR_OK || bytes_written != sizeof(Config_Typedef)) 
	{
        f_close(&config_file);
        return;
    }
    
    f_sync(&config_file);
    f_close(&config_file);
}
