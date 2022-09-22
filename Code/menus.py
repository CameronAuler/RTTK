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

import proxy_pong
import squeegee
import net_scan
import cvedb
import vscan
import crack

def record_menu_history(menu_record):
    """This function contains all of the menu history for the RTTK project."""
    if menu_record in app_data.menu_history:
        pass
    else:
        app_data.menu_history.append(menu_record)

class Menu:
    """This is the class for all of the menus in the RTTK project."""

    def display_menu(self, name):
        """This function displays the menu for the current menu for the RTTK project."""
        for _key, value in enumerate(app_data.menu_db(name)):
            print(f"\n{Colors.white}[+]{Colors.end}{Colors.cyan}  -->    {value}{Colors.end}", end="")
            for _key, value in enumerate(app_data.command_db(value.lower())):
                print(f"\t{Colors.black}   <{value}>{Colors.end}", end="")

def menu_setup(name):
    """This function sets up each menu for the RTTK project."""
    if name != "back":
        functions.set_ui()
    if isinstance(app_data.menu_dict.get(name), list):
        Menu().display_menu(name)
        record_menu_history(name)
        put.user_input()
    else:
        if name == "proxy pong":
            record_menu_history(name)
            proxy_pong.proxy_pong()
            put.user_input()
        elif name == "squeegee":
            record_menu_history(name)
            squeegee.squeegee()
            put.user_input()
        elif name == "net scan":
            record_menu_history(name)
            net_scan.net_scan()
            put.user_input()
        elif name == "cve db":
            record_menu_history(name)
            cvedb.cvedb()
            put.user_input()
        elif name == "vuln scan":
            record_menu_history(name)
            vscan.vscan()
            put.user_input()
        elif name == "crack":
            record_menu_history(name)
            crack.crack()
            put.user_input()
        elif name == "back":
            back()
        elif name == "notes":
            notes_menu()
        elif name == "options":
            display_options()
        elif name == "help":
            help_page()
        elif name == "quit":
            quit_app()
        elif name == "home":
            home()
        else:
            print("INVALID COMMAND")
            time.sleep(1)
            back()

def home():
    """This command takes the user to the main menu."""
    menu_setup("main")

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    if len(app_data.menu_history) >= 2:
        name = app_data.menu_history[-2]
        app_data.menu_history.pop()
    else:
        name = "main"
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

    documentation.help_setup()
    put.user_input()

def quit_app():
    """This function quits the RTTK application."""
    print("Quiting >>>")
    functions.threader(functions.load())
    sys.exit()
