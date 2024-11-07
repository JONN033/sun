import random
import requests
from core.file_loader import load_webhooks, load_emojis

def spam_webhook(mention_everyone=False, mention_here=False, include_emojis=False):
    webhooks = load_webhooks()
    emojis = load_emojis() if include_emojis else []
    
    # Ask for customizations
    rename_webhook = input("Do you want to rename the webhook? (y/n): ").lower() == 'y'
    if rename_webhook:
        new_name = input("Enter the new name for the webhook: ")

    change_pfp = input("Do you want to change the webhook's profile picture? (y/n): ").lower() == 'y'
    if change_pfp:
        pfp_path = input("Enter the file path of the image to set as the profile picture: ")

    # Ask how many messages to send
    try:
        message_count = int(input("How many messages would you like to send? "))
    except ValueError:
        print("Invalid number. Defaulting to 1 message.")
        message_count = 1

    # Ask for custom message content
    message_content = input("Enter the content of the message to send: ")

    for webhook in webhooks:
        for _ in range(message_count):
            # Generate the message with mentions and emojis
            message = generate_webhook_message(mention_everyone, mention_here, emojis, message_content)

            # Send the message
            response = requests.post(webhook, json={"content": message})

            # Optionally change webhook name and profile picture
            if rename_webhook:
                set_webhook_name(webhook, new_name)
            if change_pfp:
                set_webhook_pfp(webhook, pfp_path)

            print(f"Webhook spam status: {response.status_code}")

def generate_webhook_message(mention_everyone, mention_here, emojis, content):
    message = content
    if mention_everyone:
        message = "@everyone " + message
    if mention_here:
        message = "@here " + message
    if emojis:
        message += ' ' + ' '.join(random.choices(emojis, k=3))
    return message.strip()

def set_webhook_name(webhook, new_name):
    """Set the webhook's name (placeholder function, requires an API endpoint to update the name)."""
    # TO BE IMPLEMENTED
    print(f"Renaming webhook to: {new_name}")

def set_webhook_pfp(webhook, pfp_path):
    """Set the webhook's profile picture (placeholder function, requires an API endpoint to update the pfp)."""
    # TO BE IMPLEMENTED
    print(f"Changing webhook profile picture to: {pfp_path}")
