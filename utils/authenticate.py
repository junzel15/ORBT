import json
import bcrypt


def authenticate_user(email, password):
    with open("json/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["email"] == email:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return {
                    "full_name": user["full_name"],
                    "address": user["address"],
                    "bio": user["bio"],
                }
    return None
