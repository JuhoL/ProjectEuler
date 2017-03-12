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

//--------------------------------
// Structs and enums
//--------------------------------


//--------------------------------
// Static function prototypes
//--------------------------------

static uint32_t u32_GetTriangular(uint8_t u8_order);
static uint32_t u32_CalculateRoutes(uint8_t u8_gridDimension, uint8_t u8_recursion);

//--------------------------------
// Main
//--------------------------------

int main( int argc, char *argv[] )
{
	uint8_t u8_gridDimension;
	uint32_t u32_routes = 0;

	if (argc >= 2)
	{
		uint32_t u32_argument = strtoul(argv[1], 0, 10);
		if (u32_argument > 32)
		{
			printf("Too large grid! Maximum is 32...\r\n");
			return -1;
		}
		u8_gridDimension = (uint8_t)u32_argument;
		if (u8_gridDimension > 2)
		{
			printf("Calculating routes for %ux%u grid.\r\n", u8_gridDimension, u8_gridDimension);
		}
		else
		{
			printf("The grid dimension must be at least 3x3...");
		}
	}
	else
	{
		printf("Give the grid dimension as an argument...");
		return -1;
	}

	// Let's try the recursive algorithm that failed in Python in C.
	u32_routes = u32_CalculateRoutes(u8_gridDimension + 1, u8_gridDimension - 2);

	printf("\r\nRoutes for %ux%u grid is %lu", u8_gridDimension, u8_gridDimension, u32_routes);

	return 0;
}

//--------------------------------
// Static functions
//--------------------------------

static uint32_t u32_GetTriangular(uint8_t u8_order)
{
	uint32_t u32_triangular = 0;
	for (uint8_t i = 1; i <= u8_order; i++)
	{
		u32_triangular += i;
	}
	return u32_triangular;
}

static uint32_t u32_CalculateRoutes(uint8_t u8_gridDimension, uint8_t u8_recursion)
{
	uint32_t u32_totalRoutes = 0;
	uint8_t u8_cycleStart = u8_gridDimension;
	for (uint8_t i = u8_cycleStart; i > 0; i--)
	{
		if (u8_recursion > 1)
		{
			u32_totalRoutes += u32_CalculateRoutes(i, u8_recursion - 1);
		}
		else
		{
			u32_totalRoutes += u32_GetTriangular(i);
		}
	}
	return u32_totalRoutes;
}