# Project Euler Problem 33: "Digit cancelling fractions"
# 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
# simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling
# the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value
# of the denominator.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Primes import GetFactors

# Let all fractions be of form (n1*10 + n2)/(k1*10 + k2), where n1, n2, k1, k2 are netural numbers
# from 1 to 9

matchFractions = []

for n1 in range (1, 10):
	for n2 in range(1,10):
		k1 = n2
		for k2 in range(1,10):
			fraction1 = (n1*10 + n2)/(k1*10 + k2)
			if fraction1 != 1:
				fraction2 = n1/k2
				if fraction1 == fraction2:
					matchFractions.append([(n1*10 + n2), (k1*10 + k2)])
		k2 = n1
		for k2 in range(1,10):
			fraction1 = (n1*10 + n2)/(k1*10 + k2)
			if fraction1 != 1:
				fraction2 = n2/k1
				if fraction1 == fraction2:
					matchFractions.append([(n1*10 + n2), (k1*10 + k2)])

product = matchFractions[0]
for i in range(1, len(matchFractions)):
	product[0] *= matchFractions[i][0]
	product[1] *= matchFractions[i][1]

primeList = [2]
nominatorFactors = GetFactors(product[0], primeList)
denominatorFactors = GetFactors(product[1], primeList)

for n in nominatorFactors:
	if n in denominatorFactors:
		product[0] /= n
		product[1] /= n

print ("The product is " + str(int(product[0])) + "/" + str(int(product[1])))