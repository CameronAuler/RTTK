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


# MENU FUNCTIONALITY
def home():
    '''This command takes the user to the main menu.'''
    record_menu_history('home')
    Menu().display_menu('home')
    put.user_input()

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    print(app_data.menu_history)
    time.sleep(2)
    if len(app_data.menu_history) > 1:
        last_command = (app_data.menu_history[-2],)
        app_data.menu_history.pop()
    else:
        last_command = ("home",)
    
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
    #functions.threader(functions.load())
    print("Quiting >>>")
    sys.exit()
    
    
