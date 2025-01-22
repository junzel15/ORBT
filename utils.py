import json
import bcrypt


def authenticate_user(email, password):

    with open("users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["email"] == email:

            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return user["full_name"]
            else:
                return None
    return None
