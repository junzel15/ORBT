import json


def get_user_data():

    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: user_data.json not found!")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON!")
        return {}
