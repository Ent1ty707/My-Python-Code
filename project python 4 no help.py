username = input("Please enter your username: ")
if username == "admin":
    print("Welcome, admin!")
    password = input("Please enter your password: ")
    if password == "Dalha":
        print("Authentication successful.")
        input("Press Enter to continue...")
        print("Accessing admin panel...")
        input("You have successfully logged in as admin. Press Enter to exit.")
    else:
        print("Invalid password.")

if username == "user":
    print("Welcome, user!")
    password = input("Please enter your password: ")
    if password == "userpass":
        print("Authentication successful.")
        input("Press Enter to continue...")
        print("Accessing user panel...")
        input("You have successfully logged in as user. Press Enter to exit.")
    else:
        print("Invalid password.")
