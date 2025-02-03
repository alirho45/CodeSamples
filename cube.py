"""
This Script calculate the surface area of a cube from a given length.

Analysis: The mathematical defined formula to calculate the surface area of a cube is 6 times the square of the length of the edge. Per definition of a cube all edges have the same length defined as as variable a.

Pseudocode:
input length of the edge of the cube
store length of cube as variable
calculate surface area using 6*variable^2
Print result of calculations
End

"""

# Prompt for input
input_edge_length = int(input("Enter edge lenght: "))

# Define variable
a = input_edge_length

# Calculate
surface_area = 6*a**2

# Result
print("Surface area:",surface_area)



