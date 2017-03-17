# Project Euler Problem 3: "Largest prime factor"
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import sys
sys.path.insert(0, './Utils')
import benchmark
import Primes

problemNumber = 600851475143

largestFactor = Primes.GetLargestFactorDynamic(problemNumber)
print ("The largest factor of " + str(problemNumber) + " is " + str(largestFactor))