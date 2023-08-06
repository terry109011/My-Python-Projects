# Project 13 - Cold, Warm, Hot

# define the function
def temp(my_temp):
    if my_temp > 28:
        return 'Hot'
    elif my_temp <= 28 and temp >= 18:
        return 'Warm'
    else:
        return 'Cold'

# prompt input from user
while True:
    try:
        my_temp = float(input('Enter temperature: '))
        print(temp(my_temp))
        break
    except ValueError:
        print('Numeric value only, please try again.')
        continue