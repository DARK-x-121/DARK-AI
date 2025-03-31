import webbrowser
import requests
import os
import platform
from colorama import init, Fore, Style

init(autoreset=True)

def display_banner():
    print(Fore.CYAN + Style.BRIGHT + "===============================")
    print(Fore.MAGENTA + "        🌑 DARK AI 🌑       ")
    print(Fore.CYAN + "===============================")
    print(Fore.YELLOW + "Author: " + Fore.GREEN + "AMIT")
    print(Fore.YELLOW + "Credit: " + Fore.GREEN + "RAIN")
    print(Fore.YELLOW + "By: " + Fore.GREEN + "DARK")
    print(Fore.CYAN + "===============================")
    print(Fore.YELLOW + "1. " + Fore.GREEN + "Start: Visit WhatsApp Group & Run Script")
    print(Fore.YELLOW + "2. " + Fore.GREEN + "Owner: Message Owner on WhatsApp")
    print(Fore.YELLOW + "3. " + Fore.GREEN + "Exit: Exit the Tool")
    print(Fore.CYAN + "===============================")

def get_api_response(user_message, mode, timeout):
    url = "https://dev-apis-xyz.pantheonsite.io/wp-content/apis/freeAi.php"
    params = {"prompt": user_message, "model": mode}
    
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"\n⚠️ Error: API request failed!\n{str(e)}"

def start_script():
    if is_termux():
        os.system("termux-open-url https://chat.whatsapp.com/LYMt9FKfYSuDcTH5W3C2r5")
    else:
        webbrowser.open("https://chat.whatsapp.com/LYMt9FKfYSuDcTH5W3C2r5")
    
    print(Fore.GREEN + "You have been redirected to the WhatsApp group.")
    print("Running the main script...\n")
    main()

def contact_owner():
    if is_termux():
        os.system("termux-open-url https://wa.me/919836942455")
    else:
        webbrowser.open("https://wa.me/919836942455")
    
    print(Fore.GREEN + "You have been redirected to WhatsApp to message the owner.\n")

def main():
    print(Fore.GREEN + "Starting the main script...\n")

    while True:
        mode = input("Choose Mode (llama - deepseek - blackbox - chatgpt - wormgpt - evilgpt): ").strip().lower()
        
        if not is_valid_mode(mode):
            print(Fore.RED + "\n⚠️ Invalid mode! Please choose from: llama, deepseek, blackbox, chatgpt, wormgpt, or evilgpt.\n")
            continue

        user_message = input("- Enter your message: ").strip()
        
        if user_message.lower() == 'exit':
            print(Fore.YELLOW + "\nThe conversation has ended.\n")
            break

        try:
            timeout = int(input(Fore.CYAN + "Enter request timeout in seconds (default 10): ").strip() or 10)
        except ValueError:
            timeout = 10

        response = get_api_response(user_message, mode, timeout)
        
        print(Fore.MAGENTA + "\n- API Response:", response)

def is_valid_mode(mode):
    valid_modes = ['llama', 'deepseek', 'blackbox', 'chatgpt', 'wormgpt', 'evilgpt']
    return mode.lower() in valid_modes

def is_termux():
    return "termux" in platform.system().lower()

def main_entry():
    display_banner()

    while True:
        choice = input(Fore.CYAN + "Choose an option: ").strip()

        if choice == '1':
            start_script()
            break
        elif choice == '2':
            contact_owner()
            break
        elif choice == '3':
            print(Fore.RED + Style.BRIGHT + "\nThanks for using DARK AI!")
            print(Fore.MAGENTA + "Hope to see you again soon!")
            break
        else:
            print(Fore.RED + "Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main_entry()