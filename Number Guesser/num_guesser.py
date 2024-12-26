import random

random_num = random.randrange(-1, 11)

while True:
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please choose a number greater than 0!")
            continue

    else:
        print("Please type a number!")
        continue

    if user_guess == random_num:
        print("You got it!")
        break

    else:
        print("Wrong try again!")
        continue
