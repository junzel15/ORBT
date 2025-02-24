import global_state
from stream_chat import StreamChat
import os
from dotenv import load_dotenv

load_dotenv()

STREAM_API_KEY = os.getenv("STREAM_API_KEY")
STREAM_API_SECRET = os.getenv("STREAM_API_SECRET")

chat_client = StreamChat(api_key=STREAM_API_KEY, api_secret=STREAM_API_SECRET)

try:
    test_channel = chat_client.channel("messaging", "test_channel")
    test_channel.create("test_user")
    print("Channel successfully created or retrieved!")
except Exception as e:
    print(f"StreamChat setup error: {e}")


def get_authenticated_user():
    user = global_state.get_logged_in_user()
    if not user:
        raise ValueError("No user is logged in!")

    user_id = user["uuid"]
    token = chat_client.create_token(user_id)

    return user_id, token


def get_or_create_channel(channel_id):
    user_id, _ = get_authenticated_user()

    try:
        channel = chat_client.channel(
            "messaging", channel_id, {"name": f"Chat {channel_id}"}
        )
        channel.create(user_id)
        return channel
    except Exception as e:
        print(f"Error creating or retrieving channel: {e}")
        return None


def send_message(channel_id, message):
    user_id, _ = get_authenticated_user()
    channel = get_or_create_channel(channel_id)

    if channel:
        try:
            response = channel.send_message({"text": message, "user_id": user_id})
            return response
        except Exception as e:
            print(f"Error sending message: {e}")
            return None


def get_messages(channel_id):
    channel = get_or_create_channel(channel_id)

    if not channel:
        print(f"Failed to retrieve channel: {channel_id}")
        return []

    try:
        response = channel.query()
        messages = response.get("messages", [])
        return messages
    except AttributeError as e:
        print(f"Channel object does not have query method: {e}")
    except Exception as e:
        print(f"Error retrieving messages: {e}")

    return []
