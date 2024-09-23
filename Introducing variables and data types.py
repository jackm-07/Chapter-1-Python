# Author: Jack Maher
# September 4th 2024
# Introducing variables and data types

firstname = "Jack"
surname = "Maher"

print(firstname, surname)
print("My name is", firstname, surname)

firstname = "Jackius"
print(firstname)

#it can be over-rided
#firstname is a string

print(type(firstname))
# it tells us <class 'str'> meaning its a string

random_letters = "27447^&   ^*£^  YD\\   \\%"
print(random_letters)
print(type(random_letters))
# if you want a \ then you need it twice

number_sequence = 283853
number_sequence_two = 84022
print(number_sequence)
print(number_sequence_two)
print(number_sequence - number_sequence_two)
print(type(number_sequence))
# i got two number sequences and i got the program to minus them

decimal_sequence = 1.56
print(decimal_sequence)
print(type(decimal_sequence))
# decimals are defined as "float"
# = means assigning in CS

print("\n\n\n")

#prompt the user for their firstname, surname and age and print their answers to the screen using variables
print("Hello! Welcome to my program.")
print("Answer my questions please!")
firstname = input("Please enter your name:")
lastname = input("Plese enter your surname:")
age = int(input("Please enter your age in years (numbers):"))
print("Thanks for responding!")
print("Your name is", firstname, lastname, "and you are", age, "years old")
#we are getting the user to put in info and for age we use int(input to force a numerical value
