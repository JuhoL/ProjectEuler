# Project Euler Problem 14: "Highly divisible triangular number"
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

import sys
sys.path.insert(0, './Utils')
import benchmark

longestChain = 0
numberWithLongestChain = 0

for i in range(2, 999999):
	number = i
	steps = 0
	while number != 1:
		if number % 2 != 0:
			number = number*3 + 1
		else:
			number = number / 2
		steps += 1

	if steps > longestChain:
		longestChain = steps
		numberWithLongestChain = i
		print (str(numberWithLongestChain) + " has " + str(longestChain) + " steps.", end="\r")

print ("The number " + str(numberWithLongestChain) + " has the longest chain of " + str(longestChain) + " steps."),