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

def flatten(list_arr):
    flat_list = []

    for item in list_arr:
        if isinstance(item, list):
            flat_list.extend(item)
        elif isinstance(item, int):
            flat_list.append(item)

    return flat_list

def log_player_rolls(player1_rolls, player2_rolls, max_rounds):
    player2_col = "| Player 2 |"
    player1_col = "| Player 1 |"
    rounds_col = "| Round    |"
    
    for round in range(1, max_rounds + 1):
        rounds_col += f"{round}|"

    for roll in player1_rolls:
        player1_col += f"{roll}|"

    for roll in player2_rolls:
        player2_col += f"{roll}|"

    print("________________________________________________________")
    print(rounds_col)
    print(player1_col)
    print(player2_col)
    print("________________________________________________________")

def game(player1_roll1, player2_roll1, player1_roll2, player2_roll2, player1_roll3, player2_roll3, curr_round, max_rounds, sides):
    """ Main function """
    clear_console()

    curr_player1_roll = roll_x_dices(1, sides)
    curr_player2_roll = roll_x_dices(1, sides)

    match curr_round:
        case 1:
            player1_roll1 = curr_player1_roll
            player2_roll1 = curr_player2_roll
        case 2:
            player1_roll2 = curr_player1_roll
            player2_roll2 = curr_player2_roll
        case 3:
            player1_roll3 = curr_player1_roll
            player2_roll3 = curr_player2_roll

    players = ["Player 1", "Player 2"]
    scores = {}

    for player in players:
        scores[player] = 0

    winner = ""
   
    if curr_player1_roll > curr_player2_roll: 
        winner = players[0]
        scores[players[0]] += 1
    elif curr_player1_roll < curr_player2_roll: 
        winner = players[1]
        scores[players[1]] += 1
    else: winner = "Tie"

    round_str = 'round ' + str(curr_round)

    print(f"{ winner + ' wins ' + round_str + '!' if winner != 'Tie' else 'Amaaazzinng! ' + round_str + ' is a tie!' }")
    if winner != "Tie":
        print(f"{ 'Because ' + str(curr_player1_roll) + ' is greater than ' + str(curr_player2_roll) }")
    print("Current score:", re.sub(r"{|}|'", "", str(scores)))

    base_score_message = "Unbelievable! Player X has without a doubt earned the title of Champion of the Battle of Dices! "

    if scores[players[0]] == 3:
        print(base_score_message.replace("X", players[0]))
    elif scores[players[1]] == 3:
        print(base_score_message.replace("X", players[1]))
    else:
        print("This heated Battle of Dices is still going on! Who will be crowned the Champion of the Battle of Dices? ")

    if curr_round < max_rounds and should_play_again():
        curr_round += 1
        game(player1_roll1, player2_roll1, player1_roll2, player2_roll2, player1_roll3, player2_roll3, curr_round, max_rounds, sides)
    else:
        print("Game over!")
        print("The Champion of the Battle of Dices is:", players[0] if scores[players[0]] > scores[players[1]] else players[1])
        player1_rolls = flatten([player1_roll1, player1_roll2, player1_roll3])
        player2_rolls = flatten([player2_roll1, player2_roll2, player2_roll3])
        log_player_rolls(player1_rolls, player2_rolls, max_rounds)

    curr_round += 1

player1_roll1 = 0
player2_roll1 = 0
player1_roll2 = 0
player2_roll2 = 0
player1_roll3 = 0
player2_roll3 = 0
curr_round = 1
max_rounds = 3
sides = 6

if __name__ == "__main__":
    game(player1_roll1, player2_roll1, player1_roll2, player2_roll2, player1_roll3, player2_roll3, curr_round, max_rounds, sides)
