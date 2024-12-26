import random

random_num = random.randrange(0, 11)
num_guess = 0

print("Welcome to the number guessing game! Guess a number between 0 and 10!")

while True:
    num_guess += 1
    user_guess = input("Make a guess: ")

    try:
        user_guess = int(user_guess)

        if user_guess < 0:
            print("Please choose a number greater than or equal to 0!")
            continue

        if user_guess > 10:
            print("Please choose a number less than or equal to 10!")
            continue
    
    except ValueError:
        print("Please type a valid number!")
        continue

    if user_guess == random_num:
        print(f"You got it! The correct number was {random_num}.")
        break

    else:
        if user_guess > random_num:
            print("Lower!")
            continue
        else:
            print("Higher!")
            continue

print("It took you", num_guess, "guesses!")
