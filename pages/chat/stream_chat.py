from stream_chat import StreamChat
import os
from dotenv import load_dotenv
from global_state import get_logged_in_user

load_dotenv()

STREAM_API_KEY = os.getenv("STREAM_API_KEY")
STREAM_API_SECRET = os.getenv("STREAM_API_SECRET")

chat_client = StreamChat(api_key=STREAM_API_KEY, api_secret=STREAM_API_SECRET)


def get_authenticated_user():
    user = get_logged_in_user()
    if not user:
        raise ValueError("No user is logged in!")

    user_id = user["uuid"]
    token = chat_client.create_token(user_id)
    return user_id, token


def get_messages(channel_id):
    user_id, _ = get_authenticated_user()
    channel = chat_client.channel("messaging", channel_id)
    response = channel.query()
    messages = response.get("messages", [])
    return messages


def get_direct_messages():
    user_id, _ = get_authenticated_user()
    filters = {"members": {"$in": [user_id]}, "member_count": 2}
    response = chat_client.query_channels(filters, watch=True, state=True)
    messages = []
    for channel in response["channels"]:
        messages.extend(get_messages(channel["id"]))
    return messages


def get_group_messages():
    user_id, _ = get_authenticated_user()
    filters = {"members": {"$in": [user_id]}, "member_count": {"$gt": 2}}
    response = chat_client.query_channels(filters, watch=True, state=True)
    messages = []
    for channel in response["channels"]:
        messages.extend(get_messages(channel["id"]))
    return messages


def get_all_messages():
    user_id, _ = get_authenticated_user()
    filters = {"members": {"$in": [user_id]}}
    response = chat_client.query_channels(filters, watch=True, state=True)
    messages = []
    for channel in response["channels"]:
        messages.extend(get_messages(channel["id"]))
    return messages


def create_group(group_name):
    user_id, _ = get_authenticated_user()
    channel = chat_client.channel("messaging", group_name)
    channel.create(user_id)
    return channel.id


def add_member_to_group(group_id, member_id):
    channel = chat_client.channel("messaging", group_id)
    try:
        channel.add_members([member_id])
        return True
    except Exception as e:
        print(f"Error adding member to group: {e}")
        return False
