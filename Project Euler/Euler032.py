# Project Euler Problem 32: "Pandigital products"
# 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import sys
sys.path.insert(0, './Utils')
from Utils import GetNextPandigitalPermutation
import benchmark

pandigit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
products = []

lastPermutation = False
while lastPermutation == False:
    result = pandigit[5]*1000 + pandigit[6]*100 + pandigit[7]*10 + pandigit[8]

    if result not in products:
        for i in range(0, 4):
            x = 0
            y = 0

            for k in range(0, 5):
                if k <= i:
                    x += pandigit[k] * 10**(i-k)
                else:
                    y += pandigit[k] * 10**(4-k)
            
            if x*y == result:
                products.append(result)
                break

    lastPermutation = GetNextPandigitalPermutation(pandigit)

sumOfProducts = sum(products)
print ("The sum of the products is " + str(sumOfProducts))
