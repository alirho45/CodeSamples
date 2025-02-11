import pandas as pd

"""
Author: Alisha Rhodes
Date: 02/10/2025
Assignment: Module 04 Programming Assignment Ex 2
Short Desc: A program that reads an Excel file and lists the 3 most expensive items with their names and prices.
"""

# Prompt the user for the input file
file_name = input("Enter the Excel file name (with extension): ")

try:
    # Read the Excel file
    df = pd.read_excel(file_name)

    # Check if required columns exist
    if 'Price' in df.columns and 'Item Name' in df.columns:
        # Get the top three most expensive items
        top_items = df[['Item Name', 'Price']].nlargest(3, 'Price')

        print("\nTop three most expensive items:")
        print(top_items.to_string(index=False, formatters={'Price': lambda x: f"${x:,.2f}"}))
    
    else:
        print("Error: The Excel file must contain both 'Item' and 'Price' columns.")
except Exception as e:
    print(f"An error occurred: {e}")

