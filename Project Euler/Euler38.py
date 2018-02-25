# Project Euler Problem xx: "xx"
# 
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import sys
sys.path.insert(0, './Utils')
from Utils import IsPandigital, IsSemiPandigital
import benchmark

concatenationMax = 0
concatenationValue = 0

# It is obvious that the first product must start with a 9. This limits the values to try. Let's try pandigitals in range of 9123-9876
for value in range (9123, 9877):
    # If the initial value is semi-pandigital, check wether its double is also a semi-pandigital.
    isPandigital = IsSemiPandigital(value)
    if isPandigital == True:
        isPandigital = IsSemiPandigital(value*2)

    # If both the original value and its double are pandigital, check if their concatenation is true pandigital.
    if isPandigital == True:
        concatenation = int(str(value) + str(value*2))
        isPandigital = IsPandigital(concatenation)

    if isPandigital == True:
        if (concatenation > concatenationMax):
            concatenationMax = concatenation
            concatenationValue = value

print ("The largest pandigital concatenation is " + str(concatenationMax) + " produced by value " + str(concatenationValue))
