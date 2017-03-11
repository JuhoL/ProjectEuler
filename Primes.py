# Functions for handling primes.

def GeneratePrimeList(maxPrimes):
	print ("Generating prime list...")
	primeList = [2]
	k = 1

	for i in range(1, maxPrimes): # Loop until enough primes is found...
		primeFound = False
		while primeFound == False:
			primeFound = True
			k += 2
			for n in range(0,i): # Check if the next k is a prime
				if (k % primeList[n] == 0):
					primeFound = False
					break
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
		primeFound = True
		
		for n in range(0, primesInList): # Check if the i is a prime
			if (i % primeList[n] == 0):
				primeFound = False

		if primeFound == True:
			primesInList += 1
			print (str(primesInList) + " found\r", end=''),
			primeList.append(i)

	print ("")
	print ("Done!")
	return primeList

def GetSumOfPrimesBelowValue(maxValue):
	print ("Generating prime list...")
	primeList = [2]
	primesInList = 1
	sumOfPrimes = 2

	for i in range(3, maxValue, 2): # Loop until enough primes is found...
		primeFound = True
		
		for n in range(0, primesInList): # Check if the i is a prime
			if (i % primeList[n] == 0):
				primeFound = False

		if primeFound == True:
			primesInList += 1
			percentage = ((i*1000)//maxValue)/10
			print (str(percentage) + "% complete\r", end=''),
			primeList.append(i)
			sumOfPrimes += i

	print ("")
	print ("Done!")
	return sumOfPrimes

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

def GetLargestFactor(number, primeListSize):
	primeList = GeneratePrimeList(primeListSize)
	largestFactor = 0

	print ("Factors of " + str(number) + ":")
	while CheckIfPrime(number, primeList) == False:
		tooSmallPrimes = True
		for i in range(0, primeListSize):
			if number % primeList[i] == 0:
				number = number / primeList[i]
				largestFactor = primeList[i]
				print (str(largestFactor))
				tooSmallPrimes = False
		if tooSmallPrimes == True:
			print ("Primelist is too small! Remainder: " + str(number))
			break
	return largestFactor

def GetPrime(position):
	prime = 0
	k = 2

	if position != 1:
		k = 1

		for i in range(1, position): # Loop until enough primes is found...
			primeFound = False
			while primeFound == False:
				primeFound = True
				k += 2
				for n in range(2,k): # Check if the next k is a prime
					if (k % n == 0):
						primeFound = False
						break
	
	prime = k
	return prime

def AppendPrime(primeList):
	primesInList = len(primeList)
	primeFound = False
	i = primeList[primesInList - 1]

	if i == 2: # This prevents the issue vith even numbers in i += 2 logic.
		i -= 1

	while primeFound == False: # Loop until enough primes is found...
		primeFound = True
		i += 2

		for n in range(0, primesInList): # Check if the i is a prime
			if (i % primeList[n] == 0):
				primeFound = False
			
	primeList.append(i)
	return primeList

def GetLargestFactorDynamic(number):
	primeList = [2]
	largestFactor = 0

	print ("Factors of " + str(number) + ":")
	while CheckIfPrime(number, primeList) == False:
		tooSmallPrimes = True
		i = 0
		while tooSmallPrimes == True:
			if i == len(primeList):
				AppendPrime(primeList)

			if number % primeList[i] == 0:
				number = number / primeList[i]
				largestFactor = primeList[i]
				print (str(largestFactor))
				tooSmallPrimes = False

			i += 1
	return largestFactor

def GetNumberOfFactors(number, primeList, maxFactorOrder = 0):
	factors = 0

	while CheckIfPrime(number, primeList) == False:
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