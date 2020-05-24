# this one is like your scripts with argv
def print_two(*args): # allows you to create multiple parameters with just the *args function
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# okay, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # Created two parameters
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1): # Created one parameter
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none(): # No parameters
    print("I got nothin'.")


print_two("Charles", "Lucas") # Calling funtions 
print_two_again("Charles", "Lucas")
print_one("First!")
print_none()
