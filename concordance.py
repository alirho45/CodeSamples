"""
Author: Alisha Rhodes
Date: 02/10/2025
Assignment: Module 04 Practice Exercise 5-8
Short Desc: A program in the file concordance.py that displays a concordance for a file. The program will output the unique words and their frequencies in alphabetical order.

"""

# Get user input
file_name = input("Enter the file name: ")

# Create an empty list
unique_words = {}

try:
    # Open the input file for reading
    with open(file_name, 'r') as input_file:
        # Process each line in the file
        for line in input_file:
            # Split the line into words
            words = line.split()

            # Process each word in the line
            for word in words:
                # Remove punctuation and convert to lowercase for consistency
                word = word.strip(".,!?()[]{}:;\"'").lower()
                
                # Check if the word is already in the file
                if word in unique_words:
                    # Increment the frequency of the word
                    unique_words[word] += 1
                else:
                    # Add the word to the dictionary with frequency 1
                    unique_words[word] = 1

    # Get the list of unique words and sort them alphabetically
    word_list = sorted(unique_words.keys())

    # Print the unique words and their frequencies
    for word in word_list:
        print(f"{word}: {unique_words[word]}")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
