# Password generator

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

password = ''

while True:
    try:
        inp_letter = int(input('How many letters do you want in your password? '))
        inp_num = int(input('How many numbers do you want in your password? '))
        inp_sym = int(input('How many symbols do you want in your password? '))
    except ValueError:
        print('Numeric input only! Try again!')
        continue
    else:
        break
    
# generate password (but unshuffle)
for i in range(1, inp_letter + 1):
    password += random.choice(letters)
    
for j in range(1, inp_num + 1):
    password += random.choice(nums)
        
for k in range(1, inp_sym + 1):
    password += random.choice(symbols)

print(f'Your password is: {password}')

# shuffle password
# separate the password string into a list, then shuffle the list
pass_list = list(password) # convert string into a list

# IMPORTANT: do not put this in a variable as it will be recognised as None
random.shuffle(pass_list) # shuffle the list

advanced_password = ''
for element in pass_list:
    advanced_password += element
    
print(f'Your advanced password is: {advanced_password}')




