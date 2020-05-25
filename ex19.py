def cheese_and_crackers(cheese_count, boxes_of_crackers): # Created a function with two parameters
    print(f"You have {cheese_count} cheeses!") # Created a string using the cheese parameters
    print(f"You have {boxes_of_crackers} boxes of crackers!") # Created a parameter with the boxes parameter
    print("Man that's enough for a party!") # Extra string in the function
    print("Get a blanket. \n") # Creates another string with the new line character


print("We can just give the function numbers directly:") # Print a string about
#how to use a function by directly putting numbers in place inside the function
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:") # Created variables and use the variables as parameters
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:") # Shows how we can add numbers in each parameter location
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two variables and math:") # Shows how we can add more value to the variables created in the paramter location 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
