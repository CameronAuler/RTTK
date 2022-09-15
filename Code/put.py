# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the user input for the RTTK project."""

import menus
import functions

def user_input():
    """This function gathers the user input."""
    user_entry = str(input("\n<>   COMMAND: "))
    user_selection = user_entry.upper()
    return main_menu_selection(user_selection)

def main_menu_selection(user_selection):
    """This function translates the user input for the main menu."""
    if user_selection == "ANONYMITY" or user_selection == "A":
        menus.anonymity_menu()
    elif user_selection == "OSINT" or user_selection == "O":
        menus.osint_menu()
    elif user_selection == "PROBE" or user_selection == "P":
        menus.probe_menu()
    elif user_selection == "ATTACK" or user_selection == "ATK":
        menus.attack_menu()
    elif user_selection == "NOTES" or user_selection == "N":
        menus.notes_menu()
    elif user_selection == "OPTIONS" or user_selection == "OPT":
        menus.display_options()
    else:
        print("Unrecognized attack phase . . .")
        functions.set_speed(functions.load())
        user_input()
