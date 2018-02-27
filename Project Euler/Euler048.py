# Project Euler Problem 48: "Self powers"
# 
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 1000^1000.

import sys
sys.path.insert(0, './Utils')
import benchmark

# Expected memory overflow, but what do you know. Well done Python, well done...
sumOfSelfPowers = 0
for i in range (1, 1000):
	sumOfSelfPowers += i**i

print ("Sum is " + str(sumOfSelfPowers))