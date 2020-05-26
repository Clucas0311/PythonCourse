#Reverse cipher

message = "Three can keep a secret, if two of them are dead."
translated = ''

i = len(message) - 1 # so you get the the len of the message variable decrement
# it then add it to translation variable empty string variable it will then loop
while i >= 0: # while i is greater or less than zero it will loop until it finishes
    translated += message[i] # last index is the character 
    i = i - 1 # will decrement until i is less than zero loop will end ß

print(translated)
