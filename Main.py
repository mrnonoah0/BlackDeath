try:
    from tkinter import messagebox
    import re
    import pyzipper
    import os
except Exception as e:
    input(e)

option_1_txt = "Username-Search"
option_2_txt = "IP-lookup"

menu = f""" 
1: {option_1_txt}
2: {option_2_txt}
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
            "2": option_2_txt,
        }

        if choice in options:
            print(f"You chose {options[choice]}")
            os.system(f"python Programs/{options[choice]}.py")
        elif choice == "clear":
            os.system("cls")
        elif choice == "exit":
            exit()
        elif choice == "help":
            print("Options:\nclear - Clear the console\nexit - Exit the program\nhelp - Show this help message")
        elif choice == "terminal":
            while True:
                try:
                    command = input()
                    if command.lower() == "exit":
                        break
                    os.system(command)
                except Exception as e:
                    print(f"Error: {e}")

    except Exception as e:
        input(e)