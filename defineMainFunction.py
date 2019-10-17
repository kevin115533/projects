"""
File: computesSquare.py
Illustrtates the definition of a main function.
"""

def main():
    """The main function of this script"""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

def square(x):
    """Returns the square of x."""
    return x * x

main()
