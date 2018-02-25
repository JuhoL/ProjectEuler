# Project Euler Problem 50: "Consecutive prime sum"
# 
# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime, co
# tains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *

primeValueLimit = 1000000
primeValueMinimum = primeValueLimit - primeValueLimit/10

primeList = GeneratePrimeListBelowValue(primeValueLimit)
primeSums = []
primeCounts = []
maximumCount = 0

for i in range(0, len(primeList)):
    if primeList[i] > primeValueMinimum:
        windowedPrimes = primeList[i:]
        windowLimit = i
        if windowLimit > 1000:
            windowLimit = 1000
        break

print ("There are " + str(len(primeList)) + " primes.")

for i in range(0, windowLimit):
    primeSum = 0
    count = 0
    for k in range(i, windowLimit):
        primeSum += primeList[k]
        count += 1
        if primeSum > primeValueLimit:
            break
        if primeSum > primeValueMinimum and count > maximumCount:
            if primeSum in windowedPrimes:
                maximumCount = count
                primeSums.append(primeSum)
                primeCounts.append(count)

print ("Search complete.")

maximumIndex = primeCounts.index(maximumCount)
maximumPrime = primeSums[maximumIndex]

print ("Biggest prime is " + str(maximumPrime) + " with " + str(maximumCount) + " consecutive primes.")
