import random
import math
    
while True:
    try:
        lower = int(input('Enter lower bound: '))
        upper = int(input('Enter upper bound: '))
        break
    except ValueError:
        print('Numeric input only!')
        continue
    
number_of_chances = int(math.log(upper - lower + 1, 2))
print(f'\n\tYou have {number_of_chances} chances to guess the integer!\n')

secret_num = random.randint(lower, upper)
    
num_guesses = 0
while num_guesses < number_of_chances:
    num_guesses += 1
    guess = int(input('Guess a number: '))
    if secret_num == guess:
        print(f'Well done! you did it in {num_guesses} try!')
    if guess > secret_num:
        print('Your guess is too high!')
    elif guess < secret_num:
        print('Your guess is too low!')
        
print(f'\nThe number is {secret_num}!')
print('\tBetter luck next time!')

        