#ifndef _TYPES_H_
#define _TYPES_H_

typedef signed char int8;
typedef signed short int16; 
typedef signed int int32;
typedef signed long long int int64;

typedef unsigned char uint8;
typedef unsigned short uint16;
typedef unsigned int uint32;
typedef unsigned long long int uint64;

#define WORD_SIZE 32
#define NRESULT 10

#ifndef UINT_MAX
/** O maior número que cabe em um inteiro unsigned. */
#define UINT_MAX 0xffffffff
#endif


#endif

