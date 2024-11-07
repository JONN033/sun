import random
import requests
from core.file_loader import load_tokens, load_emojis, load_member_ids

def spam_server(server_id, channels, random_emojis=False, random_strings=False, mention_members=False):
    tokens = load_tokens()
    emojis = load_emojis() if random_emojis else []
    members = load_member_ids() if mention_members else []

    for token in tokens:
        headers = {"Authorization": f"Bot {token}"}
        for channel in channels:
            payload = {
                "content": generate_message(emojis, random_strings, members)
            }
            response = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, json=payload)
            print(f"Sent message to channel {channel} with status: {response.status_code}")

def generate_message(emojis, random_strings, members):
    message = ""
    if random_strings:
        message += ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))
    if emojis:
        message += ' ' + random.choice(emojis)
    if members:
        message += ' ' + random.choice(members)
    return message
