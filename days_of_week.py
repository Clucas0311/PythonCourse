# Collect input from user to pick a number 1-7
number_choice = int(input("Please choose a number between 1-7: "))

#Control flow based on user input:

if number_choice == 1: 
	print("Your day of week is Monday")
elif number_choice == 2: 
	print("Your day of week choice is Tuesday")
elif number_choice == 3: 
	print("Your day of week choice is Wednesday")
elif number_choice == 4: 
	print("Your day of week choice is Thursday")
elif number_choice == 5: 
	print("Your day of week choice is Friday")
elif number_choice == 6: 
	print("Your day of week choice is Saturday")
elif number_choice == 7: 
	print("Your day of week choice is Sunday")
elif number_choice > 7:
	print("Sorry number is too high")
else: 
	print("Sorry number is too low")