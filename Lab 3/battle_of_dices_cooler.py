import random
import re

from battle_of_dices_better import should_play_again, clear_console, initialize_scores, end_game
from dice import roll_d6, roll_d4, roll_d8, roll_d12, roll_d20, roll_d100

def game(player1, player2, curr_scores, curr_round, max_score, die_to_use):
    """ Plays a single round of the game """
    clear_console()

    updated_scores = curr_scores.copy()
    winner = ""

    # Roll the dice twice for each player and calculate the winner
    player1_total = die_to_use[0]() + die_to_use[1]()
    player2_total = die_to_use[0]() + die_to_use[1]()

    if player1_total > player2_total: 
        winner = player1
        updated_scores[player1] += 1
    elif player1_total < player2_total: 
        winner = player2
        updated_scores[player2] += 1
    else: winner = "Tie"

    round_str = 'round ' + str(curr_round)

    dice_names = {roll_d4: "D4", roll_d6: "D6", roll_d8: "D8", roll_d12: "D12", roll_d20: "D20", roll_d100: "D100"}
    print(f"Player 1 rolled {dice_names[die_to_use[0]]} and {dice_names[die_to_use[1]]}: total = {player1_total}")
    print(f"Player 2 rolled {dice_names[die_to_use[0]]} and {dice_names[die_to_use[1]]}: total = {player2_total}")

    print(f"{ winner + ' wins ' + round_str + '!' if winner != 'Tie' else 'Amaaazzinng! ' + round_str + ' is a tie!' }")
    print("Current score:", re.sub(r"{|}|'", "", str(updated_scores)))

    base_score_message = "Unbelievable! Player X has without a doubt earned the title of Champion of the Battle of Dices! "
    
    # Determine win or tie
    player1_score = updated_scores[player1]
    player2_score = updated_scores[player2]
    game_has_ended = player1_score >= max_score or player2_score >= max_score
    
    if game_has_ended:
        base_score_message = "Unbelievable! Player X has without a doubt earned the title of Champion of the Battle of Dices! "
        if player1_score >= max_score:
            print(base_score_message.replace("X", player1))
        elif player2_score >= max_score:
            print(base_score_message.replace("X", player2))
    else:
        print("This heated Battle of Dices is still going on! Who will be crowned the Champion of the Battle of Dices? ")

    return updated_scores, game_has_ended

def update_scores(curr_scores, updated_scores):
    """ Updates the scores """
    for key, val in updated_scores.items():
        curr_scores[key] = val


VALID_INPUTS = ["y", "Y", "yes", "Yes", "YES", ""]
PLAYERS = ["Player 1", "Player 2"]
current_round = 1
FIRST_TO_REACH = 3
scores = {}

# Ensure unique dice sides
dice_types = [roll_d4, roll_d6, roll_d8, roll_d12, roll_d20]
dice1 = random.choice(dice_types)
dice2 = random.choice(dice_types)

while dice1 == dice2:
    dice2 = random.choice(dice_types)

dices_to_use = [dice1, dice2]
initialize_scores(PLAYERS, scores)

# Start the game
if __name__ == "__main__":
    while (True):
        new_scores, game_won = game(PLAYERS[0], PLAYERS[1], scores, current_round, FIRST_TO_REACH, dices_to_use)
        update_scores(scores, new_scores)
        
        if game_won:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

        if should_play_again(VALID_INPUTS):
            current_round += 1
        else:
            end_game(PLAYERS[0], PLAYERS[1], scores, current_round)
            break

