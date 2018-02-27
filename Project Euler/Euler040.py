# Project Euler Problem 40: "Champernowne's constant"
# 
# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

import sys
sys.path.insert(0, './Utils')
import benchmark

# This function returns a nth digit of given x digit sequence.
# For example GetDigit(9, 3) calculated the 9th digit of three-digit sequence:
#     100101102103...
# and returns it (2, in this case).
def GetDigit(n, digits):
    modulo = (n % digits)

    if modulo == 0:
        k = 0
        digit = 0
    else:
        k = digits - modulo
        digit = 1

    # We can calculate the digit by utilising powers of ten.
    divisor = (digits * 10**k)
    digit = (digit + n // divisor) % 10

    if digits > (k + 1):
        if digit == 0:
            digit = 9
        else:
            digit -= 1

    return digit

# This function simply splits the Champernowne's sequence into single-digit, dual-digit, etc. chunks and passes them to the GetDigit().
def GetChampernownesDigit(n):
    digit = 0

    if n <= 9: # Single-digit numbers in range of 1 to 9.
        digit = GetDigit(n, 1)
    elif n <= 189: # Dual-digit numbers in range of 10 to 189 (19*10 - 1)
        n = n - 9
        digit = GetDigit(n, 2)
    elif n <= 2889: # Triple-digit numbers in range of 190 to 2889 (900*3 + 190 - 1)
        n = n - 189
        digit = GetDigit(n, 3)
    elif n <= 38889:
        n = n - 2889
        digit = GetDigit(n, 4)
    elif n <= 488889:
        n = n - 38889
        digit = GetDigit(n, 5)
    else:
        n = n - 488889
        digit = GetDigit(n, 6)

    return digit

d = [1, 10, 100, 1000, 10000, 100000, 1000000]
product = 1
for i in d:
    digit = GetChampernownesDigit(i)
    product = product * digit

print ("The product of the digits is " + str(product))
