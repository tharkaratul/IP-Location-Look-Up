
import requests
import ssl
import json
import socket
from pprint import pprint
from colorama import init, Fore, Style

init()

def info_ip(ip):
    print(f"{Fore.RED}You Only Got 500 Chances To Search ...!!!!!{Style.RESET_ALL}")
    url = f"https://api.db-ip.com/v2/free/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
            data = response.json()

            print("\nIP Geolocation Result")
            print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
            print("IP Address :", data.get("ipAddress"))
            print("Country    :", data.get("countryName"))
            print("Country Code:", data.get("countryCode"))
            print("State/Region:", data.get("stateProv"))
            print("City       :", data.get("city"))
            print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
    else:
        print("Error fetching data...")

def geo(ip):
    geo = f"https://ipwho.is/{ip}"
    geores = requests.get(geo)
    if geores.status_code == 200:
            geo_data = geores.json()
            isp = geo_data.get("connection", {}).get("isp", "Unknown ISP")
            
            print(f"{Fore.RED}Latitude :- {Style.RESET_ALL}",geo_data.get("latitude"))
            print(f"{Fore.RED}Longitude :- {Style.RESET_ALL}",geo_data.get("longitude"))
            print("Hosting Company :- ",isp)
            
    else:
         print("Error Location Not Found ...")

def ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                #print(json.dumps(cert, indent=4))
                for field in cert["issuer"]:
                    key, value = field[0]
                    if key == "organizationName":
                        print("Issuer Name:",value)
                print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
                print("Valid from:", cert["notBefore"])
                print("Valid until:", cert["notAfter"])
                return cert
    except Exception as e:
        print(f"Error getting SSL info: {e}")
        return {"error": str(e)}

ip_input = input("Enter Website Name Or IP Address :- ")
try:
    socket.inet_aton(ip_input)
    # It's an IP
    ip = ip_input
    info_ip(ip)
    geo(ip)
    print("SSL info not available for IP input.")
except OSError:
    # It's a domain
    domain = ip_input
    ip = socket.gethostbyname(domain)
    info_ip(ip)
    geo(ip)
    ssl_info(domain)
    