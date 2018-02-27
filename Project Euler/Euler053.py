# Project Euler Problem 53: "Combinatoric selections"
# 
# There are exactly ten ways of selecting three from five, 12345:
# 
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# 
# In combinatorics, we use the notation, 5C3 = 10.
# 
# In general,
# 
# nCr =	n!/(r!(n-r)!), where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# 
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import GetCombinatoricSelection

maxLimit = 100

exceeded = 0
for n in range(23, maxLimit + 1):
	r = n
	while r > 0:
		if GetCombinatoricSelection(n, r) > 1000000:
			exceeded += 1
		r -= 1

print (str(exceeded) + " nCr values exceeded 1,000,000.")