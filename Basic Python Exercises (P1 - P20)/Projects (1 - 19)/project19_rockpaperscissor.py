import random

options = ['rock','paper','scissor']

while True:
    choice = input('Enter a choice (rock, paper, scissor): ')
    comp_choice = random.choice(options)
    if choice == comp_choice:
        print(comp_choice)
        print('Draw ')
    elif choice == 'rock':
        print(comp_choice)
        if comp_choice == 'scissor':
            print('Rock beats scissor. You win! ')
        else: 
            print('Paper beats rock. You lose! ')
    elif choice == 'paper':
        print(comp_choice)
        if comp_choice == 'rock':
            print('Paper beats rock. You win! ')
        else:
            print('Scissor beats paper. You lose! ')
    elif choice == 'scissor':
        print(comp_choice)
        if comp_choice == 'rock':
            print('Rock beats scissor. You lose! ')
        else:
            print('Scissor beats paper. You win! ')
    else:
        print('Invalid input, please try again')
        continue
    
    play_again = input('Play again Y/N? ')
    if play_again == 'Y':
        continue
    if play_again == 'N':
        quit()
    else:
        print('See you later!')
        quit()