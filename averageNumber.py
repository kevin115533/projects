"""
Program: Average number
Author: Kevin Tran

The purpose of this program calculate the sum and average of a series of numbers

1. While loop to get series of numbers
2. calculate sum
3. calculate average
4. Print outputs
"""
sum1 = 0.0
count = 0
data = input("Enter a number or just enter to quit: ")
while data != "":
    count += 1
    number = float(data)
    sum1 += number
    data = input("Enter a number or just enter to quit: ")
average = sum1 / count    
print("The sum is ", sum1)
print("The average is ", average)
