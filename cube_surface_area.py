"""
Program: Surface area calculator
Author: Kevin Tran

The purpose of this program is to calculate the surface are of a cube.

1. Get user input for the length of single edge of a cube.
2. Calculate surface area of cube from the given input.
    surface_area = 6 (length**)
3. Print out put of surface area.
"""

# Get user input for cube edge length
length = int(input("Enter the length of the cubes edge(inches): "))

# Calculate surface area
surface_area = 6 * length**2

# Print output
print("The surface area of the cube is " + str(surface_area) + " inches")
