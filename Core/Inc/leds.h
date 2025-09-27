/*
 * leds.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_LEDS_H_
#define INC_LEDS_H_


#define ON 1
#define FAST 2
#define SLOW 3

void LED_Start(uint32_t LED, uint32_t freq_hz, uint8_t mode);
void LED_Stop(uint32_t LED);
#endif /* INC_LEDS_H_ */
