from os import system, _exit
from colorama import Fore, init
from .account import account

init()

def clear():
    system("cls")
    
def accept_int(prompt:str=None, length:int=None) -> int:

    prompt = f"{Fore.BLUE}   " if prompt is None else prompt

    while True:
        try:
            response = int(input(prompt))

            if length is not None and len(str(response)) != length:
                print(f"\n{Fore.RED}Please enter a {length}-digit integer!")
                continue
            
            return response
        except KeyboardInterrupt:
            _exit(1)
        except:
            print(f"\n{Fore.RED}Please enter an integer!")

def accept_account(database, **args) -> account:
    print(f"{Fore.GREEN} Welcome to Baines banking system, please enter your 6 digit pin to login:")
    return account(database, accept_int(length=6), **args)


def confirm():
    input(f"{Fore.GREEN}Please press enter to continue\n   ")