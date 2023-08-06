# Write a program which repeatedly reads numbers until the user enters "done". Once “done” is entered, print out the total, count, and average of the numbers.

# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Step 1 - Create a function which checks for numbers using try and except block.

# Step 2 - Inside while loop ask for input

# Step 3 - Calculate count, sum and average

# Enter a number: 2
# Enter a number: 4
# Enter a number: six
# Error, please enter numeric input
# Enter a number: 6
# Enter a number: done
# 12.0 3 4.0


# check the user's input
def check_val(input):
    try:
        val = int(input)
        return val
    except ValueError:
        print('Error, please enter a numeric input')
        return False
    
count = 0 # initialise counter
my_sum = 0 # initialise sum
my_average = 0 # initialise average

# Prompt the user for input until the user typed 'done'
while True:    
    inp = input('Please enter a number: ')
    if inp == 'done':
        break
    num = check_val(inp)
    if not num: # if num is False
        continue # this means ignore the rest of the loop and start over again    
    count += 1
    my_sum += num
    
if count != 0:
    my_average = my_sum / count     
print(f'Sum = {my_sum}   Count = {count}   Average = {my_average}')
