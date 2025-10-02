import random

class Dice:
    def rollD6(self):
        return random.randint(1, 6)

player_rolls_history = [] 
winning_score = 3
player_names = []
player_wins = []
gameover = False
dice = Dice()
rounds = 0

number_of_players = int(input("How many players?"))

# Initialize players data
for i in range(number_of_players):
    name = input(f"What is the name of Player {i+1}?")
    player_names.append(name)

for i in range(number_of_players):
    player_wins.append(0)

for i in range(number_of_players):
    player_rolls_history.append([])

# Play game
while not gameover:
    rounds += 1
    print(f"Round {rounds}:")
    
    current_rolls = []
    winners = []
    
    # Roll dices
    for i in range(number_of_players):
        roll = dice.rollD6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled {roll}")
    
    input("Press Enter to continue...")
    
    max_roll = max(current_rolls)
    
    # Calculate winners
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    
    print(f"Winners of this round are: {winners}")
    
    # Determine winner
    for i in range(number_of_players):
        if player_wins[i] >= winning_score:
            print(f"\n🎉 {player_names[i]} has won the game with {player_wins[i]} wins!")
            print("\nFinal Scores:")
            for j in range(number_of_players):
                print(f"{player_names[j]}: {player_wins[j]} wins")
            
            print("\nRoll History:")
            for j in range(number_of_players):
                print(f"{player_names[j]}: {player_rolls_history[j]}")
            
            gameover = True
            break
