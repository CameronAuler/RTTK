# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the user input for the RTTK project."""

import time
import argparse
import menus
from colors import Colors
import app_data
import put

def user_input():
    """This function gathers the user input."""
    # Input command retains user input from the terminal
    user_entry = str(input(f"\n{Colors.magenta}<>>> {Colors.end}"))
    # Defining the user input as user_selection in all lowercase for formating reasons.
    flag_list = user_entry.split()
    name = flag_list[0].lower()
    # the all lowercase user_selection input gets passed to  >>>
    if len(flag_list) > 1 and search_db(name) in app_data.command_dict:
        # the Menu_selection function in the menus module.
        flag_list[0] = search_db(name)
        menus.menu_setup(flag_list)
    else:
        menus.menu_setup([search_db(name)])

def command_input():
    command = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}NET SCAN{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    
    flags = command.split()
    command_search = put.search_db(flags[0])
    if command_search in app_data.command_dict.get('main'):
        flags = [command_search]
        menus.menu_setup(flags)
    else:
        return flags

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
