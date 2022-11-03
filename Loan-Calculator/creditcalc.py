"""
Loan Calculator
Stage 4/4: Differentiate payment.
Payment is different each month

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

Example input (use pdb to debug):
python -m pdb creditcalc.py --type annuity --payment 8722 --periods 120 --interest 5.6
"""
import math
import argparse
import pdb
import sys


def positive(numeric_type):
    def require_positive(value):
        number = numeric_type(value)
        if number <= 0:
            raise argparse.ArgumentError("Incorrect parameters.")
        return number
    return require_positive


if __name__ == "__main__":
    # Arguments
    parser = argparse.ArgumentParser(description="This program replicates a real loan calculator.")

    parser.add_argument("--type", type=str, choices=["annuity", "diff"], help="Available choices: annuity, diff")
    parser.add_argument("--principal", help="Loan principal")
    parser.add_argument("--payment", help="Loan payment")
    parser.add_argument("--periods", help="Number of monthly payments")
    parser.add_argument("--interest", help="Floating point interest")

    # parse args
    try:
        args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    except SystemExit:
        sys.exit()

    # assign arguments
    argument_count = 0

    if args.type:
        credit_type = args.type
        argument_count += 1
    if args.principal:
        if int(args.principal) > 0:
            loan_principal = int(args.principal)
            argument_count += 1
        else:
            print("Incorrect parameters")
            sys.exit()
    else:
        loan_principal = None
    if args.payment:
        credit_payment = int(args.payment)
        argument_count += 1
    else:
        credit_payment = None
    if args.periods:
        number_of_payments = int(args.periods)
        argument_count += 1
    else:
        number_of_payments = None
    if args.interest:
        nominal_interest_rate = float(args.interest) * .01 / 12
        argument_count += 1

    if argument_count < 4:
        print("Incorrect parameters.")
        sys.exit()

    if credit_type == "diff":
        try:
            mth_differentiated_payment = \
                [math.ceil(((loan_principal / number_of_payments) + \
                        (nominal_interest_rate * (loan_principal - \
                                                  (loan_principal * ((current_repayment_month - 1) / number_of_payments)) \
                                                  ) \
                         ) \
                        ) \
                       ) for current_repayment_month in range(1, number_of_payments + 1)]
            output_list = [f"Month {m + 1}: payment is {str(mth_differentiated_payment[m])}" for m in range(0, len(mth_differentiated_payment))]
            print(*output_list, sep="\n")
            credit_overpayment = abs(int(loan_principal - sum(mth_differentiated_payment)))
            print(f"\nOverpayment = {credit_overpayment}")
        except SystemExit:
            print("Incorrect parameters.")

    if credit_type == "annuity":
        if credit_payment is None and loan_principal is None and number_of_payments is None:
            print("Incorrect Parameters.")

        elif credit_payment is None:
            try:
                numerator = float( \
                    loan_principal * \
                    (nominal_interest_rate * \
                     (math.pow((1 + nominal_interest_rate), number_of_payments)) \
                     ) \
                    )
                denominator = float(math.pow((1 + nominal_interest_rate), number_of_payments) - 1)
                annuity_payment = math.ceil(numerator / denominator)
                credit_overpayment = abs(loan_principal - (annuity_payment * number_of_payments))

                print(f'Your annuity payment = {annuity_payment}!')
                print(f"Overpayment = {credit_overpayment}")

            except SystemExit:
                print("Incorrect parameters.")

        elif loan_principal is None:
            try:
                numerator = float((nominal_interest_rate * math.pow((1 + nominal_interest_rate), number_of_payments)))
                denominator = float((math.pow((1 + nominal_interest_rate), number_of_payments)) - 1)
                loan_principal = int(credit_payment / (numerator / denominator))

                credit_overpayment = int(credit_payment * number_of_payments - loan_principal)

                print(f'Your loan principal = {loan_principal}!')
                print(f"Overpayment = {credit_overpayment}")

            except SystemExit:
                print("Incorrect parameters.")

        elif number_of_payments is None:
            try:
                exponent = float(credit_payment / (credit_payment - (nominal_interest_rate * loan_principal)))
                base = float(1 + nominal_interest_rate)
                number_of_payments = math.ceil(math.log(exponent, base))

                credit_overpayment = int((credit_payment * number_of_payments) - loan_principal)

                if number_of_payments >= 12:
                    number_of_years = math.floor(number_of_payments / 12)
                    number_of_months = math.ceil(number_of_payments - (number_of_years * 12))

                if number_of_months == 1 and number_of_years == 0:
                    print(f'It will take {number_of_months} month to repay this loan!')
                elif number_of_months > 1 and number_of_years == 0:
                    print(f'It will take {number_of_months} months to repay this loan!')
                elif number_of_months == 0 and number_of_years == 1:
                    print(f'It will take {number_of_years} year to repay this loan!')
                elif number_of_months == 1 and number_of_years == 1:
                    print(f'It will take {number_of_years} year and {number_of_months} month to repay this loan!')
                elif number_of_months > 1 and number_of_years == 1:
                    print(f'It will take {number_of_years} year and {number_of_months} months to repay this loan!')
                elif number_of_months == 0 and number_of_years > 1:
                    print(f'It will take {number_of_years} years to repay this loan!')
                elif number_of_months > 1 and number_of_years > 1:
                    print(f'It will take {number_of_years} years and {number_of_months} months to repay this loan!')

                print(f"Overpayment = {credit_overpayment}")

            except SystemExit:
                print("Incorrect parameters.")
