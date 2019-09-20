"""
Program: Momentum Calculator
Author: Kevin Tran

Calculates objects momentum by using the objects mass and and velocity.

1. Get inputs of mass in kilograms and velocity in meters per second

2. Calculate momentum with formula of momentum = (mass)(velocity)

3. Print output

"""

mass = int(input("Enter the objects mass in kilogram(s): "))

velocity = int(input("How many meters did this object move in a second? "))

momentum = mass * velocity

print("The momentum of the object is " + str(momentum) + "kg per second")
