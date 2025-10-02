import random
import re
import sys
import os

# Add Week 2 Lab 3 to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
lab3_path = os.path.join(project_root, "Week 2", "Lab 3")
sys.path.append(lab3_path)

from battle_of_dices_better import should_play_again, clear_console, end_game
from dice import roll_d6, roll_d4, roll_d8, roll_d12, roll_d20, roll_d100

class Dice:
    def rollD6(self):
        return random.randint(1, 6)

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

# Multiplayer setup (like Task 3)
winning_score = 3
player_names = []
player_wins = []
player_rolls_history = []
current_round = 1

# Get number of players
number_of_players = int(input("How many players? "))

# Initialize player data
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}? ")
    player_names.append(name)

for i in range(number_of_players):
    player_wins.append(0)

for i in range(number_of_players):
    player_rolls_history.append([])

# Ensure unique dice sides
dice_types = [roll_d4, roll_d6, roll_d8, roll_d12, roll_d20]
dice1 = random.choice(dice_types)
dice2 = random.choice(dice_types)

while dice1 == dice2:
    dice2 = random.choice(dice_types)

dices_to_use = [dice1, dice2]
dice_names = {roll_d4: "D4", roll_d6: "D6", roll_d8: "D8", roll_d12: "D12", roll_d20: "D20", roll_d100: "D100"}

# Start the game
if __name__ == "__main__":
    while (True):
        print(f"Round {current_round}:")
        
        current_totals = []
        
        # Each player rolls their dice
        for i in range(number_of_players):
            total = dices_to_use[0]() + dices_to_use[1]()
            current_totals.append(total)
            player_rolls_history[i].append(total)
            print(f"{player_names[i]} rolled {dice_names[dices_to_use[0]]} and {dice_names[dices_to_use[1]]}: total = {total}")
        
        # Find winners
        max_total = max(current_totals)
        winners = []
        for j in range(len(current_totals)):
            if current_totals[j] == max_total:
                winners.append(player_names[j])
                player_wins[j] += 1
        
        # Print winners and handle multiple winners of round
        if len(winners) == 1:
            print(f"Winner of this round is: {winners[0]}")
        else:
            print(f"Winners of this round are: {' and '.join(winners)}")
        print("Current scores:", {player_names[i]: player_wins[i] for i in range(number_of_players)})
        
        # Determine if the game is over or continuing
        game_ended = False
        for i in range(number_of_players):
            if player_wins[i] >= winning_score:
                print(f"Unbelievable! {player_names[i]} has without a doubt earned the title of Champion of the Battle of Dices!")
                game_ended = True
                break
        
        if game_ended or not should_play_again(VALID_INPUTS):
            print("Game over!")
            break
        
        current_round += 1

