# Project Euler Problem 10: "Summation of primes"
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import GetSumOfPrimesBelowValue

value = 2000000

sumOfPrimes = GetSumOfPrimesBelowValue(value)

print ("Sum of primes below " + str(value) + " is " + str(sumOfPrimes))