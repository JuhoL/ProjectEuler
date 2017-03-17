# Project Euler Problem 23: "Non-abundant sums"
# 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
# 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import *

def IsAbundant(number):
	isAbundant = False
	if GetSumOfDivisors(number) > number:
		isAbundant = True
	return isAbundant

upperLimit = 28123
abundantNumbers = []

# The smallest abundant is 12, so the greatest useful abundant value in this case is 28123 - 12 = 28111isSumOfAbundants = [False]*upperLimit
isAbundant = [False]*(upperLimit - 12)

for i in range (12, (upperLimit - 12)):
	if isAbundant[i] == False:
		if IsAbundant(i):
			# All multiples are also abundants, so let's mark them off.
			for k in range(i, (upperLimit - 12), i):
				if isAbundant[k] == False:
					isAbundant[k] = True
					abundantNumbers.append(k)

isSumOfAbundants = [False]*upperLimit
for i in range(0, len(isAbundant)):
	for k in range(i, len(abundantNumbers)):
		sumOfTwoAbundants = abundantNumbers[i] + abundantNumbers[k]
		if sumOfTwoAbundants < len(isSumOfAbundants):
			isSumOfAbundants[sumOfTwoAbundants] = True

finalSum = 0
for i in range(1, upperLimit):
	if isSumOfAbundants[i] == False:
		finalSum += i

print ("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is " + str(finalSum))