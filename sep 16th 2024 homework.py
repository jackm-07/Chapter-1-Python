#Author : Jack Maher
# Date 16 sep 24
# Homework task 2-5

"""
Task 2:
I believe that the code would pull each number from the string and print it.

Task 3:
i) There is only 0123 in the string
ii) Strings are immutable

Task 4:
Program 1: I think it will print Leaving Certificate Computer Science
Program 2: I think it will print The fox jumps over the lazy dog!
Program 3: I think it will concatenate the noun and 's'

Task 5:
A to 2
B to 5
C to 9
D to 1
E to 8
F to 7
G to 6
H to 3
I to 4
"""

 #Task 2
# Purpose: A program to demonstrate basic string slicing

# Initialise the string
print("TASK 2 - basic string slicing")
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  

# Extract from index 1 up to but NOT including index 5
print(pangram[1:5]) # "he q"

# Extract from index 17 up to but NOT including index 19
print(pangram[17:19]) # ox

print(pangram[:19])   # "The quick brown fox"
print(pangram[20:26]) # "jumps"
print(pangram[26:])   # "over the lazy dog!"

# Task 3
# Purpose: Check if strings are immutable
# print("\nTASK 3 - Out of range, strings are immutable")
# name = "Mary"
# print(name[4])   # Out of range index
# 
# name = "Mary"
# name[3] = "k"    # String is immutable so can't update a single character

# Task 4
# Purpose: A program to demonstrate string concatenation

print("\nTASK 4 - String concatenation")
print("Program 1")

word1 = "Leaving"
word2 = "Certificate"
word3 = "Computer"
word4 = "Science"
subjectName = word1 + word2 + word3 + word4

print("\nProgram 2")
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  

print(pangram[:3] + pangram[16:])

print("\nProgram 3")
noun = input("Enter a singular noun: ")
print("The plural of "+noun+" is "+noun+"s")
