from string import printable
from random import choice
from tkinter import *
from os import _exit, startfile, getcwd

root = Tk()
root.geometry("500x500")
root.title("Random password generator")

text = Label(root, text="How many passwords would you like to generate?")
text.pack(pady=(20, 0))

amount = Text(root, width=5, height=1)
amount.pack(pady=(20, 0))


global abc

abc = list("ABCDEFGHIJKLMOPQURSTVWYXZabcdefghijklmopqurstvwxyz1234567890")

def generate(amount):
    passwords = []

    amount = int(amount.get("1.0", END))

    for x in range(amount):
        passwords.append("".join([choice(abc) for x in range(30)]))

    with open("./passwords.txt", "w") as file:
        file.write("\n".join(passwords))
    
    startfile(f"{getcwd()}/passwords.txt")
    _exit(0)

Button(root, text="Generate", command=lambda: generate(amount)).pack(pady=(20, 0))
root.mainloop()