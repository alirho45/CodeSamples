"""

Author:  Alisha Rhodes
Date written: 01/27/2025
Assignment:   Module 02 Programming Assignment
Short Desc: A Program that takes text input, specifically colors, and displays either a result or an error. An error occurs if the user input is not a primary color.

"""

# Function to mix primary colors
def mix_colors(color1, color2):
    # Define valid primary colors and their mixed secondary colors
    primary_colors = ['red', 'blue', 'yellow']
    secondary_colors = {
        ('red', 'blue'): 'purple',
        ('red', 'yellow'): 'orange',
        ('blue', 'yellow'): 'green'
    }
    
    # Check if the input colors are valid
    if color1 not in primary_colors or color2 not in primary_colors:
        return "Error: Invalid color(s). Please enter 'red', 'blue', or 'yellow'."
    
    # Ensure the order doesn't affect the result
    if (color1, color2) in secondary_colors:
        return secondary_colors[(color1, color2)]
    elif (color2, color1) in secondary_colors:
        return secondary_colors[(color2, color1)]
    
    # If the colors are the same, there's no mixing to do
    return "Error! Please enter two different primary colors."

# Get user input for two primary colors
color1 = input("Enter the first primary color (red, blue, yellow): ").strip().lower()
color2 = input("Enter the second primary color (red, blue, yellow): ").strip().lower()

# Mix the colors and display the result
result = mix_colors(color1, color2)
print(result)
