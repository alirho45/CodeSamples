import re

"""

Author:  Alisha Rhodes
Date written: 01/25/2025
Assignment:   Module 02 Practise Exercise 3-9
Short Desc: A series of numbers is put in individually until the user preses the Enter key to calculate the sum and average

"""

# Module to validate input
def get_valid_input(prompt, pattern, error_message):
    while True:
        user_input = input(prompt).strip()
        if user_input == "" or re.match(pattern, user_input):
            return user_input
        print(error_message)

# Initialize variables needed
sum = 0
count = 0

while True:
    # Get valid input
    input_number = get_valid_input(
        "Enter a number or press Enter to quit: ",
        r"^-?[0-9]+(\.[0-9]+)?$",  # Valid input range, allow negative and positive numbers
        "Error! Please enter a valid numeric input."
    )
    
    if input_number == "":
        break  # Exit if the user presses Enter

    try:
        # Add to the sum and increment count
        sum += float(input_number)
        count += 1
    except ValueError:
        print(" An error occurred. Please try again.")

# Display results
print("The sum is", sum)
if count > 0:
    print("The average is", sum / count)