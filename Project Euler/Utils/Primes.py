# Functions for handling primes.

from math import sqrt, floor
import random

#-------------------------------------------------------------------------
# Primes
#-------------------------------------------------------------------------

internalPrimelist = [2, 3]

# Miller-Rabin composity test
def CheckIfComposite(number):
    isComposite = True

    def TryIfComposite(a, d, number, s):
        isPossiblePrime = False
        modulo = pow(a, d, number)
        if modulo != 1:
            for i in range(s):
                modulo = pow(a, 2**i*d, number)
                if modulo == number - 1:
                    isPossiblePrime = True
                    break                    
        else:
            isPossiblePrime = True
        return not isPossiblePrime

    if number == 2 or number == 3:
        isComposite = False
    elif number % 2 == 0:
        isComposite = True
    else:
        d = number - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        # Increase the number of primes to try when numbers increase.
        # Heuristically tested limits from Rosettacode.org:
        # https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
        if number < 1373653:
            primes = [2, 3]
        elif number < 25326001: 
            primes = [2, 3, 5]
        elif number < 118670087467: 
            if number == 3215031751: 
                return True
            primes = [2, 3, 5, 7]
        elif number < 2152302898747: 
            primes = [2, 3, 5, 7, 11]
        elif number < 3474749660383: 
            primes = [2, 3, 5, 7, 11, 13]
        else: 
            primes = [2, 3, 5, 7, 11, 13, 17]

        isComposite = any(TryIfComposite(a,d,number,s) for a in primes)

    return isComposite

def AppendPrime(primeList = internalPrimelist):
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

def CheckIfPrime(number, primeList = internalPrimelist):
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

def CheckIfPrimeWithCompositeFilter(number, primeList = internalPrimelist):
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
    primeList = [2]
    k = 1

    for i in range(1, maxPrimes): # Loop until enough primes is found...
        primeFound = False
        while primeFound == False:
            k += 2
            primeFound = not CheckIfComposite(k)
        primeList.append(k)
        
    return primeList

def GeneratePrimeListInWindow(minValue, maxValue):
    primeList = []
    primesInList = 0

    if minValue <= 2:
        primeList.append(2)
        minValue = 3
    elif minValue % 2 == 0:
        minValue += 1

    for i in range(minValue, maxValue, 2):
        primeFound = not CheckIfComposite(i)
        if primeFound == True:
            primeList.append(i)

    return primeList

def GeneratePrimeListBelowValue(maxValue):
    return GeneratePrimeListInWindow(2, maxValue)

def GetSumOfPrimesBelowValue(maxValue, primeList = internalPrimelist):
    primeList = GeneratePrimeListBelowValue(maxValue)
    sumOfPrimes = sum(primeList)
    return sumOfPrimes

def GetLargestPrimeIndex(maxValue, primeList = internalPrimelist):
    i = 0
    while primeList[i] < maxValue:
        i += 1
        while i >= len(primeList):
            AppendPrime(primeList)
    if i > 0:
        i -= 1
    return i

def GetPrime(position, primeList = internalPrimelist):
    while position > len(primeList) - 1:
        AppendPrime(primeList)
    return primeList[position]

#-------------------------------------------------------------------------
# Factors
#-------------------------------------------------------------------------

def GetFactors(number, primeList = internalPrimelist):
    factors = []

    while number > 1 and CheckIfComposite(number) == True:
        i = 0
        while i < len(primeList) and number > 1:
            while number % primeList[i] == 0:
                number = number / primeList[i]
                factors.append(primeList[i])
            i += 1
            if i == len(primeList):
                AppendPrime(primeList)
    return factors

def GetLargestFactor(number, primeList = internalPrimelist):
    factors = GetFactors(number, primeList)
    largestFactor = max(factors)
    return largestFactor

def GetSmallestFactor(number, primeList = internalPrimelist):
    factors = GetFactors(number, primeList)
    smallestFactor = min(factors)
    return smallestFactor

def GetNumberOfFactors(number, maxFactorOrder = 0, primeList = internalPrimelist):
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

def GetNumberOfConsecutiveFactors(number, maxFactorOrder, primeList = internalPrimelist):
    factors = 0
    factorsFound = True

    for i in range (0, maxFactorOrder):
        if i == len(primeList):
            AppendPrime(primeList)
        if number % primeList[i] > 0:
            factorsFound = False
            break
            
    return factorsFound

def AreCoprimes(n1, n2, primelist = internalPrimelist):
    areCoprimes = True
    factors1 = GetFactors(n1)
    factors2 = GetFactors(n2)
    for f1 in factors1:
        if f1 in factors2:
            areCoprimes = False
            break
    return areCoprimes

def GetDistinctFactors(number, primeList = internalPrimelist):
    factors = []

    while number > 1 and CheckIfPrime(number, primeList) == False:
        i = 0
        while i < len(primeList) and number > 1:
            while number % primeList[i] == 0:
                number = number / primeList[i]
                if (primeList[i] in factors) == False:
                    factors.append(primeList[i])
            i += 1
            if i == len(primeList):
                AppendPrime(primeList)
    return factors