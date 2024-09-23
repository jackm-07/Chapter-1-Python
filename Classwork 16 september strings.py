# Author: J.T.M
# Date: 16-Sep-24
# Description: Working with strings

text = "Hello World"
print(text)

print("\n")

counter=0
while counter<11:
    print(counter,"=",text[counter], text[-1])
    counter= counter+1

#strings are immutable - cannot be changed
print("\n\n")
text = "Wello Horld"
counter=0
while counter<11:
    print(counter,"=",text[counter])
    counter= counter+1
    
print("\n\n")

print("length of text =",len(text)) # length of text
print(text[len(text)-1])

#Task 1 of the string workbook spelled: Think!

print(text[:],text[6:],text[:5])

