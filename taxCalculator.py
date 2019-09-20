"""
Program: Tax calculator
Author: Kevin Tran

Calculate income tax.

"""

# Initialzed constants
tax_rate = .20
stan_deduction = 10000.0
depend_deduction = 3000.0

# Get inputs from user
income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

# Calculate taxes
taxable_income = income - stan_deduction - \
                 depend_deduction * dependents

income_tax = taxable_income * tax_rate

# Print output to rounded number
print("The income tax is $" + str(round(income_tax)))
