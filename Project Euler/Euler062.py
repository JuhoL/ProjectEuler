# Project Euler Problem 62: "Cubic permutations"
# 
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations of its digits are cube.

import sys
sys.path.insert(0, './Utils')
from Utils import ArePermutations, GetFinalPermutation
import benchmark

def GetCube(n, cubes):
    if len(cubes) <= n:
        for i in range(len(cubes), n + 1):
            cubes.append(i**3)
    return cubes[n]

def CheckForCubicPermutations(cube, ns, upperLimit, cubes):
    if len(ns) < 5:
        n = ns[-1] + 1
        nextCube = GetCube(n, cubes)
        while nextCube <= upperLimit:
            permutationsFound = ArePermutations(cube, nextCube)
            if permutationsFound == True:
                ns.append(n)
                permutationsFound = CheckForCubicPermutations(cube, ns, upperLimit, cubes)
                del ns[-1]

            if permutationsFound == False:
                n += 1
                nextCube = GetCube(n, cubes)
            else:
                break
        if nextCube > upperLimit:
            permutationsFound = False
    else:
        permutationsFound = True
    return permutationsFound

cubes = []
n = 346

while True:
    cube = GetCube(n, cubes)
    #print ("n = " + str(n) + ", cube = " + str(cube))
    ns = [n]
    upperLimit = GetFinalPermutation(cube)
    permutationsFound = CheckForCubicPermutations(cube, ns, upperLimit, cubes)
    if permutationsFound == False:
        n += 1
    else:
        break

print ("The smallest cube is " + str(cube))

