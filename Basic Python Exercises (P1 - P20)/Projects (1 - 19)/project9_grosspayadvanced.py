# ask user for input
try:
    hours = float(input('Enter hours: '))
    rates = float(input('Enter rates: '))
except ValueError:
    print('Numerical inputs only.')
    quit()

if hours > 0 and hours <= 40:
    grosspay = hours*rates
else:
    overtime = hours - 40
    grosspay = rates*(40 + 1.5*overtime)
print(f'Your total pay is ${grosspay}.')