# Functions for handling primes.

from math import sqrt, floor
import random

# Miller-Rabin composity test
def CheckIfComposite(number):
	isComposite = True

	def TryComposite(a, d, number, s):
		isPossiblePrime = False
		modulo = pow(a, d, number)
		if modulo != 1:
			for i in range(s - 1):
				if modulo == number - 1:
					isPossiblePrime = True
					break					
				modulo = pow(modulo, 2, number)
		else:
			isPossiblePrime = True
		return not isPossiblePrime

	if number == 2:
		isComposite = False
	elif number % 2 == 0:
		isComposite = True
	else:
		d = number - 1
		s = 0
		while d % 2 == 0:
			d //= 2
			s += 1
		
		primes = [2, 3, 5, 7, 11, 13, 17]
		for a in primes:
			if a < number - 1:
				if TryComposite(a, d, number, s) == False:
					isComposite = False
					break

	return isComposite

def AppendPrime(primeList):
	primesInList = len(primeList)
	primeFound = False
	i = primeList[primesInList - 1]

	if i == 2: # This prevents the issue vith even numbers in i += 2 logic.
		i -= 1

	while primeFound == False: # Loop until enough primes is found...
		i += 2
		primeFound = not CheckIfComposite(i)
			
	primeList.append(i)
	return primeList

def CheckIfPrimeAks(number):
	isPrime = True

	# If (x - 1)^p - (x^p - 1) coefficients are divisible by p, p is a prime.
	polynome = [1, -1] # (1*x - 1)
	coefficients = [1, -1]

	exponent = number
	while exponent > 1:
		exponent -= 1

		coefficientsTemp = [0]*(len(coefficients) + 1)
		coefficients
		for i in range(0,len(coefficients)):
			for k in [0, 1]:
				coefficientsTemp[i + k] += coefficients[i] * polynome[k]
		coefficients = coefficientsTemp

	# Subtract (x^p - 1)
	coefficients[0] -= 1 # -x^p
	coefficients[len(coefficients) - 1] += 1 # +1

	for i in range(0, len(coefficients)):
		modulo = coefficients[i] % number
		if modulo != 0:
			isPrime = False
			break

	return isPrime

def CheckIfPrime(number, primeList):
	isPrime = False

	if number > 1:
		if number < 4:
			isPrime = True
		else:
			maxLimit = floor(sqrt(number)) + 1
			i = 0
			while 1:
				if primeList[i] == number or primeList[i] > maxLimit: # Any numbers n can have only one prime factor > sqrt(n)
					isPrime = True
					break
				if number % primeList[i] == 0:
					break
				i += 1
				if i >= len(primeList):
					AppendPrime(primeList)
	return isPrime

def CheckIfPrimeWithCompositeFilter(number, primeList):
	isPrime = False

	if number > 1:
		if number < 4:
			isPrime = True
		else:
			if CheckIfComposite(number) == False:
				maxLimit = floor(sqrt(number)) + 1
				i = 0
				while 1:
					if primeList[i] == number or primeList[i] > maxLimit: # Any numbers n can have only one prime factor > sqrt(n)
						isPrime = True
						break
					if number % primeList[i] == 0:
						break
					i += 1
					if i >= len(primeList):
						AppendPrime(primeList)
	return isPrime

def GeneratePrimeList(maxPrimes):
	print ("Generating prime list...")
	primeList = [2]
	k = 1

	for i in range(1, maxPrimes): # Loop until enough primes is found...
		primeFound = False
		while primeFound == False:
			k += 2
			primeFound = CheckIfPrime(k, primeList)
		print (str(i) + " found\r", end=''),
		primeList.append(k)
	print ("")
	print ("Done!")
	return primeList

def GeneratePrimeListBelowValue(maxValue):
	print ("Generating list of primes below " + str(maxValue))
	primeList = [2, 3, 5]
	primesInList = 1

	fiveCount = 0
	for i in range(5, maxValue, 2): # Loop until enough primes is found...
		if fiveCount > 0:
			primeFound = CheckIfPrime(i, primeList)

			if primeFound == True:
				primesInList += 1
				primeList.append(i)
				print(str(i))
			fiveCount -= 1
		else:
			fiveCount = 4

	print ("Done!")
	return primeList

def GeneratePrimeListBelowValueWithSieve(maxValue):
	print ("Generating list of primes below " + str(maxValue))
	finalPrimeList = []
	sieve = [True]*maxValue

	if maxValue > 1:
		primeList = [2]
		finalPrimeList.append(2)
		if maxValue > 2:
			for i in range (3, maxValue, 2):
				if sieve[i] == True and CheckIfPrime(i, primeList) == True:
					for k in range (i + i, maxValue, + i):
						sieve[k] = False
		
		for i in range(3, maxValue, 2):
			if sieve[i] == True:
				finalPrimeList.append(i)
	print ("Done!")
	return finalPrimeList

def GetSumOfPrimesBelowValue(maxValue, primeList = []):
	sumOfPrimes = 2

	if len(primeList) > 0:
		i = 2
		while True:
			prime = GetPrime(i, primeList)
			if prime > maxValue:
				break
			sumOfPrimes += prime
			i += 1
	else:
		print ("Prime search without list.")
		i = 1
		primeList = [2]
		while True:
			primeFound = False
			while primeFound == False: # Loop until enough primes is found...
				primeFound = True
				i += 2
				maxLimit = floor(sqrt(i)) + 1

				for n in range(0, len(primeList)): # Check if the i is a prime
					if (i % primeList[n] == 0):
						primeFound = False
					if (primeList[n] > maxLimit):
						break;
			if i < maxValue:
				sumOfPrimes += i
				primeList.append(i)
			else:
				break
	
	return sumOfPrimes

def GetLargestPrimeIndex(maxValue, primeList):
	i = 0
	while primeList[i] < maxValue:
		i += 1
		while i >= len(primeList):
			AppendPrime(primeList)
	if i > 0:
		i -= 1
	return i

def GetLargestFactor(number, primeList):
	largestFactor = 1

	print ("Factors of " + str(number) + ":")
	while number > 1 and CheckIfPrime(number, primeList) == False:
		i = 0
		while i < len(primeList) and number > 1:
			while number % primeList[i] == 0:
				number = number / primeList[i]
				largestFactor = primeList[i]
				print (str(largestFactor) + " remainder: " + str(number))
			i += 1
			if i == len(primeList):
				AppendPrime(primeList)
	return largestFactor

def GetPrime(position, primeList = [2]):
	while position > len(primeList) - 1:
		AppendPrime(primeList)
	return primeList[position]

def GetNumberOfFactors(number, primeList, maxFactorOrder = 0):
	factors = 0

	while number > 1 and CheckIfPrime(number, primeList) == False:
		factorFound = False
		i = 0
		while factorFound == Flase and (i < maxFactorOrder or maxFactorOrder == 0):
			if i == len(primeList):
				AppendPrime(primeList)

			if number % primeList[i] == 0:
				number = number / primeList[i]
				factors += 1
				factorFound = True
			else:
				i += 1
	return factors

def GetNumberOfConsecutiveFactors(number, primeList, maxFactorOrder):
	factors = 0
	factorsFound = True

	for i in range (0, maxFactorOrder):
		if i == len(primeList):
			AppendPrime(primeList)
		if number % primeList[i] > 0:
			factorsFound = False
			break
			
	return factorsFound