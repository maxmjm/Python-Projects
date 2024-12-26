import random

user_wins = 0
computer_wins = 0
options = ["paper", "scissors", "rock", "quit", "p", "s", "r", "q"]

while True:
    user_input = input("Type paper (p), scissors (s), rock (r), or quit (q): ").lower()

    if (user_input == "quit" or user_input == "q"):
        print("Game over! You scored", user_wins, f"and the computer scored {computer_wins}.")
        break

    if user_input not in options:
        print("Invalid input please try again!")
        continue

    random_num = random.randint(0, 2) # paper: 0, scissors: 1, rock: 2 

    computer_pick = options[random_num]
    print(f"Computer picked {computer_pick}.")

    if (user_input == "paper" or user_input == "p") and (computer_pick == "rock"):
        print("Paper beats rock you win!")
        user_wins += 1
    
    elif (user_input == "scissors" or user_input == "s") and (computer_pick == "paper"):
        print("Scissors beats paper you win!")
        user_wins += 1
        
    elif (user_input == "rock" or user_input == "r") and (computer_pick == "scissors"):
        print("Rock beats scissors you win!")
        user_wins += 1
        continue

    elif (computer_pick == "paper") and (user_input == "rock" or user_input == "r"):
        print("Paper beats rock you lost!")
        computer_wins += 1
    
    elif (computer_pick == "scissors") and (user_input == "paper" or user_input == "p"):
        print("Scissors beats paper you lost!")
        computer_wins += 1
        
    elif (computer_pick == "rock") and (user_input == "scissors" or user_input == "s"):
        print("Rock beats scissors you lost!")
        computer_wins += 1
