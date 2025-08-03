# Created by truo0052 on Github
import math
import argparse
import textwrap

parser = argparse.ArgumentParser(description="An extensive Python command-line loan calculator that may be used to calculate differential payments as well as annuities. By analyzing alternative repayment plans and computing numerous loan characteristics, this tool assists users in making well-informed financial decisions.")
parser = argparse.ArgumentParser(prog='LoanCalculator.py', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
---------------------------------------------------------------------------------
Calculate Differentiated Payments:
python filename.py --type=diff --principal=1000000 --periods=10 --interest=10 

Calculate Annuity Payment:
python filename.py --type=annuity --principal=1000000 --periods=60 --interest=10

Calculate Repayment Loan:
python filename.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
---------------------------------------------------------------------------------
'''))
parser.add_argument('--payment', type=float, metavar='', help='Monthly payment amount')
parser.add_argument('--principal', type=int, metavar='', help='Loan principal amount')
parser.add_argument('--periods', type=int, metavar='', help='Number of monthly payments')
parser.add_argument('--interest', type=float, metavar='', help='Annual interest rate')
parser.add_argument('--type', choices=['annuity', 'diff', 'notdiff'], type=str, metavar='', help='Type of payment calculation')
args = parser.parse_args()


def validate_inputs():
    # Count non-None arguments
    provided_args = sum([
        args.payment is not None,
        args.principal is not None,
        args.periods is not None,
        args.interest is not None,
        args.type is not None
    ])

    if provided_args < 4:
        return print("To few arguments, please enter three values")

    if args.interest is None:
        return False

    if args.type is None:
        return print("Select --type=annuity or --type=diff")

    # Check for negative values
    if ((args.payment is not None and args.payment < 0) or # if the input is not empty and payment is a negative number return false
            (args.principal is not None and args.principal < 0) or
            (args.periods is not None and args.periods < 0) or
            (args.interest is not None and args.interest < 0)):
        return False

    # For diff type, payment cannot be provided
    if args.type == 'diff' and args.payment is not None:
        return False

    return True


def calculate_monthly_payment(principal, payment, interest):
    i = float(interest / (12 * 100))
    n = math.log(payment / (payment - i * principal)) / math.log(1 + i)
    round_n = math.ceil(n)
    years, months = divmod(round_n, 12)

    overpayment = payment * round_n - principal

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    print(f"Overpayment = {int(overpayment)}")


def calculate_annuity_payment(principal, periods, interest):
    i = float(interest / (12 * 100))
    a = principal * (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
    payment = math.ceil(a)

    overpayment = payment * periods - principal

    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {int(overpayment)}")


def calculate_loan_principal(payment, periods, interest):
    i = float(interest / (12 * 100))
    p = payment * ((1 - math.pow(1 + i, -periods)) / i)
    principal = math.floor(p)  # Round down as shown in examples

    overpayment = payment * periods - principal

    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {int(overpayment)}")


def calculate_differentiated_payment(principal, periods, interest):
    i = float(interest / (12 * 100))
    total_paid = 0

    for m in range(1, periods + 1):
        d = (principal / periods) + i * (principal - (principal * (m - 1)) / periods)
        d = math.ceil(d)  # Round up
        total_paid += d
        print(f"Month {m}: payment is {d}")

    overpayment = total_paid - principal
    print(f"Overpayment = {overpayment}")


if __name__ == '__main__':
    if not validate_inputs():
        print("Incorrect parameters")
    else:
        if args.type == 'diff':
            calculate_differentiated_payment(args.principal, args.periods, args.interest)

        elif args.type == 'annuity':
            if args.payment is None:
                # Calculate payment
                calculate_annuity_payment(args.principal, args.periods, args.interest)
            elif args.periods is None:
                # Calculate periods
                calculate_monthly_payment(args.principal, args.payment, args.interest)
            elif args.principal is None:
                # Calculate principal
                calculate_loan_principal(args.payment, args.periods, args.interest)
            elif args.type == 'notdiff':
                print("Incorrect parameters")
