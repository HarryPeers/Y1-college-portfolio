from sys import path
from os import getcwd

path.append(f"{getcwd()}/dependancies/")

from colorama import Fore
from modules import modules

database = modules.database()

def print_balace():
    pass

options = {
    "Deposit money": None,
    "Withdraw money": None,
    "View balance": None
}

    
account = modules.interface.accept_account(database, create_missing=True)
modules.interface.clear()
print(f"{Fore.GREEN}You have been succesfully logged in!")

while True:

    for index, option in zip(range(1,1+len(options.keys())), list(options.keys())):
        print(f"   {Fore.YELLOW}{index}){Fore.GREEN} {option}")

    option = modules.interface.accept_int(length=1)

    if option == 1:
        amount = modules.interface.accept_int(f"{Fore.GREEN}Please enter how much you would like to deposit:\n   {Fore.BLUE}")
        account.balance += amount
        print(f"Your balance is now £{account.balance}.")
    elif option == 2:
        amount = modules.interface.accept_int(f"{Fore.GREEN}Please enter how much you would like to withdraw:\n   {Fore.BLUE}")
        account.withdraw(amount)
        print(f"Your balance is now £{account.balance}.")
    elif option == 3:
        print(f"Your balance is £{account.balance}.")

    modules.interface.confirm()
    modules.interface.clear()
    