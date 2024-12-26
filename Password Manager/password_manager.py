from cryptography.fernet import Fernet

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

master_password = input("What is the master password? ")
key = load_key() + master_password.encode()
fer = Fernet(key)
    
def add():
    account_name = input("Account Name: ")
    account_password = input("Password: ")

    with open("passwords.txt", "a") as password_file:
        password_file.write(account_name + " | " + fer.encrypt(account_password.encode()).decode() + "\n")

def view():
    with open("passwords.txt", "r") as password_file:
        for line in password_file.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print("Account Name:", name, "| Password:", fer.decrypt(password.encode()).decode())

while True:

    mode = input("Would you like to add a new password or view existing ones (add, view, quit)? ").lower()

    if mode == "quit":
        print("Exiting program!")
        break

    if mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid mode!")
        continue
