# Create a variable for projected_sales
# Create a float variable for projected sales
# projeceted amount equals totals sales * 0.23
# Ask the user for the totals sales

total_sales = input("Please enter the total sales for this period: ")
total_sales = float(total_sales)
projected_sales = total_sales * 0.23

print(f"The amount of profit you made was ${projected_sales}")
