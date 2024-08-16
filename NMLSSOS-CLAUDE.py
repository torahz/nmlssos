import os
import socket
import whois
import requests
from bs4 import BeautifulSoup

class NMLSS_OSINT:
    def __init__(self):
        self.menu = {
            '1': self.ip_trace,
            '2': self.social_media,
            '3': self.domain_info,
            '4': self.name_search,
            '5': self.phone_info,
            '6': self.email_search,
            '0': self.exit_program
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self):
        self.clear_screen()
        print("NMLSS OSINT")
        print("-----------")
        print("1. IP")
        print("2. Social Media")
        print("3. Domain")
        print("4. Name")
        print("5. Phone")
        print("6. Email")
        print("0. Exit Program")

    def ip_trace(self):
        ip = input("Enter IP: ")
        try:
            socket.inet_aton(ip)
            print("IP Trace:")
            print("---------")
            print("IP:", ip)
            print("Hostname:", socket.gethostbyaddr(ip)[0])
            # Use an IP geolocation API for more accurate information
            response = requests.get(f"https://ipapi.co/{ip}/json/")
            data = response.json()
            print("Country:", data.get('country_name', 'Unknown'))
            print("City:", data.get('city', 'Unknown'))
        except socket.error:
            print("Invalid IP")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def social_media(self):
        name = input("Enter name: ")
        print("Social Media:")
        print("------------")
        platforms = {
            "Facebook": f"https://www.facebook.com/{name}",
            "Twitter": f"https://twitter.com/{name}",
            "Instagram": f"https://www.instagram.com/{name}",
            "LinkedIn": f"https://www.linkedin.com/in/{name}"
        }
        for platform, url in platforms.items():
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{platform}: {url} (Profile exists)")
            else:
                print(f"{platform}: Profile not found")
        input("Press Enter to continue...")

    # ... (other methods remain the same)

    def main_menu(self):
        while True:
            self.print_menu()
            choice = input("Enter choice: ")
            if choice in self.menu:
                self.menu[choice]()
            else:
                print("Invalid choice")
                input("Press Enter to continue...")

if __name__ == "__main__":
    print("WARNING: This tool is for educational purposes only. Use responsibly and ethically.")
    input("Press Enter to continue...")
    osint = NMLSS_OSINT()
    osint.main_menu()