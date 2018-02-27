# Project Euler Problem 47: "Distinct primes factors"
# 
# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 x 7
# 15 = 3 x 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 
# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
# 
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import GetDistinctFactors

n = 648
distinctFactors = 4

numberFound = False
while numberFound == False:
	numberFound = True
	for i in range(0, distinctFactors):
		factors = GetDistinctFactors(n + i)
		if len(factors) != distinctFactors:
			n += 1 + i
			numberFound = False
			break

print ("The first number is " + str(n))