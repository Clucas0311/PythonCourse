# Write a progran that produces 48 cookies with the ingredients listed
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour

regular_amt_cookies = 48
regular_amt_sugar = 1.5
regular_amt_butter = 1
regular_amt_flour = 2.75
 # Prompt the user on how many cookies that they will like to make?
amount_of_cookies = float(input("How many cookies would you like to make?: "))

expected_cups_sugar = (amount_of_cookies / regular_amt_cookies) * \
 regular_amt_flour

expected_cups_butter = (amount_of_cookies / regular_amt_cookies) * \
 regular_amt_sugar

expected_cups_flour = (amount_of_cookies / regular_amt_cookies) * \
regular_amt_flour

print(f"""To make: {amount_of_cookies}, you need: {expected_cups_sugar:.2f} cups
of sugar, {expected_cups_butter:.2f} cups of butter and {expected_cups_flour:.2f}
cups of flour. """)
