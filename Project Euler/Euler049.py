# Project Euler Problem 49: "Prime permutations"
# 
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?

import sys
sys.path.insert(0, './Utils')
from Primes import GeneratePrimeListInWindow
from Utils import GetPermutations
import benchmark

primeList = GeneratePrimeListInWindow(1000, 10000)
resultFound = False

for i in range (0, (len(primeList) - 3)):
    prime = primeList[i]
    if prime != 1487:
        permutations = GetPermutations(prime)
        for i in range(1, len(permutations) - 1):
            if permutations[i] in primeList:
                increase = permutations[i] - prime
                thirdValue = permutations[i] + increase
                if (thirdValue in permutations) and (thirdValue in primeList):
                    result = str(prime) + str(permutations[i]) + str(thirdValue)
                    print ("Found " + result)
                    resultFound = True
                    break
        if resultFound == True:
            break
