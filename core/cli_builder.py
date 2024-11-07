from easygui import buttonbox
from colorama import Fore, Style
from pystyle import Colors, Colorate

def display_menu():
    options = ["Server Spammer", "Webhook Spammer", "Webhook Deleter", "Exit"]
    choice = buttonbox("Choose a feature:", "Sun Tool CLI", options)
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Selected option: {choice}"))
    return choice
