# Project Euler Problem 46: "Goldbach's other conjecture"
# 
# It was proposed by Christian Goldbach that every odd composite number can be written as
# the sum of a prime and twice a square.
# 
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and
# twice a square?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *

primeList = GeneratePrimeListBelowValueWithSieve(5000)
squares = [0]

def GoldbachTest(number):
	isPass = False

	if CheckIfComposite(number):
		i = GetLargestPrimeIndex(number, primeList)

		while i >= 0:
			square = number - primeList[i]
			square >>= 1

			while square > max(squares):
				squares.append(len(squares)**2)
			if square in squares:
				isPass = True

			i -= 1
	else:
		isPass = True

	return isPass

i = 35
while GoldbachTest(i) == True:
	i += 2

print ("The smallest failing ocmposite number is " + str(i))