# Project Euler Problem 45: "Triangular, pentagonal, and hexagonal"
# 
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# 
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# 
# Find the next triangle number that is also pentagonal and hexagonal.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import *

def CheckNumber(order):
	number = CalculateTriangular(order)
	isMatch = CheckIfPentagonal(number)
	if isMatch == True:
		isMatch = CheckIfHexagonal(number)
	return isMatch

i = 286
while CheckNumber(i) == False:
	i += 1
triangle = CalculateTriangular(i)
print ("The next triangle number is T" + str(i) + " = " + str(triangle))