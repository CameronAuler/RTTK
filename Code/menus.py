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
import pyfi
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

def menu_setup(flag_list):
    """This function sets up each menu for the RTTK project."""
    name = flag_list[0]
    functions.set_ui()
    
    for item in flag_list:
        if item in app_data.command_dict.get("main"):
            if name == "back":
                back()
            elif name == "help":
                help_page()
            elif name == "home":
                home()
            elif name == "notes":
                notes_menu()
            elif name == "options":
                display_options()
            elif name == "quit":
                quit_app()
            else:
                pass
    
    if isinstance(app_data.menu_dict.get(name), list):
        record_menu_history([name])
        Menu().display_menu(name)
        put.user_input()
    else:
        record_menu_history([name])
        if name == "proxy pong":
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
        else:
            print(name)
            print("INVALID COMMAND")
            time.sleep(2)
            back()

def home():
    """This command takes the user to the main menu."""
    functions.set_ui()
    Menu().display_menu("main")
    put.user_input()

def back():
    """This function goes back to the last menu in the menu history of the RTTK project."""
    if len(app_data.menu_history) >= 2:
        name = app_data.menu_history[-2]
        app_data.menu_history.pop()
    else:
        name = ["main"]
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
    
    
