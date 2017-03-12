# Project Euler Problem 21: "Amicable numbers"
# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

import benchmark
import sys
from Utils import *

if len(sys.argv) < 2:
	print ("Give max limit as an argument.")
else:
	#Code start
	valueMax = int(sys.argv[1])

	# Let's use the sieve method from prime searches.
	# 0 means unchecked, 1 means amicable and -1 means nonamicable
	sieve = [0]*valueMax

	for i in range (2, valueMax):
		if sieve[i] == 0:
			sum1 = GetSumOfDivisors(i)
			if sum1 != i:
				if GetSumOfDivisors(sum1) == i:
					sieve[i] = 1
					if sum1 < valueMax:
						sieve[sum1] = 1
					print ("Pair found: " + str(i) + " -> " + str(sum1))
				else:
					sieve[i] = -1
			else:
				sieve[i] = -1

	sumOfAmicableNumbers = 0
	for i in range (1, valueMax):
		if sieve[i] > 0:
			sumOfAmicableNumbers += i

	print ("The sum of all amicable numbers under " + str(valueMax) + " is " + str(sumOfAmicableNumbers))