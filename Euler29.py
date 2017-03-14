# Project Euler Problem 29: "Distinct powers"
# 
# Description

import benchmark
import sys

if len(sys.argv) < 2:
	print ("Give upper limit as an argument.")
else:
	valueMax = int(sys.argv[1])

	combinations = []

	for a in range(2, valueMax + 1):
		for b in range(2, valueMax + 1):
			combinations.append(a**b)

	finalList = set(combinations)

	print ("There are " + str(len(finalList)) + " distinct terms.")