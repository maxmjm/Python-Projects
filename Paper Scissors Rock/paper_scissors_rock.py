import random

user_wins = 0
computer_wins = 0
options = ["paper", "scissors", "rock"]
shortcuts = {"p": "paper", "s": "scissors", "r": "rock", "q": "quit"}

while True:
    user_input = input("Type paper (p), scissors (s), rock (r), or quit (q): ").lower()

    user_input = shortcuts.get(user_input, user_input) # Map shortcuts to full word

    if (user_input == "quit"):
        print(f"Game over! You won {user_wins} time/s. The computer won {computer_wins} time/s.")
        break

    if user_input not in options:
        print("Invalid input please try again!")
        continue

    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!")

    elif (user_input == "paper" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "paper") or (user_input == "rock" and computer_pick == "scissors"):
        print(f"{user_input.capitalize()} beats {computer_pick}. You win! ")
        user_wins += 1

    else: 
        print(f"{computer_pick.capitalize()} beats {user_input}. You lose!")
        computer_wins += 1
