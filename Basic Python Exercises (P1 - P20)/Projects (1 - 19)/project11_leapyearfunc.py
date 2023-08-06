# Project 11 - Leap year with function

# function to check leap year
def leap_year(p_year):
    if p_year % 4 == 0:
        if p_year % 100 != 0:
            print(f'{p_year} is a leap year.')
        else:
            if p_year % 400 == 0:
                print(f'{p_year} is a leap year.')
            else:
                print(f'{p_year} is not a leap year.')
    else:
        print(f'{p_year} is not a leap year.')
        
# ask user for input
while True:
    try:
        year = int(input('Enter year: '))
        if year > 0:
            leap_year(year)
            break
        else:
            print('Positive value only. Try again.')
    except ValueError:
        print('Numerical value only. Please try again.')
        continue