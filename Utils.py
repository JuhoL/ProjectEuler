# Project Euler various utility functions

def GetFactorial(order):
	factorial = order
	for i in range(2, order):
		factorial *= i

	# !0 = 1 according to the convention for an empty product.
	if factorial == 0:
		factorial = 1
	return factorial

def GetTriangular(order):
	triangular = 0
	for i in range(1, order + 1):
		triangular += i
	return triangular

def GetSumOfDigits(number):
	numberString = str(number)
	sumOfDigits = 0
	for i in range (0, len(numberString)):
		sumOfDigits += int(numberString[i])
	return sumOfDigits

def GetNumberOfDivisors(number):
	divisors = 2
	for i in range (2, number):
		if number%i == 0:
			divisors += 1
	return divisors

def GetDivisors(number):
	divisorList = [1]
	for i in range (2, number):
		if number%i == 0:
			divisorList.append(i)
	return divisorList

def GetSumOfDivisors(number):
	divisorList = GetDivisors(number)
	return sum(divisorList)

def IsPalindrome(number):
	palindromeFound = True
	numberString = str(number)
	length = len(numberString)
	for i in range (0, length//2):
		if numberString[i] != numberString[length - i - 1]:
			palindromeFound = False
			break
	return palindromeFound

def IsBinaryPalindrome(number):
	palindromeFound = True
	numberString = bin(number)[2::1]
	length = len(numberString)
	for i in range (0, length//2):
		if numberString[i] != numberString[length - i - 1]:
			palindromeFound = False
			break
	return palindromeFound