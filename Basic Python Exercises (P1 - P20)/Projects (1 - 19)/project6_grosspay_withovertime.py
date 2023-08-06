# Project 6 - Gross Pay with Overtime

hours = float(input('Enter hours: '))
rates = float(input('Enter rates: '))
overtime = hours - 40

if hours > 40:
    salary = round(rates*(40 + 1.5*overtime),2)
else:
    salary = round(hours*rates,2)
print(f'Total pay is ${salary}')
    