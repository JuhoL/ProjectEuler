# Project Euler Problem 51: "Prime digit replacements"
# 
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
# having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# 
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

import sys
sys.path.insert(0, './Utils')
from Primes import GeneratePrimeListInWindow
import benchmark

def CheckForRepeatingNumbers(numberString, minimumRepeats, repeatingMaximum):
    repeatingNumbers = []

    for i in range(0, repeatingMaximum + 1):
        repeats = numberString.count(str(i))
        if repeats >= minimumRepeats:
            repeatingNumbers.append(i)

    return repeatingNumbers

print ("Generating prime list...")
primeList = GeneratePrimeListInWindow(100000, 1000000)
print ("Done!")

numberOfPrimes = 8
minimumRepeats = 3
repeatingMaximum = 9 - numberOfPrimes
minimumFound = False

for prime in primeList:
    primeString = str(prime)
    
    repeatingNumbers = CheckForRepeatingNumbers(primeString, minimumRepeats, repeatingMaximum)
    
    if len(repeatingNumbers) > 0:
        for number in repeatingNumbers:
            count = 1
            for i in range(number + 1, 10):
                numberString = primeString.replace(str(number), str(i))
                if int(numberString) in primeList:
                    count += 1

            if count >= numberOfPrimes:
                print ("Found prime " + str(prime) + " that repeats " + str(numberOfPrimes) + " times.")
                minimumFound = True
                break
    if minimumFound == True:
        break
