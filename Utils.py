# Project Euler various utility functions

#-------------------------------------------------------------------------
# Factorials
#-------------------------------------------------------------------------

def GetFactorial(order):
	factorial = order
	for i in range(2, order):
		factorial *= i

	# !0 = 1 according to the convention for an empty product.
	if factorial == 0:
		factorial = 1
	return factorial

#-------------------------------------------------------------------------
# Triangulars
#-------------------------------------------------------------------------

triangulars = [0]

def CalculateTriangular(order):
	return order*(order+1)//2

def GetTriangular(order):
	maxOrder = len(triangulars) - 1
	while maxOrder < order:
		maxOrder += 1
		triangulars.append(CalculateTriangular(maxOrder))
	return triangulars[order]

def CheckIfPentagonal(number):
	isTriangular = False

	if number > 0:
		while number > max(triangulars):
			triangulars.append(CalculateTriangular(len(triangulars)))

		for i in range(len(triangulars)-1, 0, -1):
			if triangulars[i] == number:
				isTriangular = True
				break

	return isTriangular

#-------------------------------------------------------------------------
# Pentagonals
#-------------------------------------------------------------------------

pentagonals = [0]

def CalculatePentagonal(order):
	return (order*(3*order-1))//2

def GetPentagonal(order):
	maxOrder = len(pentagonals) - 1
	while maxOrder < order:
		maxOrder += 1
		pentagonals.append(CalculatePentagonal(maxOrder))
	return pentagonals[order]

def CheckIfPentagonal(number):
	isPentagonal = False

	if number > 0:
		while number > max(pentagonals):
			pentagonals.append(CalculatePentagonal(len(pentagonals)))

		for i in range(len(pentagonals)-1, 0, -1):
			if pentagonals[i] == number:
				isPentagonal = True
				break

	return isPentagonal

#-------------------------------------------------------------------------
# Hexagonals
#-------------------------------------------------------------------------

hexagonals = [0]

def CalculateHexagonal(order):
	return order*(2*order-1)

def GetHexagonal(order):
	maxOrder = len(hexagonals) - 1
	while maxOrder < order:
		maxOrder += 1
		hexagonals.append(CalculateHexagonal(maxOrder))
	return hexagonals[order]

def CheckIfHexagonal(number):
	isHexagonal = False

	if number > 0:
		while number > max(hexagonals):
			hexagonals.append(CalculateHexagonal(len(hexagonals)))

		for i in range(len(hexagonals)-1, 0, -1):
			if hexagonals[i] == number:
				isHexagonal = True
				break

	return isHexagonal

#-------------------------------------------------------------------------
# Fibonacci
#-------------------------------------------------------------------------

def GetFibonacci(order):
	fibonacci = 1
	fibonacciPrevious = 1
	for i in range(0, order):
		temp = fibonacci
		fibonacci = fibonacci + fibonacciPrevious
		fibonacciPrevious = temp

#-------------------------------------------------------------------------
# Sum of digits
#-------------------------------------------------------------------------

def GetSumOfDigits(number):
	numberString = str(number)
	sumOfDigits = 0
	for i in range (0, len(numberString)):
		sumOfDigits += int(numberString[i])
	return sumOfDigits

#-------------------------------------------------------------------------
# Divisors
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
# Palindromes
#-------------------------------------------------------------------------

def GetPalindrome(number):
	numberString = str(number)
	palindromeString = ""
	for i in range (len(numberString)-1, -1, -1):
		palindromeString += numberString[i]
	return int(palindromeString)

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

#-------------------------------------------------------------------------
# Pandigitality
#-------------------------------------------------------------------------

def IsPandigital(number, noZeros = True):
	isPandigital = True
	numberString = str(number)
	if len(numberString) <= 10:
		digits = [False]*(len(numberString) + 1)
		if noZeros == True:
			digits[0] = True

		for i in range(len(numberString) - 1, -1, -1):
			digit = int(numberString[i])
			if digit < len(digits) and digits[digit] == False:
				digits[digit] = True
			else:
				isPandigital = False
				break
	else:
		isPandigital = False
	return isPandigital

#-------------------------------------------------------------------------
# Sum of letters
#-------------------------------------------------------------------------

def GetSumOfLetters(word):
	sumOfLetters = 0

	# Assume the word is in all-caps and has quotation marks, e.g. "CAR"
	subtraction = ord('A') - 1
	for i in range(1, len(word) - 1):
		sumOfLetters += ord(word[i]) - subtraction

	return sumOfLetters

#-------------------------------------------------------------------------
# Combinatorics
#-------------------------------------------------------------------------

# Get combinatoric selection nCr, which means selectin r from n.
def GetCombinatoricSelection(n, r):
	a = GetFactorial(n)
	b = GetFactorial(r)
	c = GetFactorial(n-r)
	selection = a/(b*c)

	return selection

#-------------------------------------------------------------------------
# Convergence
#-------------------------------------------------------------------------

def NextConvergent(pq):
	p = pq[0]
	q = pq[1]
	pq[0] = (p+2*q)
	pq[1] = (p+q)
	return