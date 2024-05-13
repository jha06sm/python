import math
print("enter a,b,c in the format ax^+bx+c")
a=input("enter value of a")
a=int(a)
b=input("enter value of b")
b=int(b)
c=input("enter value of c")
c=int(c)
d=b^2-4*a*c
print("descriminant is:%d"%d)
x1=(-b+math.sqrt(d))/2
x2=(-b-math.sqrt(d))/2
print(x1)
print(x2)
