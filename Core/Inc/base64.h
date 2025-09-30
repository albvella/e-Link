/*
 * base64.h
 *
 *  Created on: Sep 30, 2025
 *      Author: albve
 */

#ifndef INC_BASE64_H_
#define INC_BASE64_H_

#include "main.h"
#include "stdint.h"
#include "stddef.h"

size_t Base64_Decode(const char *in, uint8_t *out, size_t out_len);
size_t Base64_Encode(const uint8_t *in, size_t in_len, char *out, size_t out_size);

#endif /* INC_BASE64_H_ */
