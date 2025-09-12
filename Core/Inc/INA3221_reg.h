/*
 * INA3321_reg.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_INA3221_REG_H_
#define INC_INA3221_REG_H_

#include <stdint.h>

#define INA3221_ADDR_0  (0x40)      ///< A0 to GND
#define INA3221_ADDR_1  (0x41)      ///< A0 to Vs+
#define INA3221_ADDR_2  (0x42)      ///< A0 to SDA
#define INA3221_ADDR_3  (0x43)      ///< A0 to SCL

#define INA3221_BUS_NUMBER 3  ///< Number of shunt available

#define INA3221_REG_CONFIG                      (0x00)
#define INA3221_REG_SHUNTVOLTAGE_1              (0x01)
#define INA3221_REG_SHUNTVOLTAGE_2              (0x03)
#define INA3221_REG_SHUNTVOLTAGE_3              (0x05)
#define INA3221_REG_BUSVOLTAGE_1                (0x02)
#define INA3221_REG_BUSVOLTAGE_2                (0x04)
#define INA3221_REG_BUSVOLTAGE_3                (0x06)



#define INA3221_REG_CRITICAL_ALERT_1            (0x07)
#define INA3221_REG_WARNING_ALERT_1             (0x08)
#define INA3221_REG_SHUNT_VOLTAGE_SUM           (0x0D)
#define INA3221_REG_SHUNT_VOLTAGE_SUM_LIMIT     (0x0E)
#define INA3221_REG_MASK                        (0x0F)
#define INA3221_REG_VALID_POWER_UPPER_LIMIT     (0x10)
#define INA3221_REG_VALID_POWER_LOWER_LIMIT     (0x11)


#define INA3221_REG_MID                      	(0xFE)
#define INA3221_REG_DID                      	(0xFF)


/**
 *  Default register after reset
 */
#define INA3221_DEFAULT_CONFIG                   (0x7127)
#define INA3221_DEFAULT_MASK                     (0x0002)
#define INA3221_DEFAULT_POWER_UPPER_LIMIT        (0x2710) //10V
#define INA3221_DEFAULT_POWER_LOWER_LIMIT        (0x2328) //9V

#define INA3221_DEFAULT_MID                   	(0x5449)
#define INA3221_DEFAULT_DID                   	(0x3220)

#define INA3221_MASK_CONFIG (0x7C00)

/**
 * Number of samples
 */
typedef enum {
	INA3221_AVG_1 = 0,  ///< Default
	INA3221_AVG_4,
	INA3221_AVG_16,
	INA3221_AVG_64,
	INA3221_AVG_128,
	INA3221_AVG_256,
	INA3221_AVG_512,
	INA3221_AVG_1024,
} ina3221_avg_t;

/**
 * Channel selection list
 */
typedef enum {
    CHANNEL_1 = 0,
    CHANNEL_2,
    CHANNEL_3,
} ina3221_channel_t;

/**
 * Conversion time in us
 */
typedef enum {
	INA3221_CT_140 = 0,
	INA3221_CT_204,
	INA3221_CT_332,
	INA3221_CT_588,
	INA3221_CT_1100,  ///< Default
	INA3221_CT_2116,
	INA3221_CT_4156,
	INA3221_CT_8244,
} ina3221_ct_t;

/**
 * Config description register
 */
typedef union
{
    struct {
        uint16_t esht : 1; ///< Enable/Disable shunt measure    // LSB
        uint16_t ebus : 1; ///< Enable/Disable bus measure
        uint16_t mode : 1; ///< Single shot measure or continious mode
        uint16_t vsht : 3; ///< Shunt voltage conversion time
        uint16_t vbus : 3; ///< Bus voltage conversion time
        uint16_t avg  : 3; ///< number of sample collected and averaged together
        uint16_t ch3  : 1; ///< Enable/Disable channel 3
        uint16_t ch2  : 1; ///< Enable/Disable channel 2
        uint16_t ch1  : 1; ///< Enable/Disable channel 1
        uint16_t rst  : 1; ///< Set this bit to 1 to reset device  // MSB
    };
    uint16_t config_register;
} ina3221_config_t;


/**
 * Mask/enable description register
 */
typedef union
{
    struct {
        uint16_t cvrf : 1; ///< Conversion ready flag (1: ready)   // LSB
        uint16_t tcf  : 1; ///< Timing control flag
        uint16_t pvf  : 1; ///< Power valid flag
        uint16_t wf   : 3; ///< Warning alert flag (Read mask to clear) (order : Channel1:channel2:channel3)
        uint16_t sf   : 1; ///< Sum alert flag (Read mask to clear)
        uint16_t cf   : 3; ///< Critical alert flag (Read mask to clear) (order : Channel1:channel2:channel3)
        uint16_t cen  : 1; ///< Critical alert latch (1:enable)
        uint16_t wen  : 1; ///< Warning alert latch (1:enable)
        uint16_t scc3 : 1; ///< channel 3 sum (1:enable)
        uint16_t scc2 : 1; ///< channel 2 sum (1:enable)
        uint16_t scc1 : 1; ///< channel 1 sum (1:enable)
        uint16_t      : 1; ///< Reserved         //MSB
    };
    uint16_t mask_register;
} ina3221_mask_t;

/**
 *  Device description
 */
typedef struct {
    const uint16_t shunt[INA3221_BUS_NUMBER]; ///< Memory of shunt value (mOhm)
    ina3221_config_t config;                  ///< Memory of ina3221 config
    ina3221_mask_t mask;                      ///< Memory of mask_config
} ina3221_t;

#endif /* INC_INA3221_REG_H_ */
