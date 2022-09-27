# import random
#
# rock = 'Rock'
# paper = 'Paper'
# scissors = 'Scissors'
# lizard = 'Lizard'
# spock = 'Spock'
#
# player_move = input("Choose [r]ock, [s]cissors, [p]aper, [l]izard or [sp]ock: ")
# if player_move == 'r':
#     player_move = rock
# elif player_move == 's':
#     player_move = scissors
# elif player_move == "p":
#     player_move = paper
# elif player_move == "l":
#     player_move = lizard
# elif player_move == "sp":
#     player_move = spock
# else:
#     raise SystemExit('Invalid Input. Tray again...')
#
# computer_random_number = random.randint(1, 5)
# computer_move = ''
#
# if computer_random_number == 1:
#     computer_move = rock
# elif computer_random_number == 2:
#     computer_move = scissors
# elif computer_random_number == 3:
#     computer_move = paper
# elif computer_random_number == 4:
#     computer_move = lizard
# else:
#     computer_move = spock
#
# print(f"The computer chose {computer_move}.")
#
# if (player_move == rock and (computer_move == scissors or computer_move == lizard)) or \
#         (player_move == paper and (computer_move == rock or computer_move == spock)) or \
#         (player_move == scissors and (computer_move == paper or computer_move == lizard)) or \
#         (player_move == lizard and (computer_move == paper or computer_move == spock)) or \
#         (player_move == spock and (computer_move == scissors or computer_move == rock)):
#
#     print('You win!')
# elif player_move == computer_move:
#     print('Draw!')
# else:
#     print('You lose!')

import random
import time


def game(player, computer):
    machine = 0
    human = 0
    if player == 'S' and computer == 'P' or player == 'P' and computer == 'R' or player == 'R' and computer == 'S':
        human += 1
        time.sleep(0.5)
        print('Player win this round!')
        one_more_game = next_game()
        return human, machine, one_more_game
    else:
        machine += 1
        time.sleep(0.5)
        print('Computer win this round!')
        one_more_game = next_game()
        return human, machine, one_more_game


def next_game():
    while True:
        time.sleep(0.2)
        question = input('Another game ? Y/N : ').upper()
        if question == 'Y':
            return True
        elif question == 'N':
            return False
        else:
            time.sleep(0.5)
            print('Invalid answer!')
            continue


moves = ['P', 'R', 'S']
print("Hello, to my first  small game!")
print("Rock, Paper, Scissors!")
name_input = input("Please enter your name: ")
print(f'{name_input}, do you wanna play a game?')

player_scores = 0
computer_scores = 0
another_game = True
while another_game is not False:
    answer = input(f'Y or N: ').upper()
    if answer != 'N' and answer != 'Y':
        print('Invalid input. Try again!')
        continue
    elif answer == 'N':
        print(f'Good bye, {name_input}!')
        time.sleep(0.3)
        print('GAME OVER')
        another_game = False
    elif answer == 'Y':
        print(f'{name_input}, welcome!')

        while True:
            player_move = input('(P)-Paper, (R)-Rock, (S)-Scissors, your choice: ').upper()
            if player_move not in moves:
                print(f'Invalid, input {name_input}. Please choose, one of shown examples!')
                continue
            time.sleep(0.5)
            print(f'Player, choice is: {player_move}')
            computer_move = random.choice(moves)
            time.sleep(0.5)
            print(f'Computer, choice is: {computer_move}')
            if player_move == computer_move:
                time.sleep(0.5)
                print('Draw!')
                another_game = next_game()
                if another_game is False:
                    break
            else:
                result = game(player_move, computer_move)
                player_scores += result[0]
                computer_scores += result[1]
                another_game = result[2]
                if another_game is False:
                    break
time.sleep(0.3)
print(f'Player scores: {player_scores}.')
print(f'Computer scores: {computer_scores}.')
time.sleep(0.3)
if player_scores > computer_scores:
    print('Player win THE GAME!')
elif player_scores < computer_scores:
    print('Computer win THE GAME!')
else:
    print('Equal scores, we don`t have Winner!')
time.sleep(0.3)
print(f"Bye, bye, {name_input}!")
print('GAME   OVER')
