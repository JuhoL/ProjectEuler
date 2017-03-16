// Project Euler Problem 15: "Lattice paths"
// 
// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
// there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

//--------------------------------
// Defines and macros
//--------------------------------

#define TRUE 					(1==1)
#define FALSE 					(1==0)
#define BIT(_b)					(1ULL << (_b))

#define DEBUG_ENABLED			FALSE

#if (DEBUG_ENABLED == TRUE)
	#define DEBUG_VALIDATE()	{v_BitStructDebug(at_bits, u8_gridDimension, VALIDATE_BIT_FIELD);}
	#define DEBUG_PRINT()		{v_BitStructDebug(at_bits, u8_gridDimension, PRINT_POSITIONS);}
	#define DEBUG_PRINT_BF()	{v_BitStructDebug(at_bits, u8_gridDimension, PRINT_BIT_FIELD);}
#else
	#define DEBUG_VALIDATE()
	#define DEBUG_PRINT()
	#define DEBUG_PRINT_BF()
#endif

//--------------------------------
// Structs and enums
//--------------------------------

typedef struct
{
	uint8_t u8_minPosition;
	uint8_t u8_maxPosition;
	uint8_t u8_currentPosition;
} bit_struct;

#if (DEBUG_ENABLED == TRUE)
typedef enum
{
	VALIDATE_BIT_FIELD = 0,
	PRINT_POSITIONS,
	PRINT_BIT_FIELD
} validation_enum;
#endif

//--------------------------------
// Static functio nprototypes
//--------------------------------

static void v_BitStructInit(bit_struct at_bitStruct[], uint8_t u8_gridDimension);
static uint8_t b_BitStructShiftRight(bit_struct at_bitStruct[], uint8_t u8_bit);
static void v_BitStructReturnBits(bit_struct at_bitStruct[], uint8_t u8_lastToReturn);

#if (DEBUG_ENABLED == TRUE)
static void v_BitStructDebug(bit_struct at_bitStruct[], uint32_t u32_bits, validation_enum e_type);
#endif

//--------------------------------
// Main
//--------------------------------

int main( int argc, char *argv[] )
{
	uint64_t u64_bitField;
	uint8_t u8_gridDimension;
	uint32_t u32_routes = 0;
	uint8_t b_debugEnabled;

	if (argc >= 2)
	{
		uint32_t u32_argument = strtoul(argv[1], 0, 10);
		if (u32_argument > 32)
		{
			printf("Too large grid! Maximum is 32...\r\n");
			return -1;
		}
		u8_gridDimension = (uint8_t)u32_argument;
		printf("Calculating routes for %ux%u grid.\r\n", u8_gridDimension, u8_gridDimension);

#if (DEBUG_ENABLED == TRUE)
		printf("Debug prints enabled.\r\n");
#endif
	}
	else
	{
		printf("Give the grid dimension as an argument...");
		return -1;
	}

	// Now we are trying to be clever. We'll solve this in binary. Let 0 be "move down" and 1 be "move left".
	// This way we know that every valid route must have exactly the number of grid dimensions of ones and zeroes.
	// E.g. on 2x2 grid all valid routes are four-bit values that have two zeroes and two ones in any order.
	// With this information we can calculate valid routes on any arbitrary grid!

	// Instead of going through number-by-number, we shall only move bits around in a bit-field,
	// so that every binary bit field we handle will be valid.
	bit_struct at_bits[u8_gridDimension];

	v_BitStructInit(at_bits, u8_gridDimension);
	DEBUG_PRINT();

	while (TRUE)
	{
		uint8_t u8_bit = 0;
		do
		{
			u32_routes++;
			DEBUG_PRINT_BF();
		} while (b_BitStructShiftRight(at_bits, u8_bit)); // Shift the LSB to the end.
		
		do
		{
			u8_bit++;
		} while ((u8_bit < u8_gridDimension) && (b_BitStructShiftRight(at_bits, u8_bit) == FALSE)); // Find a next bit to move.

		if (u8_bit < u8_gridDimension)
		{
			v_BitStructReturnBits(at_bits, u8_bit);
		}
		else
		{
			break;
		}
	}

	printf("\r\nRoutes for %ux%u grid is %u", u8_gridDimension, u8_gridDimension, u32_routes);

	return 0;
}

