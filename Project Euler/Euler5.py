# Project Euler Problem 5: "Smallest multiple"
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys
sys.path.insert(0, './Utils')
import benchmark

lastValue = 20

number = 2520
values = range (2, lastValue)
match = False

while match == False:
	number += lastValue
	match = True
	for i in values:
		if number % i > 0:
			match = False
			break

print ("The smallest number is " + str(number))