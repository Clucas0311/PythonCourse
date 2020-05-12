item_1 = float(input("What is the amount for this item?:  "))
item_2 = float(input("What is the amount for this item?:  "))
item_3 = float(input("What is the amount for this item?:  "))
item_4 = float(input("What is the amount for this item?:  "))
item_5 = float(input("What is the amount for this item?:  "))

subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = 0.07 * subtotal 
total = subtotal + sales_tax

print(f"The subtotal of the shopping cart is ${total}")
