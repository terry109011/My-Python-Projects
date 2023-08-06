# Part 4 - Celsius to Fahrenheit

while True:
    try:
        cel = float(input('Enter temperature in Celsius: '))        
        fah = (cel*(9/5)) + 32
        print(f'{cel} Celsius = {fah} Fahrenheit')
        print(20*'-')
        break
    except ValueError:
        print('Numerical input only. Please try again.')
        continue
    

