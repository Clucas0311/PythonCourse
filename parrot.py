prompt = "\n Tell me something, and I will repeat it back to you: "
prompt += "\n Enter 'quit' to end the program.  "

active = True # This is a flag variable for a while loop when we have multiple conditions that need to be tested
while active:
    message = input(prompt)

    if message == 'quit':
        active = False # Set active to False to exit out of the loop
    else:
        print(message)
