sum1 = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    sum1 += number
print("This sum is ", sum1)
