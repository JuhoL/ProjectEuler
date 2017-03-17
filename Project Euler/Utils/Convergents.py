#-------------------------------------------------------------------------
# Convergence
#-------------------------------------------------------------------------

from math import floor, sqrt

def GetSqrtConvergents(S, n):
	m = 0
	d = 1
	a = floor(sqrt(S))
	a0 = a
	convergents = [a]
	n -= 1

	while n > 0:
		m = d*a - m
		d = (S-m**2)/d
		a = floor((a0+m)/d)
		convergents.append(a)
		n -= 1

	return convergents

def GetFractionsFromConvergents(convergents):
	fractions = []
	p0 = 0
	p1 = 1
	q0 = 1
	q1 = 0

	for a in convergents:
		p = a*p1 + p0
		q = a*q1 + q0
		fractions.append([p,q])
		p0 = p1
		p1 = p
		q0 = q1
		q1 = q

	return fractions

class Convergent:
	def __init__(self, S):
		self.S = S

		# Variable a for calculating convergents
		self.a = floor(sqrt(S))
		self.a0 = self.a
		self.convergents = [self.a]
		self.m = 0
		self.d = 1

		# Variables for calculating fractionals
		self.p0 = 0
		self.p1 = 1
		self.q0 = 1
		self.q1 = 0
		self.fractions = []

	def GetSqrtConvergent(self, n):
		while n >= len(self.convergents):
			self.m = self.d*self.a - self.m
			self.d = (self.S-self.m**2)/self.d
			self.a = floor((self.a0+self.m)/self.d)
			self.convergents.append(self.a)
		return self.convergents[n]

	def GetFraction(self, n):
		while n >= len(self.fractions):
			self.a = self.GetSqrtConvergent(len(self.fractions))
			p = self.a*self.p1 + self.p0
			q = self.a*self.q1 + self.q0
			self.fractions.append([p,q])
			self.p0 = self.p1
			self.p1 = p
			self.q0 = self.q1
			self.q1 = q
		return self.fractions[n]

	def GetFractions(self):
		return self.fractions

	def GetConvergents(self):
		return self.convergents