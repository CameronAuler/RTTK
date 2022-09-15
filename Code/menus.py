# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the menu class and all of the menus for the RTTK project."""
import functions
import put

def menu_db(menu):
    """This function contains all of the menus for the program."""
    menu_list = {
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS"],
        "osint": [],
        "probe": [],
        "attack": [],
        "notes": [],
        "anonymity" : [],
        "options": ["MENU SETTINGS", "PROXY SETTINGS", "NOTES SETTINGS"]
    }
    return menu_list[menu]

"""
class menu:
    def __init__(self, name):
        self.name = name

    def display_menu():
        for index, item in enumerate(menu_db(self.name)):
            print(f"[+]   -->   {index}. {item}")
    
    display_menu()
    put.user_input()


def main_menu():
    put.main_menu_selection(menu("main"))
"""

def main_menu():
    """This function prints out the main menu options."""
    for index, phase in enumerate(menu_db("main")):
        print(f"[+]   -->   {index}. {phase}")

    print(" ")
    print(" ")

def anonymity_menu():
    """This function displays the list of identity masking tools."""
    functions.set_ui()
    return print("This is the anonymity tool menu.")

def osint_menu():
    """This function displays the list of OSINT tools."""
    functions.set_ui()
    return print("This is the OSINT tool menu.")

def probe_menu():
    """This function displays the list of probing tools."""
    functions.set_ui()
    return print("This is the Probe tool menu.")

def attack_menu():
    """This function displays the list of attack tools."""
    functions.set_ui()
    return print("This is the attack tool menu.")

def notes_menu():
    """This function displays the notes menu."""
    functions.set_ui()
    return print("This is the notes menu.")

def display_options():
    """This function displays the options menu."""
    functions.set_ui()
    for index, setting in enumerate(menu_db("options")):
        print(f"[+]   -->   {index}. {setting}")

    print(" ")
    print(" ")
