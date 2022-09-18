# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the user input for the RTTK project."""

import time
import menus
from colors import Colors
import app_data

def user_input():
    """This function gathers the user input."""
    # Input command retains user input from the terminal
    user_entry = str(input(f"\n{Colors.magenta}<>>> {Colors.end}"))
    # Defining the user input as user_selection in all lowercase for formating reasons.
    user_selection = user_entry.lower()
    # the all lowercase user_selection input gets passed to  >>>
    # the Menu_selection function in the menus module.
    menus.menu_setup(search_db(user_selection))

def search_db(user_selection):
    """This function searches the command_dict to determine the menu or tool that the command runs"""
    # searches through the command_dict for the commands associated with a specific key word.
    for key, value in app_data.command_dict.items():
        for item in value:
            if user_selection == item:
                print(f"{Colors.green}SUCCESS >>>{Colors.end}")
                time.sleep(0.1)
                return key
            else:
                pass
