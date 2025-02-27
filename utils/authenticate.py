import bcrypt
from utils.account_provider import get_user_from_dynamodb


def authenticate_user(email, password):
    try:
        user_data = get_user_from_dynamodb(email)
        if user_data and bcrypt.checkpw(
            password.encode(), user_data["password"].encode()
        ):
            return user_data
        else:
            print("Authentication failed: Invalid email or password.")
            return None
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
