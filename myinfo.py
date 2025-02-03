import re

# Function to get valid input with retry if the input is invalid
def get_valid_input(prompt, regex, error_message):
    while True:
        user_input = input(prompt)
        if re.match(regex, user_input):
            return user_input
        else:
            print(error_message)

# Get user input for name, address, and telephone number

firstName = get_valid_input("Enter your First name: ", "^[a-zA-Z]+$", "Error! Only letters a-z or A-Z allowed!")

lastName = get_valid_input("Enter your Last name: ", "^[a-zA-Z]+$", "Error! Only letters a-z or A-Z allowed!")

# Get address input, assuming it's valid as long as it's not empty
while True:
    address = input("Enter your address: ")
    if address.strip() == "":
        print("Error! Address cannot be empty!")
    else:
        break

# Get valid phone number input (only numbers)
while True:
    phone_number = get_valid_input("Enter your telephone number: ", r'^\d{10}$', "Error! The phone number is incomplete or contains invalid characters")
    if phone_number:
        break
    
# Print the entered information
print("Information of: " + firstName)
print("Name: " + firstName + " " + lastName)
print("Address: " + address)
print("Telephone Number: " + phone_number)



