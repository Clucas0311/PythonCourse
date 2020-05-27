# Moving items from one list to another 

# Start with users that need to be verified users of a website
# and an empty list to hold confirm users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = [] # Create an empty list to hold confirmed users

# Verify each user until there are no more uncomfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users: # While loop will run as long as the unconfirmed_users list is not empty
    current_user = unconfirmed_users.pop() # removes items from the end and will add it to current_user list

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

    # Displaying all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
