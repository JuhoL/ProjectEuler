# Project Euler Problem 58: "Spiral primes"
# 
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
# 
#       37 36 35 34 33 32 31
#       38 17 16 15 14 13 30
#       39 18  5  4  3 12 29
#       40 19  6  1  2 11 28
#       41 20  7  8  9 10 27
#       42 21 22 23 24 25 26
#       43 44 45 46 47 48 49
# 
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 = 62%.
# 
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

import sys
sys.path.insert(0, './Utils')
from Primes import CheckIfPrime
import benchmark

# The diagonal numbers form following sequence:
# 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49, ....
#
# It is easy to see that the values increment depending on the layer where they reside.
# If the central 1 is layer 0, then the incerment is layer * 2.

diagonals = [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
primeCount = 0
indicesChecked = 0
layer = 3
i = len(diagonals) - 1

while True:
    layer += 1
    increment = layer*2
    for corners in range(0, 4):
        diagonals.append(diagonals[i] + increment)
        i += 1

    for k in range (indicesChecked, len(diagonals)):
        isPrime = CheckIfPrime(diagonals[k])
        if isPrime == True:
            primeCount += 1
    indicesChecked = len(diagonals)

    percentage = (primeCount * 100) // (len(diagonals) + 1)
    if percentage < 10:
        break

# The side length in relation to the layer is easy to see:
# L1 = 3
# L2 = 5
# L3 = 7
# Lx = Lx*2 + 1

sideLength = layer*2 + 1

print ("Current layer is " + str(layer) + " and its side length is " + str(sideLength))
