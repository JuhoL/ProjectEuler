# Project Euler Problem 65: "Convergents of e"
# 
# the sequence of the first ten convergents for sqrt(2) are:
# 
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# 
# The first ten terms in the sequence of convergents for e are:
# 
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# 
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

import sys
sys.path.insert(0, './Utils')
from Utils import GetSumOfDigits
import benchmark

eConvergents = [2, 1]

# Generate convergent list.
n = 2
for i in range(2, 100, 3):
    eConvergents.append(n)
    n += 2
    eConvergents.append(1)
    eConvergents.append(1)

# Work backwards from the "lowest" denominator.
numerator = 1
denominator = eConvergents[99]
for i in range(98, -1, -1):
    # Add the next convergent...
    numerator = numerator + eConvergents[i] * denominator
    if i > 0:
        # And take inversion
        numerator, denominator = denominator, numerator

sumOfDigits = GetSumOfDigits(numerator)
print ("The 100th convergent is " + str(numerator) + "/" + str(denominator) + " and the sum of digits in numerator is " + str(sumOfDigits))
