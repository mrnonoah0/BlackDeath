try:
    from tkinter import messagebox
    import re
    import pyzipper
    import os
except Exception as e:
    input(e)

option_1_txt = "Username-Search"

menu = f""" 1: {option_1_txt}
"""

def Menu():
    print(menu)
    messagebox.showinfo("Black Death", "Welcome to Black Death!\n\n"    )

Menu()

while True:
    try:
        choice = input("Choose an option: ")
        options =  {
            "1": option_1_txt,
        }

        if choice in options:
            print(f"You chose {options[choice]}")
            os.system(f"python Programs/{options[choice]}.py")
        elif choice == ["clear", "Clear", "CLEAR", "cls"]:
            os.system("cls")
        elif choice == ["exit", "Exit", "EXIT", "quit", "QUIT", "Quit"]:
            exit()
        elif choice == ["help", "Help", "HELP"]:
            print("Options:\nclear - Clear the console\nexit - Exit the program\nhelp - Show this help message")

    except Exception as e:
        input(e)