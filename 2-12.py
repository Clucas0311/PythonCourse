# Joe purchased stock in Acme Software Inc here is the details:
# Number of shares Joe purchased 2,000
# When Joe purchased the stock he paid $40.00 per share
# Joe paid his stockbroker a commison that amounted to 3 percent of the amount
# he paid for stock

# Joe sold the stock two weeks later:
# The number of shares sold was 2,000
# He sold the $42.75 per share
# He paid his stockbroker another commision that amounted to 3 percent of the
# amount he recieved for the stock.
amount_paid = 2000
amount_paid_per_share = 40.00
amount_for_stock = amount_paid * amount_paid_per_share
amount_paid_to_broker =  0.03 * amount_for_stock

amount_stock_was_sold = 42.75 * amount_paid
amount_sold_comission = 0.03 * amount_stock_was_sold
profit = (amount_stock_was_sold - amount_sold_comission) - \
(amount_for_stock - amount_paid_to_broker)

print(f"""Amount paid for stock: ${amount_for_stock:,.2f}
Amount received for stock: ${amount_stock_was_sold:,.2f}
Commission for selling: ${amount_sold_comission:,.2f}
Commission for purchasing: ${amount_paid_to_broker:,.2f}
Profit: ${profit:.2f}. The profit margin is postitive, so Joe made a profit
""")
