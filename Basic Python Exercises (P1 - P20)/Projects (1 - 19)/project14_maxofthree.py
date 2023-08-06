# Project 14 - Maximum of Three numbers

# Find the max of the first 2 numbers, then compare the output to the third number
def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    return n2

def max_of_three(n1, n2, n3):
    old_max = max_of_two(n1, n2)
    new_max = max_of_two(old_max, n3)
    return new_max

# prompt inputs from user
while True:
    try: 
        n1 = int(input('Enter first number: '))
        n2 = int(input('Enter second number: '))
        n3 = int(input('Enter third number: '))
        my_max = max_of_three(n1, n2, n3)
        print(f'The maximum number is: {my_max}')
        break
    except ValueError:
        print('Numerical Inputs only, please try again')
        continue
    
    