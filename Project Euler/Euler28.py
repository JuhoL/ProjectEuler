# Project Euler Problem 28: "Number spiral diagonals"
#
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

import benchmark

dimensionMax = 1001
sumOfDiagonals = 1
index = 1
# 1x1 grid is trivial. Let's skip it.
for dimension in range(3, dimensionMax + 1, 2):
	for i in range(0, 4):
		index += (dimension - 1)
		sumOfDiagonals += index

print ("Sum of diagonals in " + str(dimensionMax) + "x" + str(dimensionMax) + " grid is " + str(sumOfDiagonals))