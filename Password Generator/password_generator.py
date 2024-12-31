import random
import string

def generate_password(min_length, numbers = True, special_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = (len(pwd) >= min_length)
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria =  meets_criteria and has_special

    return pwd

pwd = generate_password(5)
print(pwd)
