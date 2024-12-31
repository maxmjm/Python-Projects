import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True

        meets_criteria = (len(password) >= min_length)
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria =  meets_criteria and has_special

    return password

min_length = int(input("Enter minimum length of password: "))
has_number = input("Do you want the password to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want the password to have special characters (y/n)? ").lower() == "y"

password = generate_password(min_length, has_number, has_special)
print("The generated password is:", password)
