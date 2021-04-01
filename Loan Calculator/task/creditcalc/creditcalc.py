import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

incorrect_status = False
missing_args = []

if args.type == "annuity":

    monthly_payment = int(args.payment) if args.payment else missing_args.append("payment")
    loan_principal = int(args.principal) if args.principal else missing_args.append("principal")
    number_of_periods = int(args.periods) if args.periods else missing_args.append("periods")
    loan_interest = float(args.interest) if args.interest else missing_args.append("interest")

    if len(missing_args) > 1:
        incorrect_status = True
    elif len(missing_args) == 1:
        if missing_args[0] == "payment":
            interest_rate = loan_interest / (100 * 12)
            monthly_payment = math.ceil(loan_principal
                                        * (interest_rate * (1 + interest_rate) ** number_of_periods)
                                        / ((1 + interest_rate) ** number_of_periods - 1))
            over_payment = monthly_payment * number_of_periods - loan_principal
            print(f"Your monthly payment = {monthly_payment}!")
            print(f"Overpayment = {over_payment}")
        elif missing_args[0] == "principal":
            interest_rate = loan_interest / (100 * 12)
            loan_principal = math.floor(monthly_payment
                                        * ((1 + interest_rate) ** number_of_periods - 1)
                                        / (interest_rate * (1 + interest_rate) ** number_of_periods))
            over_payment = round(monthly_payment * number_of_periods - loan_principal)
            print(f"Your loan principal = {loan_principal}!")
            print(f"Overpayment = {over_payment}")
        elif missing_args[0] == "periods":
            interest_rate = loan_interest / (100 * 12)
            number_of_months = math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate
                                                                     * loan_principal), 1 + interest_rate))
            years = number_of_months // 12
            months = number_of_months - 12 * years
            if number_of_months % 12 == 0:
                years_and_months = f"{years} year{'s' if years > 1 else ''}"
            elif number_of_months < 12:
                years_and_months = f"{months} month{'s' if months > 1 else ''}"
            else:
                years_and_months = f"{years} year{'s' if years > 1 else ''} " \
                                   f"and {months} month{'s' if months > 1 else ''}"
            over_payment = round(monthly_payment * number_of_months - loan_principal)
            print(f"It will take {years_and_months} to repay this loan!")
            print(f"Overpayment = {over_payment}")
        elif missing_args[0] == "interest":
            incorrect_status = True
    else:
        incorrect_status = True

elif args.type == "diff":

    monthly_payment = int(args.payment) if args.payment else missing_args.append("payment")
    loan_principal = int(args.principal) if args.principal else missing_args.append("principal")
    number_of_periods = int(args.periods) if args.periods else missing_args.append("periods")
    loan_interest = float(args.interest) if args.interest else missing_args.append("interest")

    diff_payment = []

    if len(missing_args) != 1:
        incorrect_status = True
    else:
        if missing_args[0] == "payment":
            sum_up_payment = 0
            interest_rate = loan_interest / (100 * 12)
            for month in range(number_of_periods):
                diff_payment.append(math.ceil((loan_principal / number_of_periods) + interest_rate
                                              * (loan_principal - (loan_principal * (month + 1 - 1))
                                                 / number_of_periods)))
                sum_up_payment += diff_payment[month]
                print(f"Month {month + 1}: payment is {diff_payment[month]}")
            over_payment = sum_up_payment - loan_principal
            print(f"\nOverpayment = {over_payment}")
        else:
            incorrect_status = True

else:
    incorrect_status = True

if incorrect_status:
    print("Incorrect parameters")
