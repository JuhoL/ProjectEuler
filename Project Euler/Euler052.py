# Project Euler Problem 52: "Permuted multiples"
# 
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import sys
sys.path.insert(0, './Utils')
from Utils import GetPermutations, IsSemiPandigital
import benchmark

for number in range(123456, 165987):
    isSemiPandigital = IsSemiPandigital(number)
    if isSemiPandigital == True:
        permutations = GetPermutations(number)
        count = 0
        for i in range(2, 7):
            if (number * i) in permutations:
                count += 1
            else:
                break
        if count == 5:
            print ("The number is " + str(number))
            break

