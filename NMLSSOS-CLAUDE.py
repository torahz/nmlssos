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
        self.clear_screen()
        ip = input("Enter IP: ")
        try:
            socket.inet_aton(ip)
            print("IP Trace:")
            print("---------")
            print("IP:", ip)
            print("Hostname:", socket.gethostbyaddr(ip)[0])
            response = requests.get(f"https://ipapi.co/{ip}/json/")
            data = response.json()
            print("Country:", data.get('country_name', 'Unknown'))
            print("City:", data.get('city', 'Unknown'))
        except socket.error:
            print("Invalid IP")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")
        self.clear_screen()

    def social_media(self):
        self.clear_screen()
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
        self.clear_screen()

    def domain_info(self):
        self.clear_screen()
        domain = input("Enter domain: ")
        try:
            whois_data = whois.whois(domain)
            print("Domain Info:")
            print("------------")
            print("Domain:", domain)
            print("Registrar:", whois_data.registrar)
            print("Created:", whois_data.creation_date)
            print("Updated:", whois_data.updated_date)
        except whois.exceptions.UnknownTld:
            print("Unknown domain")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")
        self.clear_screen()

    def name_search(self):
        self.clear_screen()
        name = input("Enter name: ")
        print("Name Search:")
        print("------------")
        print("Google Dork:", f"site:google.com {name}")
        print("GHDB:", f"{name} GHDB")
        input("Press Enter to continue...")
        self.clear_screen()

    def phone_info(self):
        self.clear_screen()
        phone = input("Enter phone number: ")
        print("Phone Info:")
        print("------------")
        print("Phone Number:", phone)
        # Implement phone number lookup logic here
        input("Press Enter to continue...")
        self.clear_screen()

    def email_search(self):
        self.clear_screen()
        email = input("Enter email: ")
        print("Email Search:")
        print("------------")
        print("Email:", email)
        # Implement email lookup logic here
        input("Press Enter to continue...")
        self.clear_screen()

    def exit_program(self):
        self.clear_screen()
        print("Exiting program")
        os._exit(0)

    def main_menu(self):
        while True:
            self.print_menu()
            choice = input("Enter choice: ")
            if choice in self.menu:
                self.menu[choice]()
            else:
                print("Invalid choice")
                input("Press Enter to continue...")
                self.clear_screen()

if __name__ == "__main__":
    print("WARNING: This tool is for educational purposes only. Use responsibly and ethically.")
    input("Press Enter to continue...")
    osint = NMLSS_OSINT()
    osint.main_menu()