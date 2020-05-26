# Write a loop that prompts the user to enter a series of pizza toppings until
# they enter a "quit" value. As they enter each message, print a message saying
# You'll add that topping to their pizza

message = """\nWelcome to Pizza Shack!
What kind of toppings would you like to add to your pizza?:"""
message += "\n Enter 'quit' if you would like to leave the program: "

while True:
    toppings = input(message)

    if toppings == 'quit':
        break

    else:
        print(f"We will add {toppings} to your pizza. Enjoy!")
