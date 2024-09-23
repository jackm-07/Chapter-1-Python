#Author: Jack Maher
#Date: 20-09-24
#Pg25 T2-6

#T2
# fullName = input("What is your full name:") #asking for name
# spaceLocation = fullName.index(" ") #finding the space
# firstName = fullName[:spaceLocation] #up to spacelocation is first name
# lastName = fullName[spaceLocation+1:]#spacelocation plus 1 is last name
# print("First name is", firstName)#printing name
# print("Last name is", lastName)#   ^

#T3
# hours=int(input("Enter the hours of the time:"))
# minutes=int(input("Enter the minutes of the time:"))
# seconds=int(input("Enter the seconds of the time:"))
# hours=hours*60*60
# minutes=minutes*60
# secondTotal=hours+minutes+seconds
# print(secondTotal,"seconds total in your calculations")

#T4
# personNumber=int(input("Enter the amount of seconds you want converted to minutes:"))
# personNumber=round(personNumber/60)
# print(personNumber)

# #T5
# counter=1
# while counter<6:
#     asciiNumber=str(input("Please type a character to be converted to ascii:"))
#     print(asciiNumber,"=",ord(asciiNumber))
#     counter=counter+1

#T6
# print("Hello Ahmed! My name is Computer and I want to help you figure out your electricity bill!")
# unitsUsed=int(input("Could you write here how many units of electricity you used this month:"))
# totalCharge=unitsUsed*0.19+26.20
# print("You owe the company",totalCharge)

#T7
# fishOrder=int(input("WE DON'T HAVE ALL DAY GIVE ME THE ORDERS NOW!!! FISH FIRST:"))
# chipsOrder=int(input("STOP DAWDLING AROUND! CHIPS HOW MANY:"))
# price=round(fishOrder*4.50,1)+round(chipsOrder*2.80,1)
# print("Hello valued customer!!! You ordered",fishOrder,"fish and",chipsOrder," chips right?\nYour total is",price,"euros")       

#T8
wordOfEncryption = input("Type the word you want encrypted here (lower case only):")
counter=1
import random
key=random.randint(1,26)
print("key is",key)
wordLength=len(wordOfEncryption)
while counter<wordLength+1:
    letter1=ord(wordOfEncryption[counter-1:counter])
    letter1=letter1+key
    if letter1>124:
        letter1=letter1-26
    else:
        letter1=letter1
    counter=counter+1
    print(letter1,end=" ")
   
