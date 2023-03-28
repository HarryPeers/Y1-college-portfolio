from string import printable
from random import choice
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Random password generator")



abc = list(printable)
abc.remove(" ")

length = int(input("Enter the length of the passwords"))
amount = int(input("Enter how many passwords you want to create"))

passwords = []

for x in range(amount):
    passwords.append("".join([choice(abc) for x in range(length)]))

[print(f"{x+1})   {password}") for x, password in zip(range(amount), passwords)]

with open("./passwords.txt", "a") as file:
    file.write("\n".join(passwords)+"\n")