//--------------------------------
// Static functions
//--------------------------------

// Initialises given bit structure.
static void v_BitStructInit(bit_struct at_bitStruct[], uint8_t u8_gridDimension)
{
	for (uint8_t i = 0; i < u8_gridDimension; i++)
	{
		at_bitStruct[i].u8_minPosition = i;
		at_bitStruct[i].u8_maxPosition = i + u8_gridDimension;
		at_bitStruct[i].u8_currentPosition = at_bitStruct[i].u8_maxPosition;
	}
	return;
}

// Shifts given bit to the right. If the bit cannot be shifted, return false, otherwise return true.
static uint8_t b_BitStructShiftRight(bit_struct at_bitStruct[], uint8_t u8_bit)
{
	uint8_t b_success;

	if (at_bitStruct[u8_bit].u8_currentPosition <= at_bitStruct[u8_bit].u8_minPosition)
	{
		// Out of range.
		b_success = FALSE;
	}
	else
	{
		b_success = TRUE;
		at_bitStruct[u8_bit].u8_currentPosition--;
	}

	return b_success;
}

// Returns the bits up to given index to the highest possible position they can have.
static void v_BitStructReturnBits(bit_struct at_bitStruct[], uint8_t u8_lastToReturn)
{
	while (u8_lastToReturn-- > 0)
	{
		at_bitStruct[u8_lastToReturn].u8_currentPosition = at_bitStruct[u8_lastToReturn + 1].u8_currentPosition - 1;
	}
	return;
}

#if (DEBUG_ENABLED == TRUE)
static void v_BitStructDebug(bit_struct at_bitStruct[], uint32_t u32_bits, validation_enum e_type)
{
	uint64_t u64_bitField;

	switch (e_type)
	{
		case VALIDATE_BIT_FIELD:
			for (uint32_t i = 0; i < u32_bits; i++)
			{
				for (uint32_t k = i + 1; k < u32_bits; k++)
				{
					if (at_bitStruct[i].u8_currentPosition == at_bitStruct[k].u8_currentPosition)
					{
						printf("Bit overlap! Should not happen, you douche!");
						printf("Overlapping bits are %u and %u in position %u", i, k, at_bitStruct[i].u8_currentPosition);
					}
				}
			}
			break;

		case PRINT_POSITIONS:
			u64_bitField = 0;

			printf("| Bit\t| Position\r\n");
			for (uint32_t i = 0; i < u32_bits; i++)
			{
				printf("| %u\t| %u\r\n", i, at_bitStruct[i].u8_currentPosition);
				u64_bitField |= BIT(at_bitStruct[i].u8_currentPosition);
			}

			printf("\r\nResulting bit field: ");
			for (uint32_t i = 0; i < (u32_bits*2); i++)
			{
				if ((u64_bitField & BIT(i)) == 0)
				{
					putchar('0');
				}
				else
				{
					putchar('1');
				}
			}
			putchar('\r');
			break;

		case PRINT_BIT_FIELD:
			u64_bitField = 0;

			for (uint32_t i = 0; i < u32_bits; i++)
			{
				u64_bitField |= BIT(at_bitStruct[i].u8_currentPosition);
			}

			printf("\r\nBit field: ");
			for (uint32_t i = 0; i < (u32_bits*2); i++)
			{
				if ((u64_bitField & BIT(i)) == 0)
				{
					putchar('0');
				}
				else
				{
					putchar('1');
				}
			}
			putchar('\r');
			break;

		default:
			// Do nothing.
			break;
	}
	return;
}
#endif