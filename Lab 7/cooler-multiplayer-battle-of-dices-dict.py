import random
import sys
import os

# Add Week 2 Lab 3 to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
lab3_path = os.path.join(project_root, "Week 2", "Lab 3")
sys.path.append(lab3_path)

from battle_of_dices_better import should_play_again

class Dice:
    def rollD6(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name="", email="", country="", wins=0, rolls=[]):
        self.country = country
        self.rolls = rolls
        self.email = email
        self.name = name
        self.wins = wins
    
    def to_dict(self):
        """Convert player to dictionary for file saving"""
        return {
            "country": self.country,
            "rolls": self.rolls,
            "email": self.email,
            "name": self.name,
            "wins": self.wins,
        }
    
    def get_details(self):
        return f"Name: {self.name}\n* E-mail: {self.email}\n* Country: {self.country}\n* Wins: {self.wins}\n"

number_of_players = int(input("How many players? "))
VALID_INPUTS = ["y", "Y", "yes", "Yes", "YES", ""]
winning_score = 3
gameover = False
dice = Dice()
players = []
rounds = 0

# Get player info
for i in range(number_of_players):
    player = Player()

    player.name = input(f"What is the name of Player {i+1}? ")
    player.email = input(f"What is the e-mail of Player {i+1}? ")
    player.country = input(f"What is the country of Player {i+1}? ")

    players.append(player)


# Start the game
if __name__ == "__main__":
    while True:
        print(f"Round {rounds+1}:")
        current_rolls = []
        
        for each_player in players:
            roll = dice.rollD6()
            each_player.rolls.append(roll)
            current_rolls.append(roll)
            print(f"Player {each_player.name} rolled: {roll}")
        
        max_roll = max(current_rolls)
        winners = []
        
        # Check for winners of this round
        for each_player in players:
            if(each_player.rolls[-1] == max_roll):
                each_player.wins += 1
                print(f"Player {each_player.name} won in round {rounds+1}")
                winners.append(each_player.name)
        
        # Print winners and handle multiple winners of round
        if len(winners) == 1:
            print(f"Winner of this round is: {winners[0]}")
        else:
            print(f"Winners of this round are: {' and '.join(winners)}")
        print("Current scores:", {player.name: player.wins for player in players})
        
        game_ended = False
        for each_player in players:
            if(each_player.wins >= winning_score):
                print(f"\n {each_player.name} is the newest Battle of Dices Champion!")
                game_ended = True
                break
        
        if game_ended:
            print("Game over!")
            break
        
        if not should_play_again(VALID_INPUTS):
            print("Game over!")
            break
        
        rounds += 1
    
    # Save results to file
    filename = input("Enter the filename to save the results: ")
    filename = "dice_results.txt" if filename == "" else filename
    
    with open(filename, "w") as file:
        content = ""
        content += "Player Information:\n"
       
        for each_player in players:
            content += each_player.get_details() + "\n"
        
        content += "\nGame rounds:\n"
        
        for r in range(rounds):
            rolls_str = ""
            for i, each_player in enumerate(players):
                rolls_str += f"{each_player.name} rolled {each_player.rolls[r]}"
                if i < len(players) - 1:
                    rolls_str += ", "
            content += f"Round {r+1}:\n {rolls_str}\n"

        file.write(content)
    
    print("\nGame over! Results saved successfully.")