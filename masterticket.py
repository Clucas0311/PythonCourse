SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

# Create calculate price function. It takes number of tickets and returns
# num_tickets * TICKET_PRICE
def calculate_price(ticket_amount): 
  # Add the service charge to our result
  return (ticket_amount * TICKET_PRICE) + SERVICE_CHARGE

#Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
  # Output how many tickets are remaining using the tickets_remaining variable
  print(f"There are {tickets_remaining} tickets remaining")
  
  #Gather the user's name and assign it to a new variable
  user_name = input("Hello, may I please have your name: ")
  
  #Prompt the user by name and ask the user how many tickets would they like

  amount_of_tickets = input(f"Hello {user_name}, how many tickets would you like?: ")
  try: 
     amount_of_tickets = int(amount_of_tickets)
    # Raise a ValueError if the request is for more tickets than requested
     if amount_of_tickets > tickets_remaining:
        raise ValueError(f"They Are only {tickets_remaining}. Please try again")  
  except ValueError as err:
    #Include Error text in the output
      print(f"Oh no we ran into an issue please try again. {err} Thank you" )
  else:
  #Calcuate the price (number of tickets they want) * (ticket_price) and assign it to a variable 
    total_price = calculate_price(amount_of_tickets)
    
    #Output the price to the screen
    print(f"The total price due for all the tickets will be ${total_price}")
    
    #Prompt user if they would like to continue
    confirmation = input("Would you like to continue with your order.   Y/N:  ")
    
    #If they want to proceed
    if confirmation.lower() == "y":
      
      # print out to the screen "SOLD!" to confirm
      print("SOLD!!!!!!!")
      #TODO Gather Credit Card info and process it
          
        # reduce by the tickets remaining 
      tickets_remaining -= amount_of_tickets
      
      #Otherwise... 
    else:    
        # Thank them by name
        print(f"Thanks anyways, {user_name}, Enjoy your day")
  
  # Notify user that the tickets sold 
print(f"Unfortunately, {user_name}, the tickets have sold out. Sorry")