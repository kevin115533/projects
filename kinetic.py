"""
Program: Kinetic energy Calculator
Author: Kevin Tran

Calculates objects momentum by using the objects mass and and velocity.

1. Get inputs of mass in kilograms and velocity in meters per second

2. Calculate momentum with formula of momentum = (mass)(velocity)

3. Calulate kinetic energy with the formula of k = (1/2)mv**2

4. Print output

"""

mass = int(input("Enter the objects mass in kilogram(s): "))

velocity = int(input("How many meters did this object move in a second? "))

momentum = mass * velocity

kinetic = (1/2* mass) * velocity**2

print("The momentum of the object is " + str(momentum) + "kg per second with a kinetic energy of " + str(kinetic) + " joules.") 
