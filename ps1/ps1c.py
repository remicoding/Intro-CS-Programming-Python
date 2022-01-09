"""
Remi Coding
Problem Set 1 from Introduction to Computer Science and Programming in Python
MITOPENCOURSEWARE
"""

# In[ Part C: Finding the right amount to save ]

annual_salary_in = int(input('\nEnter your annual salary: '))

total_cost = 1000000  # $, cost of dream home
down_payment = 0.25 * total_cost  # portion needed for down payment
savings = 0  # $, amount saved thus far
r = 0.04  # annual return

semi_annual_raise = .07

# bissection-search parameters
total_months = 36

epsilon = 100  # $
num_guesses = 0
low = 0
high = 10000
guess = ((high + low) // 2) / 10000

while abs(savings - down_payment) >= epsilon and abs(high - low) > 1:
    # reset variables to initial values for next iteration of bisection search
    annual_salary = annual_salary_in
    savings = 0
    months = 0

    for i in range(total_months):
        savings += (savings * r / 12) + (annual_salary / 12) * guess

        months += 1

        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    if savings < down_payment:
        low = int(guess * 10000)
    else:
        high = int(guess * 10000)
    guess = ((high + low) // 2) / 10000
    num_guesses += 1

if savings < down_payment:
    print(
        'It is not possible possible to pay the down payment in three years.\n'
    )
else:
    print('Best savings rate:', guess)
    print('Steps in bisection search:', num_guesses, '\n')