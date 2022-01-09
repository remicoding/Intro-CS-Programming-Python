"""
Remi Coding
Problem Set 0 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""
# Imports
import numpy

# Get entries from user
num_x = int(input('\nEnter number x: '))
num_y = int(input('Enter number y: '))

# Calculations
x_to_power_y = num_x**num_y
log_2_x = numpy.log2(num_x)

# Printing output
print('X**y =', x_to_power_y)
print('log(x) = ', int(log_2_x), '\n')
