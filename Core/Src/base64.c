/*
 * base64.c
 *
 *  Created on: Sep 30, 2025
 *      Author: albve
 */

#include "base64.h"
#include "global_variables.h"


/*-----DECODIFICA BASE64-----*/
size_t Base64_Decode(const char *in, uint8_t *out, size_t out_len)
{
    size_t i = 0, j = 0;
    int v = 0, val = 0;
    while (in[i] && in[i] != '\n' && in[i] != '\r')
    {
        unsigned char c = base64_table[(unsigned char)in[i++]];
        if (c == 0x80) continue; // carattere non valido
        val = (val << 6) | c;
        v += 6;
        if (v >= 8)
        {
            v -= 8;
            if (j < out_len) out[j++] = (val >> v) & 0xFF;
        }
    }
    return j; // numero di byte decodificati
}

/*-----CODIFICA BASE64-----*/
size_t Base64_Encode(const uint8_t *in, size_t in_len, char *out, size_t out_size)
{
    size_t i = 0, j = 0;
    while (i < in_len && (j + 4) <= out_size)
    {
        uint32_t octet_a = i < in_len ? in[i++] : 0;
        uint32_t octet_b = i < in_len ? in[i++] : 0;
        uint32_t octet_c = i < in_len ? in[i++] : 0;
        uint32_t triple = (octet_a << 16) | (octet_b << 8) | octet_c;

        out[j++] = base64_enc_table[(triple >> 18) & 0x3F];
        out[j++] = base64_enc_table[(triple >> 12) & 0x3F];
        out[j++] = (i > in_len + 1) ? '=' : base64_enc_table[(triple >> 6) & 0x3F];
        out[j++] = (i > in_len) ? '=' : base64_enc_table[triple & 0x3F];
    }
    if (j < out_size) out[j] = '\0'; // null-terminate se vuoi una stringa
    return j; // lunghezza della stringa base64 prodotta (senza null)
}
