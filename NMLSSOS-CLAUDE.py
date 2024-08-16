import os
import socket
from geopy.geocoders import Nominatim
from social_analyzer import SocialAnalyzer
import whois
from search_names import SearchNames
import phonenumbers
from osint import Osint

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
        print("1. IP Trace")
        print("2. Social Media")
        print("3. Domain Info")
        print("4. Name Search")
        print("5. Phone Info")
        print("6. Email Search")
        print("0. Exit Program")

    def ip_trace(self):
        self.clear_screen()
        ip = input("Enter IP: ")
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(ip)
            print("IP Trace:")
            print("---------")
            print(f"IP: {ip}")
            print(f"Location: {location.address if location else 'Not found'}")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def social_media(self):
        self.clear_screen()
        name = input("Enter name: ")
        try:
            social_analyzer = SocialAnalyzer()
            social_media = social_analyzer.get_social_media(name)
            print("Social Media:")
            print("------------")
            for platform, url in social_media.items():
                print(f"{platform}: {url}")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def domain_info(self):
        self.clear_screen()
        domain = input("Enter domain: ")
        try:
            whois_data = whois.whois(domain)
            print("Domain Info:")
            print("------------")
            print(f"Domain: {domain}")
            print(f"Registrar: {whois_data.registrar}")
            print(f"Created: {whois_data.creation_date}")
            print(f"Updated: {whois_data.updated_date}")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def name_search(self):
        self.clear_screen()
        name = input("Enter name: ")
        try:
            search_names = SearchNames()
            results = search_names.search(name)
            print("Name Search:")
            print("------------")
            for result in results:
                print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def phone_info(self):
        self.clear_screen()
        phone = input("Enter phone number (with country code): ")
        try:
            phone_number = phonenumbers.parse(phone)
            print("Phone Info:")
            print("------------")
            print(f"Number: {phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            print(f"Is valid: {phonenumbers.is_valid_number(phone_number)}")
            print(f"Region: {phonenumbers.region_code_for_number(phone_number)}")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def email_search(self):
        self.clear_screen()
        email = input("Enter email: ")
        try:
            osint = Osint()
            results = osint.search(email)
            print("Email Search:")
            print("------------")
            for result in results:
                print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

    def exit_program(self):
        self.clear_screen()
        print("Exiting program")
        exit()

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