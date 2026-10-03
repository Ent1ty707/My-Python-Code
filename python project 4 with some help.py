accounts = {"admin": "Dalha", "user": "userpass"}

username = input("Please enter your username: ")

if username in accounts:
    password = input("Please enter your password: ")

    if password == accounts[username]:
        print("Authentication successful.")

        if username == "admin":
            while True:
                print("\nAdmin panel")
                print("1. Change admin password")
                print("2. Change a user's password")
                print("3. Create an account")
                print("4. Log out")
                choice = input("Choose an option: ")

                if choice == "1":
                    new_password = input("Enter the new admin password: ")
                    if new_password != "":
                        accounts["admin"] = new_password
                        print("Admin password changed.")
                    else:
                        print("Password cannot be empty.")

                elif choice == "2":
                    target_username = input("Enter the user's username: ")
                    if target_username in accounts and target_username != "admin":
                        new_password = input("Enter the new password: ")
                        if new_password != "":
                            accounts[target_username] = new_password
                            print("User password changed.")
                        else:
                            print("Password cannot be empty.")
                    else:
                        print("That user account was not found.")

                elif choice == "3":
                    new_username = input("Enter a username for the new account: ")
                    if new_username != "" and new_username not in accounts:
                        new_password = input("Enter a password for the new account: ")
                        if new_password != "":
                            accounts[new_username] = new_password
                            print("Account created.")
                        else:
                            print("Password cannot be empty.")
                    else:
                        print("Username is empty or already in use.")

                elif choice == "4":
                    print("Logged out.")
                    break

                else:
                    print("Please choose 1, 2, 3, or 4.")
        else:
            print("Accessing user panel...")
            input("Press Enter to exit.")
    else:
        print("Invalid password.")
else:
    print("Username not found.")