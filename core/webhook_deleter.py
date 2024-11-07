import requests
import colorama 
from colorama import Fore
from core.file_loader import load_webhooks

def delete_webhooks():
    webhooks = load_webhooks()
    for webhook in webhooks:
        response = requests.delete(webhook)
        print(f"{Fore.GREEN}[SUCCESS]: {Fore.LIGHTWHITE_EX}Deleted webhook {webhook} with status: {response.status_code}")
