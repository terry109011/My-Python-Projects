# Implement a function that takes an integer number as a parameter and returns factorial of this number.
# Factorial Equation (!)
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 4! = 4 x 3 x 2 x 1 = 24
# If input is 0 then the return value will be: The factorial of 0 is 1
# if input is a negative number then the return value will be: Factorial does not exist for negative numbers

# Example
# factorial(4) # The factorial of 4 is 24
# factorial(-1)  # Factorial does not exist for negative numbers

def factorial(p_num):
    if p_num < 0:
        print('Factorial does not exist for negative numbers')
    elif p_num == 0:
        print('The factorial of 0 is 1')
    else:
        my_fac = 1
        for i in range(1, p_num + 1):
            my_fac *= i
        print(f'The factorial of {p_num} is: {my_fac}')
        return my_fac


def check_val(input):
    try:
        val = int(input)
        return val
    except ValueError:
        print('Error, please enter numeric input')
        return False
        

num = input('Enter a number: ')
num = check_val(num)

while num == False:
    num = input('Enter a number: ')
    num = check_val(num)
    
output = factorial(num)


    

