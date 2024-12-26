master_password = input("What is the master password? ")

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as password_file:
        password_file.write(name + " | " + password + "\n")


def view():
    pass

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
