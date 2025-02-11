"""
Author: Alisha Rhodes
Date: 02/10/2025
Assignment: Module 04 Practice Exercise 5-7
Short Desc:  A program in the file unique.py that inputs a text file. The program prints the unique words in the file in alphabetical order.

"""
# Get user input
file_name = input("Enter the file name: ")

# Create an empty list
unique_words = []

# Open file for reading
try:
    with open(file_name, 'r') as input_file:
        # Loop through each line in the file
        for line in input_file:
            words = line.split()  # Split line into individual words
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)
    
    # Sort the list alphabetically
    unique_words.sort()
    
    # Output the unique words
    for word in unique_words:
        print(word)
except FileNotFoundError:
    print("Error: Please check the file name and try again.")
