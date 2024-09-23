#Author Jack Maher
#Date 18-9-24
#Ascii table

# print(ord("J"))
# print(ord("a"))
# print(ord("c"))
# print(ord("k"))
# 
# print(ord("M"))
# print(ord("a"))
# print(ord("h"))
# print(ord("e"))
# print(ord("r"))
# 
# print("from binary to letters")
# print(chr(ord("J")))
# print(chr(ord("a")))
# print(chr(ord("c")))
# print(chr(ord("k")))
# 
# print(chr(ord("M")))
# print(chr(ord("a")))
# print(chr(ord("h")))
# print(chr(ord("e")))
# print(chr(ord("r")))

print(ord("H"),ord("e"),ord("l"),ord("l"),ord("o"))


def theMaherEncryption():
    desiredHiddenMessage = input("Enter message here")
    key = 23
    counter=0
    while counter<len(desiredHiddenMessage):
        print(ord(desiredHiddenMessage[counter])+key)
        counter=counter+1


theMaherEncryption()