with open("input/day_4/input.txt", "r") as file:
    lines = file.read().splitlines()

# Convert lines into a 2D list
array_2d = [list(line) for line in lines]

open("input/day_4/output.py", "x")
with open("input/day_4/output.py", "w") as file:
    file.write(f"array_2d = {array_2d}\n")
