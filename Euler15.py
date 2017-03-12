# Project Euler Problem 15: "Lattice paths"
# 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

import benchmark
import sys

def GetTriangular(order):
	triangular = 0
	for i in range(1, order + 1):
		triangular += i
	return triangular

def CalculateRoutes(gridDimension, recursion):
	totalRoutes = 0
	cycleStart = gridDimension
	for i in range (cycleStart, 0, -1):
		if recursion > 1:
			totalRoutes += CalculateRoutes(i, recursion - 1)
		else:
			totalRoutes += GetTriangular(i)
	return totalRoutes

if len(sys.argv) < 2:
	print ("Give the grid dimension as an argument.")
else:
	# On the cubersome and ridiculously slow bit-shift approach on the C solution,
	# it is easy to see how foolish I have been. This is a simple series of triangular numbers!
	# This becomes obvious when you print the bit fields and look for patterns.
	# Let's crush this with a healty dose of recursion.
	gridDimension = int(sys.argv[1])
	print ("Calculating routes for " + str(gridDimension) + "x" + str(gridDimension) + " grid.")
	routes = CalculateRoutes(gridDimension + 1, gridDimension - 2)# gridDimension - 2)

	print (str(routes) + " routes found.")