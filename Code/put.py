# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the user input for the RTTK project."""

import menus
from colors import Colors

def user_input():
    """This function gathers the user input."""
    user_entry = str(input(f"\n{Colors.magenta}<>>> {Colors.end}"))
    user_selection = user_entry.upper()
    menu_selection(user_selection)

def menu_selection(user_selection):
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
    elif user_selection == "BACK" or user_selection == "B":
        menus.back()
    elif user_selection == "QUIT" or user_selection == "Q":
        menus.quit_app()
    else:
        menus.menu_setup(menus.history[-1])
        user_input()
