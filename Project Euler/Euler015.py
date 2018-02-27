# Project Euler Problem 15: "Lattice paths"
# 
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?

import sys
sys.path.insert(0, './Utils')
import benchmark

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

# On the cubersome and ridiculously slow bit-shift approach on the C solution,
# it is easy to see how foolish I have been. This is a simple series of triangular numbers!
# This becomes obvious when you print the bit fields and look for patterns.
# Let's crush this with a healty dose of recursion.
#
# Afterthough: I take my words back! This is actually way slower than the C implementation.
# The C version crushed 14x14 grid in a second. This takes 13 seconds. Probably something
# to do with my crappy Python skills.

gridDimension = 20

print ("Calculating routes for " + str(gridDimension) + "x" + str(gridDimension) + " grid.")
routes = CalculateRoutes(gridDimension + 1, gridDimension - 2)

print (str(routes) + " routes found.")