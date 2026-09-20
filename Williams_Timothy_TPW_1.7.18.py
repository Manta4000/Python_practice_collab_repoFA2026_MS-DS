"Williams_Timothy_TPW_1.7.18"
###Calculating the area of a circle and volume of a sphere with input radius
##Solved: but I think I am going to add some multivariable calculus principles to this for fun soon
import math as m

pi = m.pi
r = int(input("What is the radius of your circle/sphere? (assuming units in meters): "))

A = pi*(r**2)
V = (4/3)*pi*(r**3)

print("The area of a circle with radius ", r, " meters is ", round(A, 3), " square meters.")
print("The volume of a sphere with radius ", r, " meters is ", round(V, 3), " cubic meters.")