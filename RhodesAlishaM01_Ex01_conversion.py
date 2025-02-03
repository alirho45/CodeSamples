import math

"""

Author:  Alisha Rhodes
Date written: 01/19/2025
Assignment:   Module 01 Programming Assignment Part 1
Short Desc:   A Script that lets you pick between Celsius and Fahrenheit and converts it to the opposite measurement.


"""
# Starting a Loop to not end the Script when giving a invalid answer.
# Giving user a choice to pick the Coversion needed.
# Using .lower() to accept input in Capital and lower case 
while True:
    choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius:").lower()

    # If C is chosen, calculating an printing the results
    if choice == 'c':
        temp_celsius = int(input("Enter temperature in Celsius: "))
        fahrenheit = round((9/5) * temp_celsius + 32)
        print(str(temp_celsius) + " degrees Celsius are equal to " + str(fahrenheit) + " degrees Fahrenheit.")
   
    # If F is chosen, calculating and printing the results
    elif choice == 'f':
        temp_fahrenheit = int(input("Enter temperature in Fahrenheit: "))
        celsius = round((5/9) * (temp_fahrenheit - 32))
        print(str(temp_fahrenheit) + " degrees Fahrenheit are equal to " + str(celsius) + " degrees Celsius.")
    
    # should choose entry be invalid, display Error message.
    else:
        print("Invalid input. Please enter 'C' or 'F'.")
