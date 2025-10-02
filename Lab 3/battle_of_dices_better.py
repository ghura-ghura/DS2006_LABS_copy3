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

def game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use):
    """ Plays a single round of the game """
    clear_console()

    rolls = roll_x_dices(2, dice_to_use)
    player1_roll, player2_roll = rolls[0], rolls[1]
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

def play_game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use):
    """ Plays a single round of the game """
    updated_scores = game(player1, player2, curr_scores, curr_round, first_to_reach, dice_to_use)
    update_scores(curr_scores, updated_scores)
    return updated_scores

def end_game(player1, player2, curr_scores, total_rounds):
    """ Ends the game """
    print("Game over!")
    winner = player1 if curr_scores[player1] > curr_scores[player2] else player2
    print(winner, "has won the Battle of Dices after", total_rounds, "round(s)!")

def initialize_scores(players, curr_scores):
    """ Initializes the scores """
    for player in players:
        if player not in curr_scores:
            curr_scores[player] = 0
    return curr_scores

VALID_INPUTS = ["y", "Y", "yes", "Yes", "YES", ""]
PLAYERS = ["Player 1", "Player 2"]
current_round = 1
FIRST_TO_REACH = 3
scores = {}
SIDES = 6
dice_to_use = determine_dice_to_use(SIDES)
initialize_scores(PLAYERS, scores)

if __name__ == "__main__":
    while (True):
        new_scores = play_game(PLAYERS[0], PLAYERS[1], scores, current_round, FIRST_TO_REACH, dice_to_use)
        
        if new_scores[PLAYERS[0]] >= FIRST_TO_REACH or new_scores[PLAYERS[1]] >= FIRST_TO_REACH:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

        if should_play_again(VALID_INPUTS):
            current_round += 1
        else:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

