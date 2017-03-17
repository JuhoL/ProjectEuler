# Project Euler Problem 27: "Quadratic primes"
# 
# Euler discovered the remarkable quadratic formula:
# 
# n^2 + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
# However, when n=40, it is divisible by 41, and certainly when n=41 it is clearly divisible by 41.
# 
# The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive
# values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# 
# n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
# 
# where |n| is the modulus/absolute value of n, e.g. |11|=11 and |−4|=4
# 
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
# number of primes for consecutive values of n, starting with n=0.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *

def CheckConsecutivePrimes(a, b, primeList):
	n = 0
	isPrime = True
	while isPrime:
		number = n**2 + a*n + b
		isPrime = CheckIfPrime(number, primeList)
		n += 1
	n -= 1 # Remove one extra n increment.
	return n

# a and b must be primes.
primeList = GeneratePrimeListBelowValueWithSieve(1000)

mostConsecutive = [0, 0, 0]
countIndex = 0
aIndex = 1
bIndex = 2

for i in range(0, len(primeList)):
	for k in range(0, len(primeList)):
		for a in [-primeList[i],primeList[i]]:
			for b in [-primeList[k],primeList[k]]:
				consecutivePrimes = CheckConsecutivePrimes(a, b, primeList)
				if consecutivePrimes > mostConsecutive[countIndex]:
					mostConsecutive[countIndex] = consecutivePrimes
					mostConsecutive[aIndex] = a
					mostConsecutive[bIndex] = b

print ("a = " + str(mostConsecutive[aIndex]))
print ("b = " + str(mostConsecutive[bIndex]))
print (str(mostConsecutive[countIndex]) + " consecutive primes.")
finalProduct = mostConsecutive[aIndex] * mostConsecutive[bIndex]

print ("The prdouct is " + str(finalProduct))