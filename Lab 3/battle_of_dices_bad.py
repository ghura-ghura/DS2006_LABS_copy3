import random
import re
import os

valid_inputs = ["y", "Y", "yes", "Yes", "YES", "", ]

def roll_x_dices(x, sides = 6):
    """ Rolls x dices with y sides """
    rolls = []
    for i in range(x):
        rolls.append(random.randint(1, sides))
    return rolls

def should_play_again():
    """ Checks if the user wants to play again """
    inp = input("Do you want to play again? (y/n): ")
    return inp in valid_inputs

def clear_console():
    """ Clears the terminal for Windows and Linux systems """
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    """ Main function """
    clear_console()

    rolls = roll_x_dices(2, 20)
    player1_roll, player2_roll = rolls[0], rolls[1]

    players = ["Player 1", "Player 2"]
    scores = {}

    for player in players:
        scores[player] = 0

    winner = ""
    curr_round = 0

    if player1_roll > player2_roll: 
        winner = players[0]
        scores[players[0]] += 1
    elif player1_roll < player2_roll: 
        winner = players[1]
        scores[players[1]] += 1
    else: winner = "Tie"

    curr_round += 1

    round_str = 'round ' + str(curr_round)

    print(f"{ winner + ' wins ' + round_str + '!' if winner != 'Tie' else 'Amaaazzinng! ' + round_str + ' is a tie!' }")
    if winner != "Tie":
        print(f"{ 'Because ' + str(player1_roll) + ' is greater than ' + str(player2_roll) }")
    print("Current score:", re.sub(r"{|}|'", "", str(scores)))

    base_score_message = "Unbelievable! Player X has without a doubt earned the title of Champion of the Battle of Dices! "

    if scores[players[0]] == 3:
        print(base_score_message.replace("X", players[0]))
    elif scores[players[1]] == 3:
        print(base_score_message.replace("X", players[1]))
    else:
        print("This heated Battle of Dices is still going on! Who will be crowned the Champion of the Battle of Dices? ")

    if should_play_again():
        game()
    else:
        print("Game over!")
        print("The Champion of the Battle of Dices is:", players[0] if scores[players[0]] > scores[players[1]] else players[1])
        
if __name__ == "__main__":
    game()
