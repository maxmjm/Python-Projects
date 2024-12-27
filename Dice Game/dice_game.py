import random

def roll_dice():
    min_val = 1
    max_val = 6
    roll_dice = random.randint(min_val, max_val)

    return roll_dice

while True:
    num_players = input("Enter number of players (1-4): ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            break
        else:
            print("Invalid number of players!")
    else:
        print("Invalid input try again!")

max_score = 60
player_scores = [0 for _ in range(num_players)]
