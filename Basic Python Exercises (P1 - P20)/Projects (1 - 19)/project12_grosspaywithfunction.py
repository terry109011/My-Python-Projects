# Project 12 - Gross Pay with Functions

def compute_pay(hours, rates):   
    if hours > 40:
        overtime = hours - 40
        salary = round(rates*(40 + 1.5*overtime), 2)
    else:
        salary = round(hours*rates,2)
        return salary

def isfloat(input):
    try:
        val = float(input)
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()



my_hours = input('Enter hours: ')
my_hours = isfloat(my_hours)
my_rates = input('Enter rates: ')
my_rates = isfloat(my_rates)

output = compute_pay(my_hours, my_rates)

print(f'Total pay: ${output}')
