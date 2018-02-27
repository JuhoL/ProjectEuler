# Project Euler Problem 60: "Prime pair sets"
# 
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result
# will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import sys
sys.path.insert(0, './Utils')
from Primes import CheckIfPrime, GeneratePrimeListBelowValue, GetPrime
import benchmark

def CheckIfConcatenates(a, b, primeList):
    x = int(str(a) + str(b))
    isPrime = CheckIfPrime(x, primeList)
    if isPrime == True:
        x = int(str(b) + str(a))
        isPrime = CheckIfPrime(x, primeList)
    return isPrime

def FindPrimePairSets(primeIndices, primeList):
    if len(primeIndices) == 5:
        print ("Found primes:")
        primeSum = 0
        for i in primeIndices:
            print (str(primeList[i]))
            primeSum += primeList[i]
        print ("The sum of these primes is " + str(primeSum))
        exit()

    for i in range(primeIndices[-1] + 1, len(primeList)):
        a = GetPrime(i, primeList)
        for k in primeIndices:
            b = GetPrime(k, primeList)
            concatenates = CheckIfConcatenates(a, b, primeList)
            if concatenates == False:
                break
        if concatenates == True:
            primeIndices.append(i)
            FindPrimePairSets(primeIndices, primeList)
            del primeIndices[-1]

    return

print ("Generating prime list...")
primeList = GeneratePrimeListBelowValue(10000)
print ("Done!")

for i in range(1, len(primeList)):
    primeIndices = [i]
    FindPrimePairSets(primeIndices, primeList)
