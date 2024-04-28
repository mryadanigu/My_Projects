#!/usr/bin/python3

import os
from time import sleep

try:
    from colorama import init, Fore
except ImportError:
    print('\n[!] Import Error.')
    print('Please check colorama library is correctly installed.')
    exit(1)

init()
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
cyan = Fore.CYAN
reset = Fore.RESET

try:
    class ATM:
        def __init__(self):
            self.users = {
                "dagi": {"pin": "1234", "balance": 1000},
                "leul": {"pin": "5678", "balance": 500}
                }

        def authenticate_user(self, username, pin):
            """Authenticate the user by checking the provided username and pin."""
            if username in self.users and self.users[username]["pin"] == pin:
                pp = "--  " * len(username)
                qq = "" * len(username)
                print(yellow + f"""\n 
  {pp}
; Welcome, {username}! {qq};
  {pp}""" + reset)
                return True
            else:
                print(red, "\nAuthentication failed. Invalid username or PIN.", reset)
                sleep(2)
                os.system("clear")
                return False

        def check_balance(self, username):
            """Check and print the user's balance."""
            balance = self.users[username]["balance"]
            print(green + f"\nYour current balance is: ${balance:.2f}" + reset)
            sleep(3)
            os.system("clear")

        def deposit(self, username, amount):
            """Deposit an amount to the user's account."""
            if amount <= 0:
                print(red + "\nAmount must be greater than zero." + reset)
                sleep(2)
                os.system("clear")
                return
            self.users[username]["balance"] += amount
            print(green + f"\nSuccessfully deposited ${amount:.2f}. Your current balance is ${self.users[username]['balance']:.2f}" + reset)
            sleep(2)
            os.system("clear")

        def withdraw(self, username, amount):
            """Withdraw an amount from the user's account."""
            if amount <= 0:
                print(red + "\nAmount must be greater than zero." + reset)
                sleep(2)
                os.system("clear")
                return
            if amount > self.users[username]["balance"]:
                print(red + "\nInsufficient funds. Please recharge your account." + reset)
                sleep(2)
                os.system("clear")
                return
            self.users[username]["balance"] -= amount
            print(green + f"\nSuccessfully withdrew ${amount:.2f}. Your current balance is ${self.users[username]['balance']:.2f}" + reset)
            sleep(2)
            os.system("clear")

    def atm_interface():
        atm = ATM()
        print(green + "\n Welcome to the ATM." + reset)

        # Ask the user for credentials
        username = input(blue + "\n[*] Enter your username: ".title() + reset)
        pin = input(blue + "\n[*] Enter your PIN: " + reset)

        # Authenticate the user
        if not atm.authenticate_user(username, pin):
            return

        # Provide the user with options
        while True:
            sleep(1)
            print("\nPlease select an option:")
            print(green)
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print(reset)
        
            choice = input(blue + "Enter your choice: " + green)

            if choice == "1":
                atm.check_balance(username)
            elif choice == "2":
                amount = float(input(green + "\nEnter the amount to deposit: " + reset))
                atm.deposit(username, amount)
            elif choice == "3":
                amount = float(input(green + "\nEnter the amount to withdraw: " + reset))
                atm.withdraw(username, amount)
            elif choice == "4":
                print(yellow + "\nThank you for using the ATM. Goodbye!" + reset)
                break
            else:
                print(red + "Invalid choice. Please try again." + reset)
                sleep(2)
                os.system("clear")

    if __name__ == '__main__':
        atm_interface()

except KeyboardInterrupt:
    print(red + "\n\n[-] Admin request exitting..." + reset)
    sleep(2)
    os.system("clear")
    exit(1)

except ValueError:
    print(red + "\nInvalid Input. Please try again." + reset)
    sleep(2)
    os.system("clear")
    exit(1)

except Exception:
    print(red + "\n[!] System Error" + reset)
    sleep(2)
    os.system("clear")
    exit(1)
