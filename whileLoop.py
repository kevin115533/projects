sum1 = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    sum1 += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is ", sum1)
