# Project Euler Problem 34: "Digit factorials"
# 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import benchmark
from Utils import GetFactorial

sumsOfFactorials = []
for n in range (10, 100000):
	numberString = str(n)

	# Only !0 and !1 are odd. This means that even numbers may contain only even
	# number of 0's and 1's.
	oddFactorials = 0
	for i in range (0, len(numberString)):
		if int(numberString[i]) < 2:
			oddFactorials += 1

	if (n % 2 == 0 and oddFactorials % 2 == 0) or (n % 2 > 0 and oddFactorials % 2 > 0):
		sumOfFactorials = 0
		for i in range (0, len(numberString)):
			sumOfFactorials += GetFactorial(int(numberString[i]))
		if sumOfFactorials == n:
			sumsOfFactorials.append(n)

print ("The sum of numbers are " + str(sum(sumsOfFactorials)))