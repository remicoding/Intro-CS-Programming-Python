"""
Remi Coding
Problem Set 1 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""

# In[ Part A: House Hunting ]

annual_salary = int(input('\nEnter your annual salary: '))

# from salary each month
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))

total_cost = int(
    input('Enter the cost of your dream home: '))  # $, cost of dream home
portion_down_payment = 0.25 * total_cost  # portion needed for down payment
savings = 0  # $, amount saved thus far
r = 0.04  # annual return

# initializing variables for while loop
months = 0

while savings < portion_down_payment:
    savings = savings + (savings * r /
                         12) + (annual_salary / 12) * portion_saved
    months += 1

print('Number of months:', months, '\n')