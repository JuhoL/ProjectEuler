# Project Euler Problem 17: "Number letter counts"
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

import sys
sys.path.insert(0, './Utils')
import benchmark

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
maxNumberLength = 3
hundredsIndex = maxNumberLength - 3
tensIndex = maxNumberLength - 2
onesIndex = maxNumberLength - 1

def GetNumberWordString(number):
	numberWordString = ""
	lastDecadeWritten = -1

	if number >= 1000:
		numberWordString += "one thousand"
	else:
		numberString = str(number).zfill(maxNumberLength)
		for i in range (0, maxNumberLength):
			if len(numberWordString) > 0 or numberString[i] != '0':
				# Decide wether to print '-', or 'and'
				if numberString[i] != '0':
					if lastDecadeWritten == tensIndex:
						numberWordString += "-"
					elif lastDecadeWritten >= 0:
						numberWordString += " and "

				# Nobody likes teens, so we just separate them from the others.
				if i == tensIndex and numberString[i] == '1':
					numberWordString += teens[int(numberString[i + 1])]
					break
				else:
					if numberString[i] != '0':
						if i == hundredsIndex:
							numberWordString += ones[int(numberString[i])] + " hundred"
						elif i == tensIndex:
							numberWordString += tens[int(numberString[i])]
						else:
							numberWordString += ones[int(numberString[i])]
						lastDecadeWritten = i

	return numberWordString.capitalize()

def GetNumberOfLetters(alphabeticalString):
	numberOfLetters = 0
	for i in range (0, len(alphabeticalString)):
		if alphabeticalString[i].isalpha():
			numberOfLetters += 1
	return numberOfLetters

number = 1000
letters = 0

for i in range(0,number):
	letters += GetNumberOfLetters(GetNumberWordString(i + 1))

print ("Number of letters used is " + str(letters))