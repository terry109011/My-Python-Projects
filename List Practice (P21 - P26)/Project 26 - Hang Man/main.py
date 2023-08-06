# Hang Man Game 

# Step 1: Select a random word from the list provided
# Step 2: Display game interface
# Step 3: Ask user for input
# Step 4: Match input with letters in the selected word
    # Step 4.1: If correct, fill in the blank
    # Step 4.2: If incorrect, fill the hang man
# Step 5: Ask user for the next input, repeat Step 4
# Step 6: Check if hang man or the selected word has been completed
# Step 7: Ask user if they want to restart the game
    
from ascii_art import hang_man_stages, logo
from my_list import word_list
import os
import random

end_game = False
while not end_game:
    selected_word = random.choice(word_list)
    already_guessed = []
    guess_blank = ['_'] * len(selected_word)
    guess_fill = guess_blank[:]
    guess_blank_str = ' '.join(guess_blank)
    
    print(logo)
    print(f"There are {len(selected_word)} letters in the secret word.")
    print(guess_blank_str)
    print(hang_man_stages[0])
    limit = 6
    count = 0

    while not end_game:       
        user_guess = input('Enter a guess: ').upper()
        os.system('cls') # clearing the screen
        if len(user_guess) == 1:
            if user_guess.isalpha() == True:

                if user_guess in already_guessed:
                    print(f'You have already guessed letter {user_guess}')
                    print(' '.join(guess_fill))
                    print(hang_man_stages[count])
                    continue
                else:
                    already_guessed += user_guess

                if user_guess in selected_word:
                    num = selected_word.count(user_guess)
                    # if there are more than 1 letter in the selected word
                    for i in range(1, len(selected_word) + 1):
                        # return indices of duplicate element
                        if selected_word[i - 1] == user_guess:
                            guess_fill[i - 1] = user_guess
                    print("There are {number} letter {guessed_letter} in the secret word.".format(number = num, guessed_letter = user_guess))
                    print(" ".join(guess_fill))
                    print(hang_man_stages[count])
                    if '_' not in guess_fill:
                        print('You Win! Congratulation')

                else:                        
                    count += 1  
                    print("Wrong guess. " + str(limit - count) + " guesses remaining")
                    print(" ".join(guess_fill))
                    print(hang_man_stages[count])
                    if count < 6:
                        continue
                    else:
                        print('You Lose!')

                if count == 6 or '_' not in guess_fill:
                    print(f"The secret word is {selected_word}")
                    option = ['Y','y','N','n']
                    restart = input("Do you want to play again? 'Y' or 'N' ")
                    while restart not in option:
                        restart = input("Do you want to play again? 'Y' or 'N' ")
                    if restart == option[0] or restart == option[1]:
                        os.system('cls')
                        break # break the inner loop                       
                    else:
                        print('See you later! ')
                        end_game = True

            else: # Input is not a letter
                print('Single letter input only, please try again!')
                print(" ".join(guess_fill))
                print(hang_man_stages[count])
                continue

        else: # Input length is longer than 1 character
            print('Single letter input only, please try again!')
            print(" ".join(guess_fill))
            print(hang_man_stages[count])
            continue