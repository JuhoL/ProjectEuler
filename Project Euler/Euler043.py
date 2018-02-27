# Project Euler Problem 43: "Sub-string divisibility"
# 
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# 
# d2 d3 d4 = 406 is divisible by 2
# d3 d4 d5 = 063 is divisible by 3
# d4 d5 d6 = 635 is divisible by 5
# d5 d6 d7 = 357 is divisible by 7
# d6 d7 d8 = 572 is divisible by 11
# d7 d8 d9 = 728 is divisible by 13
# d8 d9 d10 = 289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

import sys
sys.path.insert(0, './Utils')
from Utils import GetNextPandigitalPermutation, PrintDigitPermutation, DigitPermutationToInteger
import benchmark

def GetSubstring(permutation, n):
    value = permutation[n] * 100
    value += permutation[n+1] * 10
    value += permutation[n+2]
    return value

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
def CheckSubstringProperty(permutation):
    global primes

    # Do some prefiltering. If the substrings start from dn, following must apply:
    #     a. n <= 2
    #     b. d(n+2) must be even
    #     c. d(n+4) must be either 5 or 0
    match = False
    for n in range(0, 2):
        if (permutation[n+2] % 2 == 0) and (permutation[n+4] % 5 == 0):
            match = True
            break

    if match == True:
        for i in range(1,(8-n)):
            value = GetSubstring(permutation, (n+i))
            if (value % primes[i]) != 0:
                match = False
                break

    return match

permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sumOfPandigitals = 0

lastPermutation = False
while lastPermutation == False:
    found = CheckSubstringProperty(permutation)

    if found == True:
        sumOfPandigitals += DigitPermutationToInteger(permutation)

    lastPermutation = GetNextPandigitalPermutation(permutation)

print ("The sum of the special pandigitals is " + str(sumOfPandigitals))
