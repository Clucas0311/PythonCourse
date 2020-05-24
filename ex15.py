from sys import argv

script, filename = argv # used argv to get the filename

txt = open(filename) # opens the file by the name

print(f"Here's your file {filename}:")
print(txt.read())

# print("Type the filename again:")
# file_again = input('> ')
#
# txt_again = open(file_again)
#
# print(txt_again.read())
