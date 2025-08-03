# Loan Calculator

 An extensive Python command-line loan calculator that may be used to calculate differential payments as well as annuities.  By analyzing alternative repayment plans and computing numerous loan characteristics, this tool assists users in making well-informed financial decisions.

## Features

- Dual Payment Types: Compute both annuity (constant monthly payments) and differentiated payments (declining payments over time)

- Calculate Repayment Period: Calculates the duration in months or years required to repay a loan based on the principal amount, set monthly payment, and interest rate, as well as the total overpayment incurred.

- Calculate Loan Principal: Calculates the highest loan amount you can afford based on your preferred monthly payment, loan duration, and interest rate, while also displaying the total overpayment.

## Import

- [argparse](https://docs.python.org/3/library/argparse) - Parser for command-line options, arguments and subcommands
- [math](https://docs.python.org/3/library/math.html) - Provides access to common mathematical functions and constants, including those defined by the C standard


## Installation
1. **Download or clone the repository** to your local machine
2. **Open the project in your preferred IDE:**
   - **PyCharm**: File → Open → Select the project folder
   - **VS Code**: File → Open Folder → Select the project folder  
   - **Any other IDE**: Open the project folder containing the Python script

3. **Ensure Python 3+ is installed** on your system. You can download it from [Python.org](https://www.python.org/downloads/)
4. **Run the script using the command line examples below** or through your IDE's terminal/console

## Command Line Examples
Loan Calculator Help Interface
```sh
python LoanCalculator.py -help
```
<img width="700" height="300" alt="help_option" src="https://github.com/user-attachments/assets/a240e84a-2d6a-4168-95e4-863f4dd83ade" />

Calculate Differentiated Payments
```sh
python LoanCalculator.py --type=diff --principal=1000000 --periods=10 --interest=10 
```

Calculate Annuity Payment:
```sh
python LoanCalculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
```

Calculate Repayment Loan:
```sh
python LoanCalculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

