# Project Euler Problem 9: "Special Pythagorean triplet"
# 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys
sys.path.insert(0, './Utils')
import benchmark
from math import *

totalSum = 1000
start = 997
end = 1
a = 0
b = 0
product = 0
tripletFound = False

for c in range(start, end, -1):
	remainder = totalSum - c
	a = 1
	while 1:
		b = remainder - a
		cCalc = sqrt(a**2 + b**2)
		if cCalc == c:
			tripletFound = True
			product = a*b*c
			break
		a += 1
		if a >= b:
			break
	if tripletFound == True:
		break

print ("The product of the triplet " + str(a) + "^2 + " + str(b) + "^2 = " + str(c) + " is " + str(product))