/*
 * battery_charger.h
 *
 *  Created on: Sep 17, 2024
 *      Author: albve
 */

#ifndef INC_BATTERY_CHARGER_H_
#define INC_BATTERY_CHARGER_H_

#include "main.h"

//DEVICE ADDRESS
#define BATTERY_CHARGER_ADDR                    (0x6B)

//REGISTER ADDESSES
#define REG00_MINIMAL_SYSTEM_VOLTAGE            (0x00)
#define REG01_CHARGE_VOLTAGE_LIMIT              (0x01)
#define REG03_CHARGE_CURRENT_LIMIT              (0x03)
#define REG05_INPUT_VOLTAGE_LIMIT               (0x05)
#define REG06_INPUT_CURRENT_LIMIT               (0x06)
#define REG08_PRECHARGE_CONTROL                 (0x08)
#define REG09_TERMINATION_CONTROL               (0x09)
#define REG0A_RECHARGE_CONTROL                  (0x0A)
#define REG0B_VOTG_REGULATION                   (0x0B)
#define REG0D_IOTG_REGULATION                   (0x0D)
#define REG0E_TIMER_CONTROL                     (0x0E)
#define REG0F_CHARGER_CONTROL_0                 (0x0F)
#define REG10_CHARGER_CONTROL_1                 (0x10)
#define REG11_CHARGER_CONTROL_2                 (0x11)
#define REG12_CHARGER_CONTROL_3                 (0x12)
#define REG13_CHARGER_CONTROL_4                 (0x13)
#define REG14_CHARGER_CONTROL_5                 (0x14)
#define REG15_MPPT_CONTROL                      (0x15)
#define REG16_TEMPERATURE_CONTROL               (0x16)
#define REG17_NTC_CONTROL_0                     (0x17)
#define REG18_NTC_CONTROL_1                     (0x18)
#define REG19_ICO_CURRENT_LIMIT                 (0x19)
#define REG1B_CHARGER_STATUS_0                  (0x1B)
#define REG1C_CHARGER_STATUS_1                  (0x1C)
#define REG1D_CHARGER_STATUS_2                  (0x1D)
#define REG1E_CHARGER_STATUS_3                  (0x1E)
#define REG1F_CHARGER_STATUS_4                  (0x1F)
#define REG20_FAULT_STATUS_0                    (0x20)
#define REG21_FAULT_STATUS_1                    (0x21)
#define REG22_CHARGER_FLAG_0                    (0x22)
#define REG23_CHARGER_FLAG_1                    (0x23)
#define REG24_CHARGER_FLAG_2                    (0x24)
#define REG25_CHARGER_FLAG_3                    (0x25)
#define REG26_FAULT_FLAG_0                      (0x26)
#define REG27_FAULT_FLAG_1                      (0x27)
#define REG28_CHARGER_MASK_0                    (0x28)
#define REG29_CHARGER_MASK_1                    (0x29)
#define REG2A_CHARGER_MASK_2                    (0x2A)
#define REG2B_CHARGER_MASK_3                    (0x2B)
#define REG2C_FAULT_MASK_0                      (0x2C)
#define REG2D_FAULT_MASK_1                      (0x2D)
#define REG2E_ADC_CONTROL                       (0x2E)
#define REG2F_ADC_FUNCTION_DISABLE_0            (0x2F)
#define REG30_ADC_FUNCTION_DISABLE_1            (0x30)
#define REG31_IBUS_ADC                          (0x31)
#define REG33_IBAT_ADC                          (0x33)
#define REG35_VBUS_ADC                          (0x35)
#define REG37_VAC1_ADC                          (0x37)
#define REG39_VAC2_ADC                          (0x39)
#define REG3B_VBAT_ADC                          (0x3B)
#define REG3D_VSYS_ADC                          (0x3D)
#define REG3F_TS_ADC                            (0x3F)
#define REG41_TDIE_ADC                          (0x41)
#define REG43_Dp_ADC                            (0x43)
#define REG45_Dm_ADC                            (0x45)
#define REG47_DPDM_DRIVER                       (0x47)
#define REG48_PART_INFORMATION                  (0x48)


#define POOR_SOURCE_MASK                        (0x0000100000000000)
#define VAC2_CHANGE_MASK                        (0x0000040000000000)
#define VAC1_CHANGE_MASK                        (0x0000020000000000)
#define VAC2_PRESENT_MASK                       (0x02)
#define VAC1_PRESENT_MASK                       (0x01)


void BC_Init(void);
int BC_Write_Reg(uint8_t reg, uint8_t wdata);
int BC_Read_Reg(uint8_t reg, uint8_t *rdata);
int BC_MultiWrite_Reg(uint8_t reg, uint16_t wdata);
int BC_MultiRead_Reg(uint8_t reg, uint16_t *rdata);
int BC_Read_Flags(uint64_t *flags);
void BC_Manage_Interrupts(uint64_t flags);

#endif /* INC_BATTERY_CHARGER_H_ */
