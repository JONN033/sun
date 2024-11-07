import os
import colorama
from colorama import Fore
from pystyle import Colors, Colorate
from core.server_spammer import spam_server
from core.webhook_spammer import spam_webhook
from core.webhook_deleter import delete_webhooks
from core.token_formatter import main as token_formatter_main 

def get_terminal_width():
    """Get the width of the terminal window."""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 120  

def center_text(text):
    """Center text based on terminal width."""
    terminal_width = get_terminal_width()
    return text.center(terminal_width)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Display the banner at the top of the application."""
    clear_screen()
    header = '''
   _____             
  / ____|            
 | (___  _   _ _ __  
  \___ \| | | | '_ \ 
  ____) | |_| | | | |
 |_____/ \____|_| |_| 
 -------------------- 
    '''
    for line in header.splitlines():
        if line.strip():
            print(Colorate.Horizontal(Colors.yellow_to_red, center_text(line)))


    print(center_text(f"    Version 1 | https://github.com/JONN033/sun\n"))

def main_menu():
    """Display the main menu."""
    menu = '''
<1> Server Spammer   <2> Webhook Spammer   <3> Webhook Deleter   <4> Token Formatter
    '''

    menu_lines = menu.splitlines()
    centered_menu = '\n'.join([center_text(line) for line in menu_lines if line.strip()])
    print(centered_menu)

def main_menu2():
    """Display the second menu."""
    menu = '''<5> Exit            <6> Token Onliner     <7> Token Nuker       <8> Reply Spammer
(More features soon!)
    '''
    menu_lines = menu.splitlines()
    centered_menu = '\n'.join([center_text(line) for line in menu_lines if line.strip()])
    print(centered_menu)

def handle_server_spammer():
    """Handle server spammer functionality."""
    server_id = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Enter the server ID: ").strip()
    channels = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Enter channel IDs (comma-separated): ").split(',')
    random_emojis = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Include random emojis from emojis.txt? (y/n): ").lower() == 'y'
    random_strings = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Include random strings? (y/n): ").lower() == 'y'
    mention_members = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Mention members from member_ids.txt? (y/n): ").lower() == 'y'
    spam_server(server_id, channels, random_emojis, random_strings, mention_members)

def handle_webhook_spammer():
    """Handle webhook spammer functionality."""
    mention_everyone = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Mention @everyone? (y/n): ").lower() == 'y'
    mention_here = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Mention @here? (y/n): ").lower() == 'y'
    include_emojis = input(f"{Fore.YELLOW}[INFORMATION]: {Fore.LIGHTWHITE_EX}Include emojis? (y/n): ").lower() == 'y'
    spam_webhook(mention_everyone, mention_here, include_emojis)

def handle_webhook_deleter():
    """Handle webhook deletion."""
    delete_webhooks()

def get_user_choice():
    """Get and validate the user's menu choice."""
    while True:
        try:
            user_choice = input(f"{Fore.YELLOW}[INPUT]: > {Fore.WHITE}").strip()
            if user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                raise ValueError("Invalid option. Please choose a valid menu option.")
            return user_choice
        except ValueError as e:
            print(f"{Fore.RED}[ERROR]: {Fore.LIGHTWHITE_EX}{e}")

def main():
    """Main function to drive the menu and options."""
    while True:
        display_banner()
        main_menu()
        main_menu2() 
        user_choice = get_user_choice()

        if user_choice == "1":
            handle_server_spammer()
        elif user_choice == "2":
            handle_webhook_spammer()
        elif user_choice == "3":
            handle_webhook_deleter()
        elif user_choice == "4":
            token_formatter_main()  
        elif user_choice == "5":
            print(f"{Fore.Yellow}[WARNING]:{Fore.LIGHTWHITE_EX}Exiting Sun")
            break
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.LIGHTWHITE_EX}Invalid option, please try again.")

        clear_screen()

if __name__ == "__main__":
    main()
