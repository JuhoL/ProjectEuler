# Functions for handling primes.

from math import *

def AppendPrime(primeList):
	primesInList = len(primeList)
	primeFound = False
	i = primeList[primesInList - 1]

	if i == 2: # This prevents the issue vith even numbers in i += 2 logic.
		i -= 1

	while primeFound == False: # Loop until enough primes is found...
		primeFound = True
		i += 2
		maxLimit = floor(sqrt(i)) + 1

		for n in range(0, primesInList): # Check if the i is a prime
			if (i % primeList[n] == 0):
				primeFound = False
			if (primeList[n] > maxLimit):
				break;
			
	primeList.append(i)
	return primeList

def CheckIfPrime(number, primeList):
	isPrime = False

	if number > 1:
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
	print ("Generating prime list...")
	primeList = [2]
	primesInList = 1

	for i in range(3, maxValue, 2): # Loop until enough primes is found...
		primeFound = CheckIfPrime(i, primeList)

		if primeFound == True:
			primesInList += 1
			print (str(primesInList) + " found\r", end=''),
			primeList.append(i)

	print ("")
	print ("Done!")
	return primeList

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
	while position > len(primeList):
		AppendPrime(primeList)
	return primeList[len(primeList) - 1]

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