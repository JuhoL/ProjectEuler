# Project Euler Problem 63: "Powerful digit counts"
# 
# The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

import sys
sys.path.insert(0, './Utils')
import benchmark

n = 2
integers = 9 # All x^1 where x < 10 are trivial cases.

while True:
    iterations = 0
    x = 2
    windowMin = 10**(n-1)
    windowMax = 10**n
    while x**n < windowMin:
        x += 1
    
    while x**n < windowMax:
        x += 1
        integers += 1
        iterations += 1

    if iterations > 0:
        n += 1
    else:
        break

print ("There are " + str(integers) + " integers.")
