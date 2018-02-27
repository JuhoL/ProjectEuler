# Project Euler Problem 16: "Power digit sum"
# 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import sys
sys.path.insert(0, './Utils')
import benchmark

def GetSumOfDigits(number):
	sumOfDigits = 0
	numberString = str(number)
	for i in range (0, len(numberString)):
		sumOfDigits += int(numberString[i])
	return sumOfDigits

previousValue = 0
value = int(1)
exponent = 1000
i = 0
while i <= exponent:
	sumOfDigits = GetSumOfDigits(value)
	if previousValue > value:
		print ("Overflow!")
		break
	else:
		previousValue = value
		value = value << 1
	i += 1

print ("2^" + str(i-1) + "\r\n" + str(previousValue) + "\r\n" + str(sumOfDigits))