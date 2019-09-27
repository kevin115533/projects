"""
Program: Right Triangle
Author: Kevin Tran

The purpose of this program to is find if a triangle is a right triangle

1. Get input on 3 sides of the triangle
2. Compare lengths
3. Print output
"""

sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))
sideC = float(input("Enter the length of side C: "))

a = sideA**2
b = sideB**2
c = sideC**2

result1 = a + b
result2 = a + c
result3 = b + c

if result1 == c:
    print("This is a right triangle")

elif result2 == b:
    print("This is a right triangle")

elif result3 == a:
    print("This is a right triangle")
    
else:
    print("This is not a right triangle")
