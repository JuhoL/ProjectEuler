# Project Euler Problem 22: "Names scores"
# 
# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

import sys
sys.path.insert(0, './Utils')
import benchmark

def GetNameScore(name, position):
	score = 0
	subtraction = ord('A') - 1

	for i in range(1, len(name) - 1):
		score += ord(name[i]) - subtraction
	score *= position

	return score

fileName = "p022_names.txt"

file = open(fileName, 'r')
nameList = sorted(file.readlines()[0].split(","))
file.close()

totalNameScore = 0
for i in range(0, len(nameList)):
	totalNameScore += GetNameScore(nameList[i], i + 1)

print ("The total name score is " + str(totalNameScore))