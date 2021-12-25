# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations. """

loan_costs = [500, 600, 200, 1000, 450]

# Uses the `len` function to calculate the total number of loans in the list.
# Prints the number of loans from the list
number_of_loans = len(loan_costs)
print("The number of loans in the list is:", number_of_loans)

# What is the total of all loans?
# Uses the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
sum_of_loans = sum(loan_costs)
print("The total of all loans in the list is: ", sum_of_loans)

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculates the average loan price.
# Print the average loan amount
average_loan_price = sum_of_loans / number_of_loans
print("The average loan price of this list is: ", average_loan_price)

"""Part 2: Analyze Loan Data."""

# Given the following loan data, calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Uses get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Prints each variable.
future_value = loan.get("future_value")
print(future_value)

remaining_months = loan.get("remaining_months")
print(remaining_months)


# Uses the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

present_value = future_value / (1 + .20/12) ** remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Writes a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")

if present_value >= loan_price:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is expensive and not worth the price.")


"""Part 3: Perform Financial Calculations."""

# Given the following loan data, calculates the present value for the loan.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defines a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
    return present_value


# Uses the function to calculate the present value of the new loan given below.
#    Uses an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.2
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creates an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loops through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500: 
        inexpensive_loans.append(loan)

# Prints the `inexpensive_loans` list
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file. """

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Uses the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w") as csvfile: 
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)

    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
