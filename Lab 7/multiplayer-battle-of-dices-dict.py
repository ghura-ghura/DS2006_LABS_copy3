from copy import deepcopy
from random import randint

class Dice:
    def rollD6(self):
        return randint(1, 6)

rounds = 0
gameover = False
winning_score = 3

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": [],
}

players = []

number_of_players = int(input("How many players? "))

for i in range(number_of_players):
    player = deepcopy(player_info)

    player["name"] = input(f"What is the name of Player {i+1}? ")
    player["email"] = input(f"What is the e-mail of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")
    
    players.append(player)

dice = Dice()

while gameover is False:
    print(f"Round {rounds+1}:")
    current_rolls = []

    for each_player in players:
        roll = dice.rollD6()

        each_player["rolls"].append(roll)
        current_rolls.append(roll)

        print(f"Player {each_player['name']} rolled {roll}")

    max_roll = max(current_rolls)
    winners = []

    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            each_player["wins"] += 1
            print(f"Player {each_player['name']} won in round {rounds+1}")
            winners.append(each_player["name"])

    print(f"Winners of this round: {winners}")

    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n {each_player['name']} is the newest Battle of Dices Champion!")
            gameover = True
            break
    
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

    rounds += 1

filename = str(input("Enter the filename to save the results: "))
with open(filename, "w") as file:
    file.write("Player Information:\n")

    for each_player in players:
        file.write(f"Name: {each_player['name']}\n")
        file.write(f"* E-mail: {each_player['email']}\n")
        file.write(f"* Country: {each_player['country']}\n")
        file.write(f"* Wins: {each_player['wins']}\n\n")

    file.write("Results:\n")

    for r in range(rounds):
        rolls_str = ""

        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            if i < len(players) - 1:
                rolls_str += ", "
        
        file.write(f"Round {r+1}: {rolls_str}\n")

print(f"\nGame over! Results saved to {filename}")