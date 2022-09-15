# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""

import os
import time
from sys import platform
import options
import db

def clear():
    """This function clears the terminal window."""
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    else:
        return platform

def main_title():
    """This function prints the ASCII logo."""

    clear()

    print(r"""
          _____                _____                _____                      _____          
         /\    \              /\    \              /\    \                    /\    \         
        /::\    \            /::\    \            /::\    \                  /::\____\        
       /::::\    \           \:::\    \           \:::\    \                /:::/    /        
      /::::::\    \           \:::\    \           \:::\    \              /:::/    /         
     /:::/\:::\    \           \:::\    \           \:::\    \            /:::/    /          
    /:::/__\:::\    \           \:::\    \           \:::\    \          /:::/____/           
   /::::\   \:::\    \          /::::\    \          /::::\    \        /::::\    \           
  /::::::\   \:::\    \        /::::::\    \        /::::::\    \      /::::::\____\________  
 /:::/\:::\   \:::\____\      /:::/\:::\    \      /:::/\:::\    \    /:::/\:::::::::::\    \ 
/:::/  \:::\   \:::|    |    /:::/  \:::\____\    /:::/  \:::\____\  /:::/  |:::::::::::\____\ 
\::/   |::::\  /:::|____|   /:::/    \::/    /   /:::/    \::/    /  \::/   |::|~~~|~~~~~     
 \/____|:::::\/:::/    /   /:::/    / \/____/   /:::/    / \/____/    \/____|::|   |          
       |:::::::::/    /   /:::/    /           /:::/    /                   |::|   |          
       |::|\::::/    /   /:::/    /           /:::/    /                    |::|   |          
       |::| \::/____/    \::/    /            \::/    /                     |::|   |          
       |::|  ~|           \/____/              \/____/                      |::|   |          
       |::|   |                                                             |::|   |          
       \::|   |                                                             \::|   |          
        \:|   |                                                              \:|   |          
         \|___|                                                               \|___|          

----------------------------------------------------------------------------------------------
______________________________________________________________________________________________
----------------------------------------------------------------------------------------------
      """)

def main_menu():
    """This function prints out the main menu options."""
    for index, phase in enumerate(db.menus("main")):
        print(f"[+]   -->   {index}. {phase}")

    print(" ")
    print(" ")

def user_input():
    """This function gathers the user input."""
    user_entry = str(input("\n<>   COMMAND: "))
    user_selection = user_entry.upper()

    if user_selection == "ANONYMITY":
        anonymity_menu()
    elif user_selection == "OSINT":
        osint_menu()
    elif user_selection == "PROBE":
        probe_menu()
    elif user_selection == "ATTACK":
        attack_menu()
    elif user_selection == "NOTES":
        notes_menu()
    elif user_selection == "OPTIONS":
        display_options()
    else:
        print("")
        print("Unrecognized attack phase . . .")
        for _each_number in range(options.options("menu_length")):
            time.sleep(0.001)
            print("=", end="")
        print("")
        user_input()

def anonymity_menu():
    """This function displays the list of identity masking tools."""
    return print("This is the anonymity tool menu.")

def osint_menu():
    """This function displays the list of OSINT tools."""
    return print("This is the OSINT tool menu.")

def probe_menu():
    """This function displays the list of probing tools."""
    return print("This is the Probe tool menu.")

def attack_menu():
    """This function displays the list of attack tools."""
    return print("This is the attack tool menu.")

def notes_menu():
    """This function displays the notes menu."""

def display_options():
    """This function displays the options menu."""

main_title()
main_menu()
user_input()
