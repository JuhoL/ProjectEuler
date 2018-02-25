# Project Euler Problem 31: "Coin sums"
# 
# In England the currency is made up of pounds and pences, and there are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pounds (200p).
#
# How many different ways can 2 pounds be made using any number of coins?

import sys
sys.path.insert(0, './Utils')
import benchmark

# Combinatorics time! Let's count in pences. We want to find numer of solutions for n = 200.
# Let's notate the number of coins in each solutions in this way:
# a = number of 1p coins,
# b = number of 2p coins,
# ...
# g = number of 1 pound coins and
# h = number of 2 pound coins.
#
# So we can write the equation with wighted values:
# a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = n
#
# This results in combinatorial generating equation series:
# [x^n](1 + x + x^2 + x^3 + ... + x^200)*(1 + x^2 + x^4 + x^6 + ... + x^200)*(1 + x^5 + x^10 + ... + x^200) ...
#
# When the polynome is calculated open, the total number of combinations can be extracted from the coefficient of x^n.

def GetPartialCombination(x, n):
    # Every value can be selected 0 times, so it is guaranteed to be valid for any value.
    i = 1
    partialCombinations = {0:1}

    while (i * x) <= n:
        partialCombinations[(i*x)] = 1
        i += 1
    
    return partialCombinations

def MultiplyPolynomeDictionaries(polynome1, polynome2):
    result = {}
    for expInP1 in polynome1:
        for expInP2 in polynome2:
            newExp = expInP1 + expInP2
            product = polynome1[expInP1] * polynome2[expInP2]
            if (result.has_key(newExp)):
                result[newExp] += product
            else:
                result[newExp] = product
    return result

coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200

# Let's define polynomes as dictionaries in a way that the dictionary key corresponds to the given exponent.
combinations = {0 : 1}

for i in coins:
    partialCombination = GetPartialCombination(i, n)
    result = MultiplyPolynomeDictionaries(combinations, partialCombination)
    combinations.clear()
    combinations = result.copy()

# In the resulting polynome, the coefficient of exponent 200 is the total number of combinations.
totalCombinations = combinations[200]
print ("2 pounds can be made in " + str(totalCombinations) + " different ways.")
