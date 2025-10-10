import json

# main menu
user_choice = input("1. Login (type 1)  2. Create Account (type 2): ")

if user_choice == "1":  
    action_choice = input("1. Add new file (type 1)  2. View files (type 2): ")
    
    if action_choice == "1":
        new_file_name = input("Enter new file: ")
        
        # open vault and add new file
        with open("vault.json", "r") as file:
            data = json.load(file)
            new_file_entry = {"new_file": new_file_name}
            data["vault"].append(new_file_entry)
        
        # save updated vault
        with open("vault.json", "w") as file:
            json.dump(data, file, indent=4)

    elif action_choice == "2":
        # open and load accounts file
        with open("accounts.json", "r") as file:
            data = json.load(file)

        # print accounts neatly
        print(json.dumps(data, indent=4))

elif user_choice == "2":
    # get username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # load and add new user
    with open("accounts.json", "r") as file:
        data = json.load(file)
        new_user = {"username": username, "password": password}
        data["accounts"].append(new_user)

    # save to json
    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)

else:
    print("Incorrect number. Try again.")
