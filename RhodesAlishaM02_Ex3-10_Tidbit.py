import re

"""
Author:  Alisha Rhodes
Date written: 01/26/2025
Assignment:   Module 02 Practice Exercise 3-10
Short Desc: The Program takes the purchase price of an Item and calculates the lifetime loan payment schedule based on set variables such as 10% down payment, 12% annual interest rate and the 5% of the purchase price in monthly payments. 

"""

# Module to validate input
def get_valid_input(prompt, pattern, error_message):
    while True:
        user_input = input(prompt).strip()
        if user_input and re.match(pattern, user_input):
            return float(user_input)
        print(error_message)

# Constants
ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
DOWNPAYMENT_RATE = 0.10
TABLEFORMATSTRING = "{:<5}{:<18.2f}{:<18.2f}{:<18.2f}{:<18.2f}{:<18.2f}"

# Get input with validation
purchasePrice = get_valid_input(
    "Enter the purchase price (minimum $1): ",
    r"^[1-9]\d*(\.\d+)?$",  # Pattern ensures a number >= 1
    "Invalid input. Please enter a number greater than or equal to 1."
)

# Initialize
monthlyPayment = 0.05 * purchasePrice
month = 1
balance = purchasePrice - (purchasePrice * DOWNPAYMENT_RATE)

# Output header
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  New Balance")
print("-" * 80)

# While loop to calculate payments
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance  # Pay off the remaining balance
        interest = balance * MONTHLY_RATE
        principal = monthlyPayment
        remaining = 0
    else:
        interest = balance * MONTHLY_RATE
        principal = monthlyPayment - interest
        remaining = balance - monthlyPayment

    # Display payment details only if balance is greater than 0 after this payment
    if balance > 0:
        print(f"{month:<5}{balance:<18.2f}{interest:<18.2f}{principal:<18.2f}{monthlyPayment:<18.2f}{remaining:<18.2f}")

    # Update balance and increment month
    balance = remaining
    if balance == 0:  # Exit loop if balance is zero
        break
    month += 1
