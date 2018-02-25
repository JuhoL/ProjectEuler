# Project Euler Problem 56: "Powerful digit sum"
# 
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
# one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import sys
sys.path.insert(0, './Utils')
from Utils import GetSumOfDigits
import benchmark

maxSumOfDigits = 0

for a in range (90, 100):
    for b in range (90, 100):
        value = a**b
        sumOfDigits = GetSumOfDigits(value)
        if sumOfDigits > maxSumOfDigits:
            maxSumOfDigits = sumOfDigits

print ("The maximum digital sum is " + str(maxSumOfDigits))
