# Project Euler Problem 20: "Factorial digit sum"
# 
# n! means n × (n − 1) × ... × 3 × 2 × 1
# 
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 
# Find the sum of the digits in the number 100!

import benchmark
import sys
from Utils import *

if len(sys.argv) < 2:
	print ("Give factorial order as an argument.")
else:
	order = int(sys.argv[1])
	factorial = GetFactorial(order)
	sumOfDigits = GetSumOfDigits(factorial)
	
	print ("The sum of digits of " + str(order) + "! is " + str(sumOfDigits))