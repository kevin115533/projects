"""
Program: Triangle comparison
Author: Kevin Tran

The purpose of this program to is compare the side lengths of a triangle

1. Get input on 3 sides of the triangle
2. Compare lengths
3. Print output
"""

a = int(input("Enter the length of side A: "))
b = int(input("Enter the length of side B: "))
c = int(input("Enter the length of side C: "))

if a == b == b == c:
    print("The triangle is equilateral")
else:
    print("The triangle is not equilateral")
