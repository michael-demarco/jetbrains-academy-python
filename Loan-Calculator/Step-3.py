import math

credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
credit_principal = int(input('Enter the loan principal:'))
choice = str(input("""
What do you want to calculate?\n
type "m" - for count of months,\n
type "p" - for monthly payment:"""
                   ))

if choice == 'm':
    monthly_payment = int(input('Enter monthly payment:\n'))
    months_to_repay = math.ceil(credit_principal / monthly_payment)

    if months_to_repay == 1:
        print(f'It takes {months_to_repay} month to repay the credit')
    else:
        print(f'It takes {months_to_repay} months to repay the credit')

elif choice == 'p':
    count_of_months = int(input('Enter the number of months:\n'))
    monthly_payment = math.ceil(credit_principal / count_of_months)
    last_month_payment = math.ceil(credit_principal - ((count_of_months - 1) * monthly_payment))
    if last_month_payment == 0:
        print(f'Your monthly payment = {monthly_payment}')
    else:
        print(f'Your monthly payment = {monthly_payment} and the last month payment = {last_month_payment}')
