# Project Euler Problem 10: "Summation of primes"
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import benchmark
import Primes

value = 10000

sumOfPrimes = Primes.GetSumOfPrimesBelowValue(value)
print ("Sum of primes below " + str(value) + " is " + str(sumOfPrimes))