# Project Euler Problem 10: "Summation of primes"
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import benchmark
import sys
from Primes import *

if len(sys.argv) < 2:
	print ("Give the grid dimension as an argument.")
else:
	value = int(sys.argv[1])

	primeList = GeneratePrimeListBelowValueWithSieve(value)
	sumOfPrimes = sum(primeList)
	
	print ("Sum of primes below " + str(value) + " is " + str(sumOfPrimes))