# from random import random

# def flip_coin():
# 	# generate random number 0-1
	
# 	if random() > 0.5: 
# 		return "Heads"
# 	else: 
# 		return "Tails"


def letter_check(word, letter): 
  for character in word:
  	if word == letter: 
  		return True 
  	return False 

print(letter_check("strawberry", 'a'))
# print(flip_coin())