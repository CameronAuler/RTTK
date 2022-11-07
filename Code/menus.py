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

# Imports all of the tools fro mteh tools package
from tools import *


def record_menu_history(record):
    """This function contains all of the menu history for the RTTK project."""
    if record not in app_data.menu_history:
        app_data.menu_history.append(record)


# Menu class
class Menu:
    """This is the class for all of the menus in the RTTK project."""

    def display_menu(self, menu):
        '''This function displays the menu for the current menu for the RTTK project.'''
        functions.set_ui()
        for _key, value in enumerate(app_data.menu_db(menu)):
            print(f"\n{Colors.white}[+]{Colors.end}{Colors.cyan}  -->    {value}{Colors.end}", end="")
            for _key, value in enumerate(app_data.command_db(value.lower())):
                print(f"\t{Colors.black}   <{value}>{Colors.end}", end="")





# Main Navigational Function coordinates menus with commands
def menu_setup(flag_list):
    """menu_setup() is the main Navigational Function that coordinates menus with commands."""
    
    # Fixes the double load animation due to loading 2 menus consecutively
    name = flag_list[0]
    
    if name != "back":
        functions.set_ui()
    else:
        pass
    
    # If the name of the tool/menu is in the menu_dict dictionary in app_data and its value is a list
    if isinstance(app_data.menu_dict.get(name), tuple):
        # Record the name of the tool/menu in memory
        record_menu_history([name])
        # Displays the menu corresponding with name
        Menu().display_menu(name)
        # Prompts user input
        put.user_input()
    
    # Tools
    elif name == "proxy pong":
        record_menu_history([name])
        proxy_pong.proxy_pong()
        put.user_input()
    elif name == "squeegee":
        squeegee.squeegee()
        put.user_input()
    elif name == "net scan":
        net_scan.net_scan(flag_list)
    elif name == "cve db":
        cvedb.cvedb()
        put.user_input()
    elif name == "vuln scan":
        vscan.vscan()
        put.user_input()
    elif name == "pyfi":
        pyfi.pyfi()
        put.user_input()
    elif name == "crack":
        crack.crack()
        put.user_input()
    
    #Menu Functions
    # Elif name matches any of these string values run specific menu functionalities corresponding to name
    elif name == "back":
        back()
    elif name == "help":
        help_page()
    elif name == 'home':
        home()
    elif name == "notes":
        notes_menu()
    elif name == "options":
        display_options()
    elif name == "quit":
        quit()
    else:
        print(name)
        print("INVALID COMMAND")
        time.sleep(2)
        sys.exit()




# MENU FUNCTIONALITY
def home():
    '''This command takes the user to the main menu.'''
    Menu().display_menu('home')
    put.user_input()

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    if len(app_data.menu_history) >= 2:
        last_command = app_data.menu_history[-2]
        app_data.menu_history.pop()
    else:
        last_command = ["home"]
    put.input_processor(last_command)

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

    documentation.help_setup()
    put.user_input()

def quit():
    """This function quits the RTTK application."""
    print("Quiting >>>")
    functions.threader(functions.load())
    sys.exit()
    
    
