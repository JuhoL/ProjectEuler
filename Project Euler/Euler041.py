# Project Euler Problem 41: "Pandigital prime"
# 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import *
from Utils import IsPandigital
from math import sqrt

# This is a really bad solution. There are lots of evaluations for non-pandigitals taht take up time.
# Correct solution vould be to build only pandigitals from individual digits and filter out even numbers.
# This requries some recursion. Very similar than the lattice paths problem number 15.
# Maybe I'll return to this problem later and write a proper solution.
# 
# This bad brute-force solution relies on guessing and skipping even pandigitals but subtracting 18 from the
# largest pandigital.
largestPandigitaPrime = 0
for i in range (7654321, 1234567, -18):
	if IsPandigital(i):
		if CheckIfComposite(i) == False:
			largestPandigitaPrime = i
			break

print ("The largest pandigital prime is " + str(largestPandigitaPrime))