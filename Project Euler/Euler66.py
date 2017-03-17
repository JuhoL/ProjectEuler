# Project Euler Problem 66: "Diophantine equation"
# 
# Consider quadratic Diophantine equations of the form:
# 
# x^2 – Dy^2 = 1
# 
# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
# 
# It can be assumed that there are no solutions in positive integers when D is square.
# 
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
# 
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
# 
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import sys
sys.path.insert(0, './Utils')
import benchmark
from Convergents import *
from Utils import IsSquare

def SolveDiophantineEquation(D):
	pq = []
	if D == 2 or IsSquare(D) == False:
		convergent = Convergent(D)
		i = 1
		while True:
			pq = convergent.GetFraction(i)
			polynome = pq[0]**2 - D*pq[1]**2
			if polynome == 1:
				break
			i += 1
	else:
		pq = [0,0]
	return pq

largestX = 0
largestXD = 0
for i in range(2, 1001):
	pq = SolveDiophantineEquation(i)
	if pq[0] > largestX:
		largestX = pq[0]
		largestXD = i

print ("The largest x is " + str(largestX) + " with D = " + str(largestXD))