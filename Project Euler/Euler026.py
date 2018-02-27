# Project Euler Problem 26: "Reciprocal cycles"
# 
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import GetFactors, GeneratePrimeListBelowValue

# It is know that a fraction in lowest terms with a prime denominator other than 2 or 5
# (i.e. coprime to 10) always produces a repeating decimal. The length of the repetend
# (period of the repeating decimal) of 1/n is equal to the order of 10 modulo n. If 10
# is a primitive root modulo n, the repetend length is equal to n - 1; if not, the repetend
# length is a factor of n - 1.

primeList = GeneratePrimeListBelowValue(30)
longestRepeat = 0
longestRepeatD = 0

for i in range (11, 1000):
	factors = GetFactors(i, primeList)
	if (2 in factors) == False and (5 in factors) == False:
		exp = 2
		while pow (10, exp, i) != 1:
			exp += 1
		if (longestRepeat < exp):
			longestRepeat = exp
			longestRepeatD = i

print ("The longest repeating is 1/" + str(longestRepeatD) + " with " + str(longestRepeat) + " repeating digits.")