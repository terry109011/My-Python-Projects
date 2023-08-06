# Project 29 - Quiz App

from ascii_art import logo
from questions import quiz
import os

# Function to check answer
def check_answer(question_num, answer, attempts, player):
    os.system('cls')
    if answer.lower() == quiz[question_num]["answer"].lower():
        print(f"Correct Answer!\n{player}'s score is {players_score[player] + 1}")
        return True
    else:
        print("Incorrect Answer!")
        print(f"")
        print(f"You have {attempts - 1} attempts left.")
        return False
    
# Function to switch player
def switch_player(current_player_index):
    if current_player_index == 0:
        return 1
    return 0

print(logo)

print("There are 6 questions in total. You can skip a question anytime by entering 'skip'.")
input("Press any key to continue...")
player1 = input('Enter player 1 name: ')
player2 = input('Enter player 2 name: ')
player_list = [player1, player2]
players_score = dict.fromkeys(player_list, 0)
current_player = player_list[0]

for question in quiz: # keys [1 2 3 4 5 6]
    print("----------------------------------------------------")
    print(f"It is {current_player}'s turn.")
    attempts = 2
    score = players_score[current_player]
    while attempts > 0:
        print(quiz[question]["question"])
        answer = input("Enter Answer (To move to the next question, type 'skip'): ")
        if answer == "skip":
            break
        check = check_answer(question, answer, attempts, current_player)
        if check == True:
            players_score[current_player] += 1
            break
        attempts -= 1
    current_player_index = player_list.index(current_player)
    next_player_index = switch_player(current_player_index)
    current_player = player_list[next_player_index]