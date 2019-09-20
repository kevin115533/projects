"""
Program: Employee pay calculator
Author: Kevin Tran

The purpose of this program is calculate an employees pay considering overtime

1. Get input of employees hours
2. Calculate hourly pay. If there are more than 40 hours then pay is 1.5 times the
    hourly rate for those hours
3. Print output of the calculated paycheck.
"""

# Constants
pay_rate = 15

# Get inputs
emp_name = input("Enter employees name: ")
print("How many hours did " + emp_name + " work this week? ")
hours_clocked = int(input())

# Calculate pay of the employee
if hours_clocked > 40:
    overtime_hours = hours_clocked - 40
    overtime_pay = overtime_hours * (pay_rate*1.5)
    total_pay = (40 * pay_rate) + overtime_pay
else:
    total_pay = hours_clocked * pay_rate

# Print outputs
if hours_clocked > 40:
    print(emp_name + "'s total pay this week is $" + str(total_pay) + " with " + str(overtime_hours)
          + " hours of overtime")
else:
    print(emp_name + "'s total pay this week is $" + str(total_pay))
