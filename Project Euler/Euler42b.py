# Project Euler Problem 42: "Coded triangle numbers"
# 
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first
# ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word
# a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import GetSumOfLetters, GetTriangular

def CheckIfTriangleWord(word, triangulars):
	isTriangle = False
	sumOfLetters = GetSumOfLetters(word)
	
	while sumOfLetters > max(triangulars):
		triangulars.append(GetTriangular(len(triangulars) + 1))

	if (sumOfLetters in triangulars):
		isTriangle = True

	return isTriangle

fileName = "p042_words.txt"
file = open(fileName, 'r')
wordList = sorted(file.readlines()[0].split(","))
file.close()

# A bit faster list based search.
triangulars = [GetTriangular(1)]

triangleWords = 0
for word in wordList:
	if CheckIfTriangleWord(word, triangulars):
		triangleWords += 1

print ("There are " + str(triangleWords) + " triangle words.")