# Project Euler Problem 3: "Largest prime factor"
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import benchmark

primeListSize = 2000
problemNumber = 600851475143

def GeneratePrimeList(maxPrimes):
	print ("Generating prime list...")
	primeList = [2]
	k = 2

	for i in range(1, maxPrimes): # Loop until enough primes is found...
		primeFound = False
		while primeFound == False:
			primeFound = True
			k += 1
			for n in range(0,i): # Check if the next k is a prime
				if (k % primeList[n] == 0):
					primeFound = False
					break
		print (str(i) + " found\r", end=''),
		primeList.append(k)
	print ("")
	print ("Done!")
	return primeList

def CheckIfPrime(number, primeList):
	isPrime = False

	if number == 1:
		isPrime = True
	else:
		size = len(primeList)
		for i in range(0,size):
			if primeList[i] == number:
				isPrime = True
				break
	return isPrime

def GetLargestFactor(number):
	primeList = GeneratePrimeList(primeListSize)
	largestFactor = 0

	print ("Factors of " + str(number) + ":")
	while CheckIfPrime(number, primeList) == False:
		tooSmallPrimes = True
		for i in range(0, primeListSize):
			if number % primeList[i] == 0:
				number = number // primeList[i]
				largestFactor = primeList[i]
				print (str(largestFactor))
				tooSmallPrimes = False
		if tooSmallPrimes == True:
			print ("Primelist is too small! Remainder: " + str(number))
			break
	return largestFactor

largestFactor = GetLargestFactor(problemNumber)
print ("The largest factor of " + str(problemNumber) + " is " + str(largestFactor))