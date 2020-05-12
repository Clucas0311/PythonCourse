# Vineyard calculation:
# V =( R - 2E) / S
# V = the number of grapevines that will fit in the row
# R is the length of the row in feet
# E is the amount of Space in feet used by an end-post assembly
# S is the space between vines, in feet

# Write a program that makes calculations for the vineyard owner

# Prompt the user for the length of the row in ft?
length_of_row = float(input("What is the length of the row, in feet?: "))
amount_space_end = float(input("What is the amount of space used, in feet by \
an end assembly: "))
amt_btwn_vine = float(input("Enter the amount of space between vines,\
 in feet: "))
 
# Calculation of the grapevines throuh user data
grapevines = (length_of_row - (2 * amount_space_end)) / (amt_btwn_vine)

# Display data on screen
print(f"The number of grapevines that will fit in a row: {grapevines:.2f}")
