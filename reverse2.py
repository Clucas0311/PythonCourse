message = "What's in your wonderball, totally exciting, RACECAR"

backwards = ""

i = len(message) - 1
while i >= 0:
    backwards += message[i]
    i = i - 1

print(backwards)
