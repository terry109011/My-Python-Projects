# Bill Roulette

# Instruction:
# Create a program which which asks for names and select random name
# from the list of names. The person selected will have to pay for everybody's food bill.

# Example Input:
# Elshad, Edy, Redy, John, Jenny

# Example Output:
# Edy is going to pay for the meal today!

# Hint:
# Use split() function to convert string to list.

# ---------------------------------------------------------------------------------------
import random

# VERSION 1 - without using split()
# name_list = []
# prompt user's input
# while True:
#     name = input('Enter name: ')
#     if name == 'done':
#         print(name_list)
#         break
#     else:
#         name_list.append(name)
        
# index = random.randint(0, len(name_list) - 1)
# chosen = name_list[index]
# print(f'{chosen} is going to pay for the meal today!')


# VERSION 2 - use split()
name = input('Enter names, separated by a comma: \n')
name_list = name.split(',')
print(name_list)
index = random.randint(0, len(name_list) - 1)
chosen = name_list[index]
print(f'{chosen} is going to pay for the meal today!')


    
        