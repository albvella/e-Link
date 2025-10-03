/*
 * leds.h
 *
 *  Created on: Sep 13, 2024
 *      Author: albve
 */

#ifndef INC_LEDS_H_
#define INC_LEDS_H_

//Frequenza
#define FAST     0
#define MEDIUM   1
#define SLOW     2
#define VERY_SLOW 3

//Duty Cycle
#define FULL     4
#define HIGH     5
#define HALF     6
#define LOW      7

void LED_Init(void);
void LED_Start(uint32_t LED, uint8_t freq, uint8_t duty);
void LED_Stop(uint32_t LED);
#endif /* INC_LEDS_H_ */
