"""
Program: Guessing Game
Author: Kevin Tran

The purpose of this program is to play a number guessing game

1. Get user input for range of numbers
2. Get input for a minimum number of guesses for the computer
3. The computer will generate a random number
4. Print output until the correct number is guessed or minimum guesses is reached
"""

import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = int(input("Enter the your number: "))
compGuesses = int(input("How many tries does the computer get? "))
compWins = True

for x in range (compGuesses):
    compNumber = random.randint(smaller, larger)
    print("Computer guesses number: ", compNumber)
    if compNumber < myNumber:
        print("Too small")
    elif compNumber > myNumber:
        print("Too large")
    else:
        print("The computer has guesses your number!")
        compWins = False
        break
if compWins == True:
    print("Computer has ran out of guesses!")

