# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module is for the help display of the RTTK project."""
import app_data
import menus
from colors import Colors

def help_setup():
    """This function is to setup the help menu for the RTTK application."""
    # Prints the headers for the help menu
    print(f"                           {Colors.black}{Colors.white_bg}Commands{Colors.end}", end="")
    print(f"        {Colors.black}{Colors.white_bg}Keys{Colors.end}")

    # Prints each key of the menu_dict dictionary
    for key, _value in app_data.menu_dict.items():
        print(f"\n{Colors.magenta}{key.upper()}{Colors.end}     \t", end="")
        # References the Menu class in the menus module which contains the function display_menu()
        menus.Menu().display_menu(key)
        # New Line
        print("\n")
