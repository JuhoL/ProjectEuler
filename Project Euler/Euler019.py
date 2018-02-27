# Project Euler Problem 19: "Counting Sundays"
# 
# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November. All the rest have thirty-one.
# February has twenty-eight, and on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless
# it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

import sys
sys.path.insert(0, './Utils')
import benchmark

def IsLeapYear(year):
	isLeap = False
	if (year % 100 == 0 and year % 400 == 0) or year % 4 == 0:
		isLeap = True
	return isLeap

# January 1st 1901 was Tuesday. Let's mark 0 = Sunday.
day = 2
sundays = 0
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for year in range(1901, 2001):
	for month in range(0, 12):
		if day % 7 == 0:
			sundays += 1

		if month == 1:
			if IsLeapYear(year):
				day += 1
		day += daysInMonth[month]

print ("There were " + str(sundays) + " sundays.")