
def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    return result

no1 = int(input('What is the first number? '))
no2 = int(input('What is the second number? '))
opt = input('Pick operation from this list (+,-,*,/) ')
output = calculator(no1, no2, opt)
print(f'{no1} {opt} {no2} = {output}')