# Ask the user for the amount of the item purchased
amount_of_purchase = float(input("How much does item cost?: "))

# Assume sales tax is 5 percent
sales_tax = 0.05 * amount_of_purchase

# Assume the county sales tax is 2.5 percent
county_sales_tax = 0.025 * amount_of_purchase

# The program should display the amount of purchase, the state sales tax
# the county sales tax and the total of the sales

total_of_purchase = amount_of_purchase + sales_tax + county_sales_tax

print(f"""The total purchase of the item ${amount_of_purchase},
The state sales tax is ${sales_tax}, and the county sales tax is
{county_sales_tax}. The total price for the sale is ${total_of_purchase}""")
