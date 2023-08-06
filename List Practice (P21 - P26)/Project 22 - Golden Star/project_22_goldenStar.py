# Golden Star
# Problem prompt: https://replit.com/@AppMillers/Project-22-Find-the-Golden-Star#Readme.md

import random
def print_map(p_map):
    print('\n'.join([' '.join(['{0:<6.2}'.format(item) for item in row]) for row in p_map]))

map = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map)
print()

# 3x3 map
num_row = len(map)
num_col = len(map[0])

# Place a star at a random position
star_row = random.randint(0, num_row - 1)   # access row
star_col = random.randint(0, num_col - 1)   # access column
map[star_row][star_col] = '⭐'
star_pos = str(star_row) +  str(star_col)

# Map user's input to thecorresponding coordinate on the map
while True:
    try:
        position = input('Enter your guess, where is the golden star on the map? ')
        row_input = int(position[0])
        col_input = int(position[1])
        if (row_input > 2 or row_input < 0) or (col_input > 2 or col_input < 0):
            print('The position index for row or column is between 0 and 2. Please try again!')    
            continue    
        else:
            row_str = str(row_input) # convert row index to string format (user's input)
            col_str = str(col_input) # convert column index to string format (user's input)
            guess = row_str + col_str 
            # Match user's input with the star position
            if guess == star_pos:
                print_map(map)
                print('Congratulation! Your guess is correct')
            else:
                print('Oops! Incorrect')
                map[row_input][col_input] = '❌'
                print_map(map)
            break
    except ValueError or TypeError:
        print('Positive integer only! Please try again!')
        continue

