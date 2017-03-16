# Project Euler Problem 15: "Lattice paths"
# 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

import benchmark
import sys

if len(sys.argv) < 2:
	print ("Give the grid dimension as an argument.")
else:
	# Project Euler has the capability to make you feel stupid.
	# It appears that my first notion that the valid routes can be presented in binary with exact
	# number of ones and zeros is actually the fastest solution there is. I just did not know how to
	# represent the concept mathematically. In Problem 15 overview PDF the solution is represented
	# as combinatorial product sequence PI(i=1 -> n)(n+1)/i. This solves the problem in 0.8 ms.
	# Into the shame box you go, I say to myself.

	gridDimension = int(sys.argv[1])
	if gridDimension > 2:
		print ("Calculating routes for " + str(gridDimension) + "x" + str(gridDimension) + " grid.")
		routes = 1
		for i in range (1, gridDimension + 1):
			routes = routes*(gridDimension + i)/i

		print (str(routes) + " routes found.")
	else:
		print ("The grid dimension must be at least 3x3...")