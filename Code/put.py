# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the user input for the RTTK project."""

import time
import sys
import menus
from colors import Colors
import app_data
import put
import menus

# Imports all of the tools fro mteh tools package
from tools import *

def user_input():
    '''This function gathers the user input within shell mode.'''
    # Input command retains user input from the terminal
    user_entry = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}RTTK{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    
    # Seperates the input string using spaces as deviders and stores values in a list
    command_list = user_entry.split()
    
    # Searches the command in the command database for the corresponding menu/tool and converts the input to the menu/tool name
    command_list[0] = search_db(command_list[0])
    
    # Converts the list of seperated flags into a tuple for more efficient handling
    command = tuple(command_list)
    
    # passes the command tuple to the input_processor function
    input_processor(command)


# Processes commands passed through shell mode associated with tools
def command_input():
    '''Processes comands associated with tools.'''
    # Still needs to be updated, may combine with user input
    
    # Takes in user input within shell mode for the tool specified in previous commands
    command = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}TOOL{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    
    flags = command.split()
    command_search = put.search_db(flags[0])
    if command_search in app_data.command_dict.get('main'):
        flags = [command_search]
        menus.menu_setup(flags)
    else:
        return flags

# Searches the command database associated with shell mode
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



def input_processor(command):
    # Convert list to tuple (for sys.argv list)
    if isinstance(command, list):
        command = tuple(command)
    else:
        pass
    
    # References the parent command of the input
    parent_cmd = command[0]
    
    # CLI PROCESSING
    # Checks for the RTTK shell mode initiation (only rttk.py passed as an argument)
    if len(command) == 1 and parent_cmd == 'rttk.py':
        menus.home()
    else:
        pass
    
    # SHELL PROCESSING
    if len(command) == 1:
        # Menu functionality handling
        if parent_cmd == 'home':
            menus.home()
            
        elif parent_cmd == 'back':
            menus.back()
            
        elif parent_cmd =='quit':
            menus.quit()
            
        elif parent_cmd in app_data.menu_dict:
            # If the name of the tool/menu is in the menu_dict dictionary in app_data and its value is a list
            # Record the name of the tool/menu in memory

            menus.record_menu_history(parent_cmd)
            # Displays the menu corresponding with name
            menus.Menu().display_menu(parent_cmd)
            # Prompts user input
            put.user_input()
        else:
            print(parent_cmd)
            print(type(parent_cmd))
            print('this menu functionality has not been added yet.')
    else:
        # Tool Handling
        print(parent_cmd)
        print(type(parent_cmd))
        print('the functionality of passing multiple arguments through the shell is currently being redone.')