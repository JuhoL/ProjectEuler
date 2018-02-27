# Project Euler Problem 20: "Factorial digit sum"
# 
# n! means n x (n - 1) x ... x 3 x 2 x 1
# 
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import *

order = 100
factorial = GetFactorial(order)
sumOfDigits = GetSumOfDigits(factorial)

print ("The sum of digits of " + str(order) + "! is " + str(sumOfDigits))