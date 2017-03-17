# Project Euler Problem 37: "Truncatable primes"
# 
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove
# digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work
# from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *

def CheckTruncatability(numberString, primeList, backwards = False):
	isPrime = True
	for k in range(1, len(numberString)):
		if backwards == False:
			number = int(numberString[k::])
		else:
			number = int(numberString[:k:])
		isPrime = CheckIfPrime(number, primeList)
		if isPrime == False:
			break
	return isPrime

truncatablePrimes = []
primeList = GeneratePrimeListBelowValueWithSieve(10000)

i = 4 # Skip 2, 3, 5 and 7
while len(truncatablePrimes) < 11:
	prime = GetPrime(i, primeList)
	primeString = str(prime)

	isTruncatable = CheckTruncatability(primeString, primeList, False)
	if isTruncatable == True:
		isTruncatable = CheckTruncatability(primeString, primeList, True)

	if isTruncatable == True:
		print ("Prime found: " + str(prime))
		truncatablePrimes.append(prime)

	i += 1

finalSum = sum(truncatablePrimes)
print ("The sum of truncatable primes is " + str(finalSum))