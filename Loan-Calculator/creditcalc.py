"""
Loan Calculator
Stage 4/4: Differentiate payment.
Payment is different each month

Dm = (P / n) + i * (P - (P * (m - 1)) / n)

Dm - mth differentiated payment
P = the principal loan
i = nominal interest rate. 1/12 * annual interest rate, float
n = number of payments. number of months
m = current repayment month

Example command-line input
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

1. Dm
    interest
    number of months
    loan principal
    user calculated:
        number of payments
        payment amount, or
        loan principal
    if fewer than four parameters provided
        "Incorrect parameters"
    if negative values entered
        "Incorrect parameters"

2. Annuity Payment
    principal
    number of monthly payments
    monthly payment amount
    user calculated:
        number of payments
        payment amount, or
        loan principal

3. invalid parameters

--type
    annuity
    diff
    If otherwise
        "Incorrect parameters"

--payment
    if --type=diff
        "Incorrect parameters"

--principal
    known if interest, annuity payment, and number of months are known

--periods
    known if interest, annuity payment, and principal are known

--interest
    floating-point value
    must always be provided.
    if --interest is missing:
        "Incorrect parameters"

4. Calculate Overpayment

"""

import math
import argparse

# Create Argument Parser
parser = argparse.ArgumentParser(description="This program replicates a real loan calculator.")

# Example input:
# > python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

# Add Arguments
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="Available choices: annuity, diff")
parser.add_argument("--principal", metavar="p",
                    help="Loan principal")
parser.add_argument("--periods", metavar="n",
                    help="Number of monthly payments")
parser.add_argument("--interest", metavar="i",
                    help="Floating point interest")
# parse args
args = parser.parse_args()

type = args.type
principal = args.principal
count_of_periods = args.periods
interest = args.interest

if type == "diff":
    interest = float(interest) / 12
    monthly_payments = [((principal / count_of_periods) + interest * (principal - (principal * (m - 1)) / count_of_periods)) for m in range(1, count_of_periods)]
    calculating_differentiated_payments = [f"Month {m}: payment is {str(monthly_payments)}/n" for m in monthly_payments]
    print(calculating_differentiated_payments)
    print("/n")
    print("Overpayment = " + principal - monthly_payments.sum)
