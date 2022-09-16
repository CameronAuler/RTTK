# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the menu class and all of the menus for the RTTK project."""
import sys
import functions
import put

history = []

def menu_history(menu_record):
    """This function contains all of the menu history for the RTTK project."""
    if menu_record in history:
        pass
    else:
        history.append(menu_record)

def menu_db(menu):
    """This function contains all of the menus for the program."""
    menu_list = {
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS", "QUIT"],
        "osint": ["SQUEEGEE", "SCANNER", "BACK"],
        "probe": ["NET SCAN", "BACK"],
        "attack": ["CVE DB", "CRACK", "BACK"],
        "notes": ["BACK"],
        "anonymity" : ["PROXY PONG", "BACK"],
        "options": ["MENU SETTINGS", "PROXY SETTINGS", "NOTES SETTINGS", "BACK"]
    }
    return menu_list[menu]

class Menu:
    """This is the class for all of the menus in the RTTK project."""

    def display_menu(self, name):
        """This function displays the menu for the menu class."""
        for index, item in enumerate(menu_db(name)):
            print(f"[+]   -->   {index}. {item}")
        print(" ")

    def user_input(self):
        """This function gathers the user input."""
        user_entry = str(input("\n<>>> "))
        user_selection = user_entry.upper()
        return put.menu_selection(user_selection)

def menu_setup(name):
    """This function sets up each menu for the RTTK project."""
    functions.set_ui()
    Menu().display_menu(name)
    menu_history(name)
    put.user_input()

def main_menu():
    """This function displays the list of identity maskidng tools."""
    name = "main"
    menu_setup(name)

def anonymity_menu():
    """This function displays the list of identity masking tools."""
    name = "anonymity"
    menu_setup(name)

def osint_menu():
    """This function displays the list of OSINT tools."""
    name = "osint"
    menu_setup(name)

def probe_menu():
    """This function displays the list of probing tools."""
    name = "probe"
    menu_setup(name)

def attack_menu():
    """This function displays the list of attack tools."""
    name = "attack"
    menu_setup(name)

def notes_menu():
    """This function displays the notes menu."""
    name = "notes"
    menu_setup(name)

def display_options():
    """This function displays the options menu."""
    name = "options"
    menu_setup(name)

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    name = history[0]
    menu_setup(name)

def quit_app():
    """This function quits the RTTK application."""
    sys.exit()

