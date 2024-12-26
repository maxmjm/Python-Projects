master_password = input("What is the master password? ")

def add():
    account_name = input("Account Name: ")
    account_password = input("Password: ")

    with open("passwords.txt", "a") as password_file:
        password_file.write(account_name + " | " + account_password + "\n")

def view():
    with open("passwords.txt", "r") as password_file:
        for line in password_file.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print("Account Name:", name, "| Password:", password)

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
