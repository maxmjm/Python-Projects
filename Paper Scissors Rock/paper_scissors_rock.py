import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type paper (p), scissors (s) or rock (r): ").lower()

    if user_input not in ["paper", "scissors", "rock"] or ["p", "s", "r"]:
        print("Invalid input please try again!")
        continue
