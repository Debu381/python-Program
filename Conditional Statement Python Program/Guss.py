#write a python program to guess a number between 1 to 9

import random
target_num, guess_num=random.randint(1,10), 0
while target_num !=guess_num:
    guess_num=int(input('Guess a number'))

print('Well guessed')