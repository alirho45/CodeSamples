"""
Author: Alisha Rhodes
Date: 01/27/2025
Assignment: Module 02 Programming Assignment
Short Desc: A program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number and displays the factorial.

"""

# Function to calculate factorial
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # Multiply factorial by each number from 1 to n
    return factorial

# Get user input and validate
while True:
    try:
        num = int(input("Enter a nonnegative integer: "))
        if num < 0:
            print("Please enter a nonnegative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid nonnegative integer.")

# Calculate and display 
result = calculate_factorial(num)
print(f"The factorial of {num} is {result}.")
