# One acre of land is equivalent to 43,560 square feet
# Create a program that ask the user to enter the total square feet in
# A tract of land and calculates the the number of acres in the tract

square_feet = int(input("Enter the total square feet in the tract of land: "))
number_of_acres = square_feet/43560
print(f'The number of acres in the tract, {number_of_acres}')
