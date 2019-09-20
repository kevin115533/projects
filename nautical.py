"""
Program: Nautical Miles Calculator
Author: Kevin Tran

The purpose of this program is to convert kilometers to nautical miles.

1. Get user input kilometers to convert.

2. Calculate nautical miles using provided kilometer using formula
    nm = (km/10000) * 5400

3. Print results    

"""

km = int(input("Enter the amount of kilometers to convert: "))

nm = (km/10000) * 5400

print("The conversion of " + str(km) +" kilometers is approximatley " + str(round(nm)) + " nautical miles")
