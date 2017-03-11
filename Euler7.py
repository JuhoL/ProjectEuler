# Project Euler Problem 7: "10001st prime"
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import benchmark

def GetPrime(position):
	print ("Finding prime...")
	prime = 0
	k = 2
	primeList = [2]

	for i in range(1, position): # Loop until enough primes is found...
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
	prime = k
	return prime

print ("The 10001th prime is " + str(GetPrime(10001)))