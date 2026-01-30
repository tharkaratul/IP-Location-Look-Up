import requests
import socket
from colorama import init, Fore, Style
print("choose The Option")
print("1. IF YOU KNOW IP ADDRESS")
print("2. IF YOU DONT KNOW IP ADDRESS")
option=int(input(F"{Fore.GREEN}OPTION NO :-{Style.RESET_ALL}"))
if option >=2:
    domain = input("Enter website: ")
    ip = socket.gethostbyname(domain)
    url = f"https://api.db-ip.com/v2/free/{ip}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nIP Geolocation Result")
        print(f"{Fore.GREEN}----------------------{Style.RESET_ALL}")
        print("IP Address :", data.get("ipAddress"))
        print("Country    :", data.get("countryName"))
        print("Country Code:", data.get("countryCode"))
        print("State/Region:", data.get("stateProv"))
        print("City       :", data.get("city"))
    else:
        print("Error fetching data...")


else:
    print(f"{Fore.RED}You Only Got 500 Chances To Search ...!!!!!{Style.RESET_ALL}")
    ip = input("Enter IP address: ")

    url = f"https://api.db-ip.com/v2/free/{ip}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nIP Geolocation Result")
        print(f"{Fore.GREEN}----------------------{Style.RESET_ALL}")
        print("IP Address :", data.get("ipAddress"))
        print("Country    :", data.get("countryName"))
        print("Country Code:", data.get("countryCode"))
        print("State/Region:", data.get("stateProv"))
        print("City       :", data.get("city"))
    else:
        print("Error fetching data...")