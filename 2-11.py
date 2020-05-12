# Write a program that ask the user for the number of males and females
# Registered in class. The program should display the percentages of females of
# Males and females in the class

# Prompt User for amount of males in the class:
num_of_males = int(input("How many males are in your class: "))

# Prompt User for amount of males in the class:
num_of_females = int(input("How many females are in your class: "))

total_classmates = num_of_males + num_of_females
# Caluclate the percentage
percentage_of_male = (num_of_males / total_classmates) * 100
percentage_of_females = (num_of_females / total_classmates) * 100

# Print statement
print(f"""There are {percentage_of_male:.1f}% of males, and
{percentage_of_females:.1f}% of females in the class.""")
