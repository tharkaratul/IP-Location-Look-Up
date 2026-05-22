
import requests
import webbrowser
import ssl
import sys
import socket
from pprint import pprint
from colorama import init, Fore, Style

init()

def info_ip(ip):
    url = f"https://api.db-ip.com/v2/free/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
            data = response.json()

            print("\nIP Geolocation Result")
            print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
            print("IP Address   |", data.get("ipAddress"))
            print("Country      |", data.get("countryName"))
            print("Country Code |", data.get("countryCode"))
            print("State/Region |", data.get("stateProv"))
            print("City         |", data.get("city"))
            print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
    else:
        print("Error fetching data...")

def geo(ip):
    geo = f"https://ipwho.is/{ip}"
    geores = requests.get(geo)
    if geores.status_code == 200:
            geo_data = geores.json()
            isp = geo_data.get("connection", {}).get("isp", "Unknown ISP")
            lat = geo_data.get("latitude")
            lon = geo_data.get("longitude")
            print(f"{Fore.RED}Latitude        |{Style.RESET_ALL}",lat)
            print(f"{Fore.RED}Longitude       | {Style.RESET_ALL}",lon)
            print("Hosting Company | ",isp)
            option = input("Want location on maps(Y/N) :- ").lower()
            if option == "y":
                print("Successfully Done !!!")
                url = f"https://www.google.com/maps?q={lat},{lon}"           
                webbrowser.open(url)
                pass
            elif option == "n":
                print("Fetching SSl ...")
                pass
            else:
                 print("Choose Y/N...")
                 
                 
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
                print(f"{Fore.RED}Valid from {Style.RESET_ALL}", cert["notBefore"])
                print(f"{Fore.RED}Valid until:{Style.RESET_ALL}", cert["notAfter"])
                print(f"{Fore.GREEN}-----------------------------------------------------{Style.RESET_ALL}")
                sys.exit("Sussceful..exit")
    except Exception as e:
        print(f"Error getting SSL info: {str(e)}")
        print("Try entering url")
        sys.exit()
#        return {"error": str(e)}
                        
                
def iplookup_fetch(ip):
        socket.inet_aton(ip)
        info_ip(ip)
        geo(ip)
        domain = ip_input.removeprefix("https://").removeprefix("http://")
        ssl_info(domain)


def main(ip_input):
    alpha_to_remove = ["https://","http://"]
    if any(alpha in ip_input for alpha in alpha_to_remove):
        try:
            print(ip_input)
            response = requests.get(ip_input)
            if response.status_code == 200 or 204:
                ip_input = ip_input.removeprefix("https://").removeprefix("http://")
                ip = socket.gethostbyname(ip_input)
                iplookup_fetch(ip)
            else:
                print("web not reachable")
        except  requests.exceptions.RequestException as e:
            print("check url/network...")         
    else:
        try:
            host_details = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip_input}")
            split = [line.strip() for line in host_details.text.split("\n") if line.strip()]
            if split and "error" not in split[0].lower():
                web_name = split[-1]
                print(f"The domain is: {web_name}")
            else:
                print("Domains not found")
            response = requests.get(f"https://{web_name}")
            if response.status_code == 200 or 204:
                ip = socket.gethostbyname(ip_input)
                info_ip(ip)
                geo(ip)
                domain = ip_input.removeprefix("https://").removeprefix("http://")
                ssl_info(domain)
                sys.exit()
                if OSError:
                    def oserror_handler(url):
                        domain = url.removeprefix("https://").removeprefix("http://")
                        ip = socket.gethostbyname(domain)
                        print(ip)
                        info_ip(ip)
                        geo(ip)
                        ssl_info(domain)
                        sys.exit()
                    oserror_handler(url=ip_input)
            else:
                print("web not reachable")
        except  requests.exceptions.RequestException as e:
             print("invalid : 1")

    def oserror_handler(url):
        domain = url.removeprefix("https://").removeprefix("http://")
        ip = socket.gethostbyname(domain)
        print(ip)
        info_ip(ip)
        geo(ip)
        ssl_info(domain)

ip_input = input("Enter Website Url Or IP Address :- ")

main(ip_input)