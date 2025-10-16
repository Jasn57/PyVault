import json
from cryptography.fernet import Fernet

user_choice = input("1. Login (type 1)  2. Create Account (type 2): ")

if user_choice == "1":  
    action_choice = input("1. Add new file (type 1)  2. View files (type 2): ")
    
    if action_choice == "1":
        new_file_name = input("Enter new file: ")
        new_file_name = encrypted_message = f.encrypt(new_file_name.encode())
        
        with open("vault.json", "r") as file:
            data = json.load(file)
            new_file_entry = {"new_file": new_file_name}
            data["vault"].append(new_file_entry)
        
        with open("vault.json", "w") as file:
            json.dump(data, file, indent=4)

    elif action_choice == "2":
        with open("accounts.json", "r") as file:
            data = json.load(file)
        decrypted_message = f.decrypt(encrypted_message).decode()
        print(json.dumps(data, indent=4))

elif user_choice == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("accounts.json", "r") as file:
        data = json.load(file)
        new_user = {"username": username, "password": password}
        data["accounts"].append(new_user)

    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)

else:
    print("Incorrect number. Try again.")
