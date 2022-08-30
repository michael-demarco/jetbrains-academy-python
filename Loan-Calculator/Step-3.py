# Loan Calculator
# Stage 3/4: Annuity payment
# The annuity payment amount is precisely this fixed sum of money that you need to pay at regular intervals.

import math

# write your code here
###
# First, you should ask the user which parameter they want to calculate.
# The calculator should be able to calculate
#     the number of monthly payments,
#     the monthly payment amount,
#     and the loan principal.
###

choice = str(input("""
What do you want to calculate?\n
type "n" for number of monthly payments,\n
type "a" for annuity monthly payment amount,\n
type "p" for loan principal:\n
"""))

# calculate monthly payments
if choice == 'n':
    loan_principal = float(input('Enter the loan principal:\n'))
    monthly_payment = float(input('Enter the monthly payment:\n'))
    loan_interest = float(input('Enter the loan interest:\n')) * 0.01 / 12

    exponent = float(monthly_payment / (monthly_payment - loan_interest * loan_principal))
    base = float(1 + loan_interest)
    number_of_months = math.ceil(math.log(exponent, base))

    if number_of_months >= 12:
        number_of_years = math.floor(number_of_months / 12)
        number_of_months = math.ceil(number_of_months - (number_of_years * 12))

    if number_of_months == 1 and number_of_years == 0:
        print(f'It takes {number_of_months} month to repay the credit')
    elif number_of_months > 1 and number_of_years == 0:
        print(f'It takes {number_of_months} months to repay the credit')
    elif number_of_months == 0 and number_of_years == 1:
        print(f'It takes {number_of_years} year to repay the credit')
    elif number_of_months == 1 and number_of_years == 1:
        print(f'It takes {number_of_years} year and {number_of_months} month to repay the credit')
    elif number_of_months > 1 and number_of_years == 1:
        print(f'It takes {number_of_years} year and {number_of_months} months to repay the credit')
    elif number_of_months == 0 and number_of_years > 1:
        print(f'It takes {number_of_years} years to repay the credit')
    elif number_of_months > 1 and number_of_years > 1:
        print(f'It takes {number_of_years} years and {number_of_months} months to repay the credit')

# calculate monthly payment (annuity payment)
elif choice == 'a':
    loan_principal = float(input('Enter the loan principal:\n'))
    number_of_periods = float(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n')) * 0.01 / 12

    numerator = float(loan_principal * (loan_interest * (math.pow((1 + loan_interest), number_of_periods))))
    denominator = float(math.pow((1 + loan_interest), number_of_periods) - 1)
    annuity_payment = math.ceil(numerator / denominator)

    last_month_payment = math.ceil(loan_principal - ((number_of_periods - 1) * annuity_payment))
    if last_month_payment <= 0:
        print(f'Your monthly payment = {annuity_payment}')
    else:
        print(f'Your monthly payment = {annuity_payment} and the last month payment = {last_month_payment}')

# calculate loan principle
elif choice == 'p':
    annuity_payment = float(input('Enter the annuity payment:\n'))
    number_of_periods = float(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n')) * 0.01 / 12

    numerator = float((loan_interest * math.pow(1 + loan_interest, number_of_periods)))
    denominator = float((math.pow(1 + loan_interest, number_of_periods)) - 1)
    loan_principle = float(annuity_payment / ( numerator / denominator))

    print(f"Your loan principle is {loan_principle}!")
