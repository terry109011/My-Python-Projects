# Part 3 - Gross Pay

try:
    hours = float(input('Please enter number of hours: '))
    rates = float(input('Please enter your pay rates: '))
except ValueError:
    print('Numerical inputs only, please try again.')
    quit()
    
else:    
    grosspay = hours*rates
    print(f'Total pay is: {grosspay}')
    print(20*'-')