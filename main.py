import json
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("FERNET_KEY")

if not key:
    key = Fernet.generate_key()
    print(f"Generated Key: {key.decode()}")
    with open(".env", "a") as env_file:
        env_file.write(f"\nFERNET_KEY={key.decode()}")

f = Fernet(key.encode() if isinstance(key, str) else key)

# Ensure files exist
for filename in ["vault.json", "accounts.json"]:
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({"vault": []} if "vault" in filename else {"accounts": []}, f)

user_choice = input("1. Login (type 1)  2. Create Account (type 2): ")

if user_choice == "1":
    action_choice = input("1. Add new file (type 1)  2. View files (type 2): ")

    if action_choice == "1":
        new_file_name = input("Enter new file: ")
        encrypted_name = f.encrypt(new_file_name.encode()).decode()

        with open("vault.json", "r") as file:
            data = json.load(file)

        data["vault"].append({"new_file": encrypted_name})

        with open("vault.json", "w") as file:
            json.dump(data, file, indent=4)

    elif action_choice == "2":
        with open("vault.json", "r") as file:
            data = json.load(file)

        for entry in data["vault"]:
            decrypted_name = f.decrypt(entry["new_file"].encode()).decode()
            print("Decrypted File:", decrypted_name)

elif user_choice == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("accounts.json", "r") as file:
        data = json.load(file)

    data["accounts"].append({"username": username, "password": password})

    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)

else:
    print("Incorrect number. Try again.")
