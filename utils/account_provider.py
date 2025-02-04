import json


def get_user_data(email):
    try:

        with open("json/users.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["email"] == email:
                return user

        return None
    except FileNotFoundError:
        print("Error: user_data.json not found!")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON!")
        return None
