# Project 7 - Leap Year

year = int(input('Enter year: '))

if year % 4 == 0:
    if year % 100 != 0:
        print(f'{year} is a leap year.')
    else:
        if year % 400 == 0:
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
else:
    print(f'{year} is not a leap year.')
