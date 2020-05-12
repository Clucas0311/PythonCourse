# The program should ask the user to enter the temperature in Celcius
temp_in_celcius = float(input("Please enter the temperature in celcius: "))

# Then display the temperature in Fahrenheit
 # Formula (9/5)(Celcius) + 32
temp_in_farenheit = ((9/5)*temp_in_celcius) + 32
print(f'The temperature in Fahrenheit is: {temp_in_farenheit:.1f}F')
