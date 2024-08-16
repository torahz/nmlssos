import os
import socket
import whois
import re
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

    def print_menu(self):
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
            print("Country:", socket.gethostbyaddr(ip)[3][4:])
        except socket.error:
            print("Invalid IP")
        input("Press Enter to continue...")
        self.main_menu()

    def social_media(self):
        name = input("Enter name: ")
        print("Social Media:")
        print("------------")
        print("Facebook:", f"https://www.facebook.com/{name}")
        print("Twitter:", f"https://twitter.com/{name}")
        print("Instagram:", f"https://www.instagram.com/{name}")
        input("Press Enter to continue...")
        self.main_menu()

    def domain_info(self):
        domain = input("Enter domain: ")
        try:
            whois_data = whois.whois(domain)
            print("Domain Info:")
            print("------------")
            print("Domain:", domain)
            print("Registrar:", whois_data.registrar)
            print("Created:", whois_data.creation_date)
            print("Updated:", whois_data.update_date)
        except whois.exceptions.UnknownWhoisServer:
            print("Unknown domain")
        input("Press Enter to continue...")
        self.main_menu()

    def name_search(self):
        name = input("Enter name: ")
        print("Name Search:")
        print("------------")
        print("Google Dork:", f"site:google.com {name}")
        print("GHDB:", f"{name} GHDB")
        input("Press Enter to continue...")
        self.main_menu()

    def phone_info(self):
        phone = input("Enter phone number: ")
        print("Phone Info:")
        print("------------")
        print("Phone Number:", phone)
        # Implement phone number lookup logic here
        input("Press Enter to continue...")
        self.main_menu()

    def email_search(self):
        email = input("Enter email: ")
        print("Email Search:")
        print("------------")
        print("Email:", email)
        # Implement email lookup logic here
        input("Press Enter to continue...")
        self.main_menu()

    def exit_program(self):
        print("Exiting program")
        os._exit(0)

    def main_menu(self):
        self.print_menu()
        choice = input("Enter choice: ")
        if choice in self.menu:
            self.menu[choice]()
        else:
            print("Invalid choice")
            self.main_menu()

if __name__ == "__main__":
    osint = NMLSS_OSINT()
    osint.main_menu()