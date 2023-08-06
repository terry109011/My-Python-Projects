import random

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(f'Dice 1: {num1}', f'\nDice 2: {num2}')
inp = input('Roll the dice again? Y/N ')

while True:
    if inp == 'Y':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f'Dice 1: {num1}\nDice 2: {num2}')
        inp = input('Roll the dice again? Y/N ')
    if inp == 'N':
        quit()
