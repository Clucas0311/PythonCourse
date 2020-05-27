# A movie theater charges different ticket from prices depending on a person's
# age. If a person is under the age of 3 the ticket is free; if they are
# between 3 and 12, the ticket is $10; and the if they are over the age 12, the
# ticket is 15. Write a loop in which you ask users thier age, and then tell them
# the cost of their movie ticket

age = """\nHello, welcome to Movie theater, first I need to know your age
So I can determine the cost of your ticket, how old are you?: """
while True:
    ask_age = input(age)
    ask_age = int(ask_age)
    if ask_age < 3:
        print(f"You're {ask_age} years old, your ticket is free, Enjoy!")
        break
    elif ask_age >= 3 and ask_age <= 12:
        print(f"""You're {ask_age} years old. You're older than 3 but younger than
12 your ticket will cost $10""")
        break
    else:
        print(f"You're {ask_age} years old. You're above 12 your ticket cost $15" )
        break
