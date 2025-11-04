import argparse
import subprocess
import os
import requests
from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init()

# Function for process1: List files in the current directory
def run_process1():
    print(Fore.CYAN + "Running Process 1: Listing files in the current directory" + Style.RESET_ALL)
    files = os.listdir('.')
    for file in files:
        print(Fore.GREEN + file + Style.RESET_ALL)

# Function for process2: Run system info command
def run_process2():
    print(Fore.CYAN + "Running Process 2: Displaying system info" + Style.RESET_ALL)

    # ❌ INSECURE: Using shell=True with unsanitized input
    user_input = input("Enter a system command to run: ")

    # This is dangerous and will be flagged by Semgrep as a potential command injection
    subprocess.run(user_input, shell=True)


# Function for process3: Write a custom message to a file
def run_process3(message):
    print(Fore.CYAN + f"Running Process 3: Writing message to file - {message}" + Style.RESET_ALL)
    with open('output.txt', 'w') as file:
        file.write(message)
    print(Fore.GREEN + "Message written to 'output.txt'" + Style.RESET_ALL)

# Function for process4: Fetch data from an API (using `requests`)
def run_process4(api_url):
    print(Fore.CYAN + f"Running Process 4: Fetching data from API - {api_url}" + Style.RESET_ALL)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(Fore.GREEN + f"Response from {api_url}: " + response.json() + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Failed to fetch data. Status code: {response.status_code}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error occurred while fetching data: {e}" + Style.RESET_ALL)

# Function for process5: Display a banner
def run_process5(banner_text):
    print(Fore.CYAN + "Running Process 5: Displaying banner" + Style.RESET_ALL)
    f = Figlet(font='slant')
    banner = f.renderText(banner_text)
    print(Fore.MAGENTA + banner + Style.RESET_ALL)

# Main function to handle argument parsing and process selection
def main():
    parser = argparse.ArgumentParser(description="CLI Tool that runs different processes based on arguments.")
    
    # Adding subcommands for different processes
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Command for process1 (List files in the directory)
    subparsers.add_parser('process1', help='List files in the current directory.')
    
    # Command for process2 (Display system info)
    subparsers.add_parser('process2', help='Display system information.')
    
    # Command for process3 (Write a message to a file)
    process3_parser = subparsers.add_parser('process3', help='Write a message to a file.')
    process3_parser.add_argument('message', type=str, help='Message to write to the file.')
    
    # Command for process4 (Fetch data from an API)
    process4_parser = subparsers.add_parser('process4', help='Fetch data from an API endpoint.')
    process4_parser.add_argument('api_url', type=str, help='API URL to fetch data from.')
    
    # Command for process5 (Display an ASCII banner)
    process5_parser = subparsers.add_parser('process5', help='Display an ASCII banner.')
    process5_parser.add_argument('banner_text', type=str, help='Text to display as a banner.')

    # Parse arguments
    args = parser.parse_args()

    # Execute the corresponding process based on the command
    if args.command == 'process1':
        run_process1()
    elif args.command == 'process2':
        run_process2()
    elif args.command == 'process3':
        run_process3(args.message)
    elif args.command == 'process4':
        run_process4(args.api_url)
    elif args.command == 'process5':
        run_process5(args.banner_text)
    else:
        print(Fore.RED + "Invalid command. Use --help to see available commands." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
