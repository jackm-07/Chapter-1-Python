# author: Jack Maher
# date: 12-09-24
# Homework pg18 Q26-42 pg19 task 6
"""
26:always integer
27:the remainder of x%y
28:%
29:**
30:Power of
31:?
32:Increasing
33: x=0
    x+=1
    x+=9
34. x=0
    x=x+1
    x=x+9
35.?
36.x floor divided = 5?
37. decreasing
38. BIRDMAS
39. left-to-right
40. arguments means intstructions?
    it finds x then rounds it to 2 decimals
41. string concatenation puts two strings next to each other x+y xy
    string replication repeats a string x*3 xxx
42. see above
"""
#calcualting volume of cylinder

pi = 3.14
r=int(input("What is the radius of the cylinder?:")) #its making it type where none is written
h=int(input("What is the height of the cylinder?:"))
v = pi*r*h
v=round(v,1)
print("The volume is",v)
totalLiquid=1000
print("In order to get",totalLiquid,"to fit into your specified cylinder, it would take",totalLiquid//v,"cylinders")






