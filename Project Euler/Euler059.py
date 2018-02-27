# Project Euler Problem 59: "XOR decryption"
# 
# Each character on a computer is assigned a unique code and the preferred standard is ASCII
# (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# 
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# 
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is
# impossible to decrypt the message.
# 
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password
# is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method
# is using a sufficiently long password key for security, but short enough to be memorable.
# 
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt
# (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text
# must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import sys
sys.path.insert(0, './Utils')
import benchmark

def GetPotentialPasswordCharacters(characterList, cryptedCharacter):
    for c in range(ord('a'), ord('z') + 1):
        xor = c ^ cryptedCharacter
        if xor >= ord('a') and xor <= ord('z') or xor >= ord('A') and xor <= ord('Z'):
            characterList.append(c)

file = open("p059_cipher.txt", 'r')

data = file.read()
asciiValues = map(int, data.split(','))

potentialC1s = []
potentialC2s = []
potentialC3s = []

GetPotentialPasswordCharacters(potentialC1s, asciiValues[3])
GetPotentialPasswordCharacters(potentialC2s, asciiValues[1])
GetPotentialPasswordCharacters(potentialC3s, asciiValues[2])

passwordFound = False

for c1 in potentialC1s:
    for c2 in potentialC2s:
        for c3 in potentialC3s:
            testWord = chr(c2^asciiValues[1]) + chr(c3^asciiValues[2]) + chr(c1^asciiValues[3])
            
            # Heuristical test shows that the first character is a non-alphabetical.
            # Let's check the following characters. "The" seems a logical first word...
            if testWord == "The":
                password = [c1, c2, c3]
                passwordFound = True

            if passwordFound == True:
                break
        if passwordFound == True:
            break
    if passwordFound == True:
        break

if passwordFound == True:
    # Let's decrypt...
    decryptedString = ''
    sumOfCharacters = 0
    for i in range (0, len(asciiValues), 3):
        if len(asciiValues) >= (i + len(password)):
            limit = len(password)
        else:
            limit = (i + len(password)) - len(asciiValues) - 1

        for k in range(0, limit):
            sumOfCharacters += asciiValues[i + k] ^ password[k]
            decryptedString += chr(asciiValues[i + k] ^ password[k])

    print ("Decrypted message:\n")
    print (decryptedString)
    print ("\n*******************\n\nThe sum of all characters is " + str(sumOfCharacters))
else:
    print ("No password found...")

file.close()
