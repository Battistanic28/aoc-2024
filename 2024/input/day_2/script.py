# Read the content of the input file
with open('input/day_2/input.txt', 'r') as file:
    data = file.readlines()

# Convert to a 2D array (split by space and line breaks)
array_2d = [line.strip().split() for line in data]

# Write the 2D array to output.py
open("input/day_2/output.py", "x")
with open('input/day_2/output.py', 'w') as file:
    file.write(f"array_2d = {array_2d}\n")
