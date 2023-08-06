# Write another program that prompts for a list of numbers as we did in previous exercises and at the end prints out both the maximum and minimum of the inputted numbers.

# For Example:

# Enter a number: 1
# Enter a number: 3
# Enter a number: 2
# Enter a number: 4
# Enter a number: done

# Output:
# Maximum number: 4.0, Minimum number: 1.0

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

num_lst = []
inp = input('Enter a number: ')

# first input cannot be 'done' because this would result in a bug with num_lst
if inp == 'done':
        print('First input must be a number')
        quit()
        
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    num = check_for_float(inp)
    if num == False: # or (if not num:)
        continue
    num_lst.append(num)

# initialise min and max
my_max = num_lst[1]
my_min = num_lst[1]
for element in num_lst:
    if element > my_max:
        my_max = element
    if element < my_min: 
        my_min = element
    
print(f'Max = {my_max}\nMin = {my_min}')