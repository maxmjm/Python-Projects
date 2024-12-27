import turtle

def get_number_of_racers():
    number_of_racers = 0
    while True:
        number_of_racers = input("How many racers (2-10)? ")
        if number_of_racers.isdigit():
            number_of_racers = int(number_of_racers)
        else:
            print("Invalid input please try again!")
            continue
        if 2 <= number_of_racers <= 10:
            return number_of_racers
        else:
            print("Number of racers must be between 2 and 10 inclusive!")
