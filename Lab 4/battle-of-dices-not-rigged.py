import re
import os

from dice import roll_d4, roll_d6, roll_d8, roll_d12, roll_d20, roll_d100

def determine_dice_to_use(dice_sides):
    """ Determines the dice to use based on the number of sides """
    if dice_sides <= 4:
        return roll_d4
    if dice_sides <= 6:
        return roll_d6
    if dice_sides <= 8:
        return roll_d8
    if dice_sides <= 12:
        return roll_d12
    if dice_sides <= 20:
        return roll_d20
    return roll_d100

def flatten(list_arr):
    flat_list = []

    for item in list_arr:
        if isinstance(item, list):
            flat_list.extend(item)
        elif isinstance(item, int):
            flat_list.append(item)

    return flat_list

def write_to_file(file_name, content):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)

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

    log = ""
    log += "________________________________________________________\n"
    log += rounds_col + "\n"
    log += player1_col + "\n"
    log += player2_col + "\n"
    log += "________________________________________________________\n"

    print(log)

    should_save_file = input("Do you want to save the game results to a file? (y/n): ")
    if should_save_file == "y":
        file_name = input("Enter the name of the file: ")
        write_to_file(file_name, log)

def roll_x_dices(x, fn = roll_d6):
    """ Rolls x dices with the given function """
    rolls = []
    for _ in range(x):
        rolls.append(fn())
    return rolls

def should_play_again(inputs):
    """ Checks if the user wants to play again """
    inp = input("Do you want to play again? (y/n): ")
    return inp in inputs

def clear_console():
    """ Clears the console """
    os.system('cls' if os.name == 'nt' else 'clear')

def game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use, player1_rolls, player2_rolls):
    """ Plays a single round of the game """
    clear_console()

    player1_roll = roll_x_dices(1, dice_to_use)
    player2_roll = roll_x_dices(1, dice_to_use)

    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)

    updated_scores = curr_scores.copy()
    winner = ""

    if player1_roll > player2_roll:
        winner = player1
        updated_scores[player1] += 1
    elif player1_roll < player2_roll:
        winner = player2
        updated_scores[player2] += 1
    else: winner = "Tie"

    round_str = 'round ' + str(curr_round)

    print(f"{ winner + ' wins ' + round_str + '!' if winner != 'Tie' else 'Amaaazzinng! ' + round_str + ' is a tie!' }")
    print("Current score:", re.sub(r"{|}|'", "", str(updated_scores)))

    base_score_message = "Unbelievable! Player X has without a doubt earned the title of Champion of the Battle of Dices! "

    if updated_scores[player1] >= first_to_reach:
        print(base_score_message.replace("X", player1))
    elif updated_scores[player2] >= first_to_reach:
        print(base_score_message.replace("X", player2))
    else:
        print("This heated Battle of Dices is still going on! Who will be crowned the Champion of the Battle of Dices? ")

    return updated_scores

def update_scores(curr_scores, updated_scores):
    """ Updates the scores """
    for key, val in updated_scores.items():
        score = curr_scores.get(key, 0)
        if val > score:
            curr_scores[key] = val

def play_game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use, player1_rolls, player2_rolls):
    """ Plays a single round of the game """
    updated_scores = game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use, player1_rolls, player2_rolls)
    update_scores(curr_scores, updated_scores)
    return updated_scores

def end_game(player1, player2, curr_scores, total_rounds):
    """ Ends the game """
    print("Game over!")
    winner = player1 if curr_scores[player1] > curr_scores[player2] else player2
    print(winner, "has won the Battle of Dices after", total_rounds, "round(s)!")

    log_player_rolls(flatten(player1_rolls), flatten(player2_rolls), total_rounds)

def initialize_scores(players, curr_scores):
    """ Initializes the scores """
    for player in players:
        if player not in curr_scores:
            curr_scores[player] = 0
    return curr_scores

VALID_INPUTS = ["y", "Y", "yes", "Yes", "YES", ""]
PLAYERS = ["Player 1", "Player 2"]
FIRST_TO_REACH = 3
player1_rolls = []
player2_rolls = []
current_round = 1
scores = {}
SIDES = 6
dice_to_use = determine_dice_to_use(SIDES)
initialize_scores(PLAYERS, scores)

if __name__ == "__main__":
    while (True):
        new_scores = play_game(PLAYERS[0], PLAYERS[1], scores, current_round, FIRST_TO_REACH, dice_to_use, player1_rolls, player2_rolls)
        
        if new_scores[PLAYERS[0]] >= FIRST_TO_REACH or new_scores[PLAYERS[1]] >= FIRST_TO_REACH:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

        if should_play_again(VALID_INPUTS):
            current_round += 1
        else:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

