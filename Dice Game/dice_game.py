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

while max(player_scores) < max_score:
    for player_index in range(num_players):
        print("\nPlayer number", player_index + 1, "turn has just started!")
        print("Your total score is", player_scores[player_index], "\n")
        current_score = 0

        while True:
            roll = input("Would you like to roll (y)? ")
            if roll.lower() != "y":
                break
            value = roll_dice()
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_score = 0
                break
            else: 
                current_score += value
                print("You rolled a", value)
            print("Your score is", current_score)
        player_scores[player_index] += current_score
        print("Your total score is", player_scores[player_index])
