number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    if number > 89:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 69:
        letter = "C"
    elif number <60:
        letter = "F"
    print("The letter grade is ", letter)
else:
    print("Error: grade must be between 100 and 0")
