"""Write a code that asks the user to input a number between 1 and 5 inclusive. The code will take
the integer value and print out the string value. So for example if the user inputs 2 and the code will
print two. Reject any input that is not in not a number in that range"""

secret_number = 5
guess = input("Guess the number between 1-10:  ")
if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print("You've guessed correctly")
    elif guess > secret_number and guess <= 10:
        print("You've guessed too high!. Sorry you lose")
    elif guess < secret_number and guess >= 1:
        print("You guessed too low. Sorry you lose")
else:
    print("That's not an interger! What are you playing at??!")
