# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the menu class and all of the menus for the RTTK project."""
import functions
import put

def menu_db(menu):
    """This function contains all of the menus for the program."""
    menu_list = {
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS", "BACK"],
        "osint": ["SQUEEGEE", "SCANNER", "BACK"],
        "probe": ["NET SCAN", "BACK"],
        "attack": ["CVE DB", "CRACK", "BACK"],
        "notes": ["BACK"],
        "anonymity" : ["PROXY PONG", "BACK"],
        "options": ["MENU SETTINGS", "PROXY SETTINGS", "NOTES SETTINGS"]
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

def main_menu():
    """This function displays the list of identity maskidng tools."""
    functions.set_ui()
    Menu().display_menu("main")
    put.user_input()

def anonymity_menu():
    """This function displays the list of identity masking tools."""
    functions.set_ui()
    Menu().display_menu("anonymity")
    put.user_input()

def osint_menu():
    """This function displays the list of OSINT tools."""
    functions.set_ui()
    Menu().display_menu("osint")
    put.user_input()

def probe_menu():
    """This function displays the list of probing tools."""
    functions.set_ui()
    Menu().display_menu("probe")
    put.user_input()

def attack_menu():
    """This function displays the list of attack tools."""
    functions.set_ui()
    Menu().display_menu("attack")
    put.user_input()

def notes_menu():
    """This function displays the notes menu."""
    functions.set_ui()
    Menu().display_menu("notes")
    put.user_input()

def display_options():
    """This function displays the options menu."""
    functions.set_ui()
    Menu().display_menu("options")
    put.user_input()
