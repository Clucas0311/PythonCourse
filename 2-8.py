# Ask the user input for the total price for the food
cost_of_food = float(input("How much does the total bill cost: "))
tip_percentage = .18 * cost_of_food
sales_tax = .07 * cost_of_food


total = cost_of_food + tip_percentage + sales_tax

print(f"""The cost of the bill: ${cost_of_food:.2f} with an 18 % percent
{tip_percentage}%, and the sales tax {sales_tax:.1f}%. The total cost comes out to be
${total:.2f}""")
