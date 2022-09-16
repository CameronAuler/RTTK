# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the menu class and all of the menus for the RTTK project."""
import sys
import time
import functions
from colors import Colors
import put
import notes
import app_data
import options
import documentation

def menu_history(menu_record):
    """This function contains all of the menu history for the RTTK project."""
    if menu_record in app_data.history:
        pass
    else:
        app_data.history.append(menu_record)

class Menu:
    """This is the class for all of the menus in the RTTK project."""

    def display_menu(self, name):
        """This function displays the menu for the current menu for the RTTK project."""
        for _key, value in enumerate(app_data.menu_db(name)):
            print(f"\n{Colors.white}[+]{Colors.end}{Colors.cyan}   -->   {value}{Colors.end}", end="")
            for _key, value in enumerate(app_data.command_db(value.lower())):
                print(f"\t{Colors.black}   <{value}>{Colors.end}", end="")
        print("\n")

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

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    name = app_data.history[0]
    menu_setup(name)

def notes_menu():
    """This function displays the notes menu."""
    # name = "notes"
    notes.notes_setup()
    time.sleep(1)
    back()

def display_options():
    """This function displays the options menu."""
    # name = "options"
    options.options_setup()
    time.sleep(1)
    back()

def help_page():
    """This function contains the documentation for how to use the RTTK application."""
    functions.set_ui()

    documentation.help_setup()
    put.user_input()



def quit_app():
    """This function quits the RTTK application."""
    print("Quiting >>>")
    functions.threader(functions.load())
    sys.exit()
