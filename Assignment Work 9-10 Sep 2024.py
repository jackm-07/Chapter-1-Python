# Author: Jack Maher
# Date: 09-Sep-24
# Classwork from Assignment on Teams

#Notes
x=8
y=x
print(y)
x = x+1
print(x)
print(y)
print("\n\n")

#year = int(input("Enter the current year:"))
#age = int(input("What age will you be this year:"))
#print("Your year of birth is:", year-age)
#print("\n\n")

print("2000"+str(18))
print("\n\n")

#program to convert celcius to fahrenheit
#centigrade = float(input("Enter the Centigrade [celcius] value:"))
#fahrenheit = 9/5 * centigrade + 32
#print(centigrade, "degrees C equals", fahrenheit, "degrees F")
#print("\n\n")

#round function
#print(centigrade, "degrees C equals", round(fahrenheit,1), "degrees F")
#print("\n\n")

#remainder operator
print(30 % 10)
print(30 % 15)
print(30 % 20)
print(9 % 4)
print(12 % 5)
print("\n\n")

arrivalTime = (21 + 850000) % 24
print("You will arrive at",arrivalTime)

#Program to calculate a running total

#Initalising the variable
runningTotal = 0

#Perform the calculations
price1 = 10
runningTotal = runningTotal + price1
price2 = 14
runningTotal = runningTotal + price2
price3 = 6
runningTotal = runningTotal + price3

#Displaying the output
print("The total amount for your groceries is", runningTotal)

#Introducing Randoms Numbers

#Program to multiply two randomly generated numbers
import random # why this line?
num1 = random.randint(1,10) # Generates a number between 1 and 10
num2 = random.randint(1,10) # is the same line as 63

#Multiplying the two numbers and displaying
print(num1,"times",num2,"=",num1*num2)

#Program to average five randomly generated numbers
import random
low = random.randint(1,100)
high = random.randint(low,100)
n1 = random.randint(low,high)
n2 = random.randint(low,high)
n3 = random.randint(low,high)
n4 = random.randint(low,high)
n5 = random.randint(low,high)
average = (n1+n2+n3+n4+n5) /5
print("The average of", n1,n2,n3,n4,n5,"is", average)



#Workbook
#Task 1
personName = "Jack"
favouriteColour = "blue"
print("Hello", personName, ", your favourite colour is", favouriteColour,"!")
print("Goodbye",personName)
print("\n\n")

#Task 2
#personName = input("Type your name:")
#favouriteColour = input("What is your favourite colour:")
#print("Hello",personName, "your favourite colour is",favouriteColour)
#print("Goodbye",personName)
#print("\n\n")
# I do not know why it has "none" where its meant to be typed

#Task 3
#Variables must be named before they can be used, the number '1' would be a int, the phrase "Jack is typing this" would be a str and '1.5' would be a float

#Task 4
goals = 0
goals = goals + 1
print("The value of goals is", goals)
print("\n\n")

answer = 1+2
print(answer)
value1 = answer+3
value2 = 1+2+3
print(value1,value2)
print("\n\n")

a = 10
b = 5
temp = a
a = b
b = temp
print("a=",a,"b=",b)
print("\n\n")
# the values get swapped

accountBalance = 1000
withdrawalAmount = 600
accountBalance = accountBalance - withdrawalAmount
print("Your account now has",accountBalance,"euros")
print("\n\n")

days = 1
hrs = 24
mins = 60
secs = 60
total = days*hrs*mins*secs
print(total)

"""
Explaining task 7 in workbook
It firsts asks the user to input the principal
It turns the principal into a float
It then asks for the interest rate and turns that into a float
It finally asks for the length of time in years and turns it into a float
It multiplies all the variables and prints that the interest amount is the amount
"""
#I predict that the task 8 line of code will turn out to be 100
print(pow(10, abs(-2)))

#task nine and ten are in the notes part
"""
The purpose of the variables low and high were to give a random range of integers between 1-100
The 'low' variable was used to set a baseline that the high could not be lower than.
The brackets allowed the order of operations to be rearranged
The running total could have also added up the integers instead of us doing line 15
"""
#Tasks 1-5 on page 18

#Task 1
myAge = 17 #assigning my age to a variable
print("You are",myAge,"years old?\n","What a great age to be!")

#Task 2
decimal1 = 1.5
decimal2 = 2.8
print("The sum of",decimal1,"and",decimal2,"is",decimal1+decimal2)
print("The difference of",decimal1,"and",decimal2,"is",round(abs(decimal1-decimal2),1))
print("The product of",decimal1,"and",decimal2,"is",round(decimal1*decimal2),1) #why no decimal point?

#Task 3
d1 = 1.8
d2 = 3.4
print("The mean of",d2,"and",d1,"is",(d2+d1)/2)
print("The remainder of",d2,"divided into",d1,"is",round((d2 % d1),1))
print("The power of",d2,"to the power of",d1,"is",round((d2**d1),1))

#Task 4
f = float(input("What is the temperature in F:"))
celsius = 5/9 * f -32
print("The temperature of",f,"in centigrade is",round(celsius),1)

#Task 5
mile = 1
kilometre = 1.60935
#The distance between the school and Singapore is 7,067.64 miles
singaporeDistance = mile*7067.64
print("The distance between Singapore and CCC is",singaporeDistance*kilometre,"kilometres")
print("If you were to rent a helicopter with enough fuel to get you to Singapore\n")
print("And it cost you 900 euros per km then it would cost",round(singaporeDistance*kilometre*900,1),"euros")

"""
1.A variable is where data can be stored.
2.The value of a variable is what the variable is equal to
3. variableName = valueOfVariable
4. age = "16"
5. do not put numbers in front and if you want 16 as a string then add your ""
6. camelCase or underscore_method
7. reserved words/keywords are words that tell the program to do something
8. As the program will view it as a botched command and will not compile
9. strings, integers, floats and boolean
strings are things in ""
integers are real whole numbers such as -8 and 2
10. houseNumber = 20
11. = ?
12. int
    print(type(houseNumber))
13. integers
14. float
15. float and integers
16. x = float(5)
    print(type(x))
    result is <class 'float'>
    x = int(5.1)
    print(type(x))
    result is <class 'int'>
17. y = float(6)
18. y = str(6)
19. +-/*//**%
20. + is addition
    - is subtraction
    * is multiplication
    / is division
    % is modulus
21.numericalValue1 = 4
   numericalValue2 = 8
   print("The product of",numericalValue1,"and",numericalValue2,"is",numericalValue1*numericalValue2)
22.numericalValue3 = 10
   numericalValue4 = 2
   print(numericalValue3,"divided by",numericalValue4,"equals",numericalValue3/numericalValue4)
23.floats
24.floor division is the number before the decimal point
25.//
26.always integer
"""




