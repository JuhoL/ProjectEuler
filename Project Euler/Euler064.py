# Project Euler Problem 64: "Odd period square roots"
# 
# The first ten continued fraction representations of (irrational) square roots are:
# 
# sqrt(2)=[1;(2)], period=1
# sqrt(3)=[1;(1,2)], period=2
# sqrt(5)=[2;(4)], period=1
# sqrt(6)=[2;(2,4)], period=2
# sqrt(7)=[2;(1,1,1,4)], period=4
# sqrt(8)=[2;(1,4)], period=2
# sqrt(10)=[3;(6)], period=1
# sqrt(11)=[3;(3,6)], period=2
# sqrt(12)= [3;(2,6)], period=2
# sqrt(13)=[3;(1,1,1,1,6)], period=5
# 
# Exactly four continued fractions, for N <= 13, have an odd period.
# 
# How many continued fractions for N <= 10000 have an odd period?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Convergents import *
from Utils import IsSquare

# This is almost exactly the same solution as to problem number 66.
# The only difference is that we are interested wether the polynome results in 1 or -1.
# Beyond these points the convergents start to repeat.

def GetRepeatingFractionsPeriod(D):
	pq = []
	if D == 2 or IsSquare(D) == False:
		convergent = Convergent(D)
		i = 1
		while True:
			pq = convergent.GetFraction(i)
			polynome = pq[0]**2 - D*pq[1]**2
			if polynome == 1 or polynome == -1:
				# A simple check to differentiate 1 and 2 period repeats.
				nextConvergent = convergent.GetSqrtConvergent(i + 1)
				convergents = convergent.GetConvergents()
				if nextConvergent != convergents[1]:
					i += 1
				break
			i += 1
	else:
		i = 0
	return i

oddPeriod = 0
for i in range (2, 10001):
	period = GetRepeatingFractionsPeriod(i)
	if period % 2 > 0:
		oddPeriod += 1

print (str(oddPeriod) + " fractions have odd periods.")