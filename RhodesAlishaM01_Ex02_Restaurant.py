"""

Author:  Alisha Rhodes
Date written: 01/19/2025
Assignment:   Module 01 Programming Assignment Part 2
Short Desc: This script utilizes a predefined dataset of menu items, including their prices. It prompts you to enter the menu item number and confirm the selection by displaying the item's name. You can add items one at a time, but adding multiple quantities of the same item in a single step (e.g., 2x Item Number 1) is not yet supported. The script calculates and displays several totals, including: the pre-tax total, the tax amount, the total with tax, the tip amount, and the overall total. Calculations are based on a tax rate of 8% and a suggested tip rate of 18%. 


"""
# Define Menu Item List with Item Number, Name and Price
menu_items = [("01", "Schnitzel", 15.50),("02", "Fries", 3.00),("03", "Burger", 5.99),("04", "Spicy Artisan Chicken Sandwich", 7.50),("11", "Fountain Drink", 1.99),("12", "Lemonade", 2.30),("13", "Water", 0.00)]

# Define Variables    
total_pre_tax = 0.00
tax_rate = 0.08  
tip_rate = 0.18 
checkout = []

while True:
        # Ask for menu item number
        item_number = input("Enter Menu Item Number: ").strip().lower()
        
        # Search for the item by number
        found = False
        for item in menu_items:
            if item[0] == item_number:
                found = True
                item_name = item[1]
                item_price = item[2]
                
                # Confirm Item by spelling it out
                confirm_item = input("Do you mean: " + item_name + " (Y/N)? ").strip().lower()


                if confirm_item == 'y':
                    checkout.append(item)  # Add the item to the cart
                    total_pre_tax += item_price
                    print("Added " + item_name + " for $" + "{:.2f}".format(item_price))

                break
        
        if not found:
            print("Invalid item number. Please try again.")
            continue

        # Ask if the user wants to add more items
        add_more = input("Would you like to add more items? (Y/N): ").strip().lower()
        if add_more == 'n':
            break  # Exit the loop if no more items are to be added

# Print each menu item entered
print("Menu Items Entered:")
for item in checkout:
     print("- " + item[1] + " for $" + str(item[2]))


# Correct calculations with rounding
tax_amount = round(total_pre_tax * tax_rate, 2)
total_with_tax = round(total_pre_tax + tax_amount, 2)
tip_amount = round(total_with_tax * tip_rate, 2)
total_with_tax_and_tip = round(total_with_tax + tip_amount, 2)

# Print the final results with string concatenation
print("Total Pre-Tax: $" + str(round(total_pre_tax, 2)))
print("Sales Tax: $" + str(round(tax_amount, 2)))
print("Total with Tax: $" + str(round(total_with_tax, 2)))
print("Proposed Tip: $" + str(round(tip_amount, 2)))
print("Total with Tax and Tip: $" + str(round(total_with_tax_and_tip, 2)))


