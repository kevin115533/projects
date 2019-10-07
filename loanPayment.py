"""
Program: Loan payment calculator
Author: Kevin Tran

The purpose of this program is to display a payment plan of specified price

1. Get item price input
2. Calculate down payment
3. Print months and headers
4. Calculate the all the numbers
5. print table
"""

itemPrice = float(input("Enter the price of the item: "))
downPayment = itemPrice * .10
monthCount = 0

print("Down payment of the item is $",downPayment)
print("%20s" % "Balance", "%12s" % "Interest" , "%12s" % "Principal", "%12s" % "Payment", "%20s" % "Remaining Balance")

amountOwed = itemPrice - downPayment
payment = amountOwed * .05
remaining = (amountOwed + (amountOwed * .12/12)) 
stillPaying = True

while stillPaying == True:
    balance = remaining
    interest = balance * .12/12
    principal = payment - interest
    remaining = balance - payment
    if remaining <= 0.0:
        stillPaying = False
    monthCount += 1
    if balance > payment:
        print("Month ", monthCount,"%9s" % "%.2f" % balance ,"%12s" % "%.2f" % interest,"%10s" % "%.2f" % principal,"%14s" % "%.2f" % payment,"%17s" % "%.2f" % remaining)
    else:
        print("Month ", monthCount,"%9s" % "%.2f" % balance ,"%11s" % "%.2f" % interest,"%10s" % "%.2f" % principal,"%14s" % "%.2f" % balance,"%17s" % "%.2f" % 0.00)
    

