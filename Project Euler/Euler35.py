# Project Euler Problem 35: "Circular primes"
# 
# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *

if len(sys.argv) < 2:
	print ("Give upper limit as an argument.")
else:
	upperLimit = int(sys.argv[1])

	primeList = GeneratePrimeListBelowValueWithSieve(upperLimit)

	circularPrimes = 0
	for i in range(0, len(primeList)):
		numberString = str(primeList[i])
		
		isCircular = True
		for j in range(0, len(numberString)):
			isCircular = CheckIfPrime(int(numberString), primeList)
			if isCircular == False:
				break
			numberString = numberString[1::1] + numberString[0]
		if isCircular == True:
			circularPrimes += 1

	print ("There are " + str(circularPrimes) + " circular primes below " + str(upperLimit))