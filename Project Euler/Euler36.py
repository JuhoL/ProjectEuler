# Project Euler Problem 36: "Double-base palindromes"
# 
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import sys
sys.path.insert(0, './Utils')
import benchmark
from Utils import *

if len(sys.argv) < 2:
	print ("Give maximum limit as an argument.")
else:
	maxValue = int(sys.argv[1])

	# Since leading zeros are forbidden, all values must be odd. 1 is trivial case.
	sumOfDoublePalindromes = 1
	for i in range(3, maxValue, 2):
		if IsPalindrome(i) and IsBinaryPalindrome(i):
			sumOfDoublePalindromes += i

	print ("The sum of double-base palindromes below " + str(maxValue) + " is " + str(sumOfDoublePalindromes))