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
import functions
import notes
import options

# Imports all of the tools fro mteh tools package
from tools import *

def user_input():
    '''This function gathers the user input within shell mode.'''
    # Input command retains user input from the terminal
    user_entry = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}RTTK{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    
    # Seperates the input string using spaces as deviders and stores values in a list
    command_list = user_entry.split()
    
    # Searches the command in the command database for the corresponding menu/tool and converts the input to the menu/tool name
    cmd = command_list[0]
    command_list[0] = search_db(cmd)
    
    # Converts the list of seperated flags into a tuple for more efficient handling
    command = tuple(command_list)
    
    # Debug Line
    #print(f"passed to input_processor() . . .\n-----------------------------------\ncommand: {command}\ncommand length: {len(command)}\ncommand type: {type(command)}")

    # passes the command tuple to the input_processor function
    input_processor(command)

# Processes commands passed through shell mode associated with tools
def tool_input(tool):
    '''Processes comands associated with tools.'''
    # Still needs to be updated, may combine with user input

    # Takes in user input within shell mode for the tool specified in previous commands
    tool_entry = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}{tool.upper()}{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    flag_list = tool_entry.split()
    flags = tuple(flag_list)
    return flags

# Searches the command database associated with shell mode
def search_db(user_selection):
    """This function searches the command_dict to determine the menu or tool that the command runs"""
    # searches through the command_dict for the commands associated with a specific key word.
    for key, value in app_data.command_dict.items():
        for item in value:
            if user_selection == item:
                # print(f"{Colors.green}SUCCESS >>>{Colors.end}")
                return key
            else:
                pass


def list_to_tuple(command):
    # Convert list to tuple (for sys.argv list)
    if isinstance(command, list):
        temporary_tuple = command
        command = tuple(temporary_tuple)
        return command
    else:
        return command


# The tool_cmd_eval function takes the tool name and any flags that were passed with the tool name and passes the flags to the corresponding tool function.
def tool_cmd_eval(tool, flags):
    if tool == 'proxy pong':
        proxy_pong.proxy_pong()
    elif tool == 'dnum':
        dnum.dnum()
    elif tool == 'sqeegee':
        squeegee.squeegee()
    elif tool == 'net scan':
        net_scan.net_scan(flags)
    elif tool == 'cve db':
        cvedb.cvedb()
    elif tool == 'vuln scan':
        vscan.vscan()
    elif tool  == 'pyfi':
        pyfi.pyfi()
    elif tool == 'crack':
        crack.crack()
    elif tool == 'brutus':
        brutus.brutus()
    else:
        print(f"{Colors.red}INVALID COMMAND>>>{Colors.end}")

def fun_cmd_eval(fun_cmd):
    if fun_cmd == 'home':
        menus.home()
    elif fun_cmd == 'help':
        menus.help()
    elif fun_cmd == 'back':
        functions.back()
    elif fun_cmd == 'clear':
        functions.clear()
        put.input_processor((app_data.menu_history[-1],))
    elif fun_cmd =='quit':
        menus.quit()
    else:
        print(f"{Colors.red}INVALID COMMAND>>>{Colors.end}")


def utility_eval(utility, flags):
    if utility == 'options':
        options.options_setup(flags)
    elif utility == 'notes':
        notes.notes_setup(flags)
    else:
        print(f"{Colors.red}INVALID COMMAND>>>{Colors.end}")

def cli_cmd_eval(command):
    # If the only command is the rttk command
    if len(command) == 1:
        # Display Home screen
        menus.home()
        
    elif len(command) >= 2 and search_db(command[1]) in app_data.command_dict:
        # Sets the name of the tool to the variable tool
        tool = search_db(command[1])
        flags = command[2:]
        tool_cmd_eval(tool, flags)
        
    else:
        print(f"{Colors.red}INVALID COMMAND>>>{Colors.end}")

def input_processor(command):
    '''This function processes all of the input for RTTK through the CLI and through shell mode.'''
    
    # Converts the command list to a tuple for better memory management
    command = list_to_tuple(command)
    
    # Debug line
    #print(f"passed from input_processor() . . .\n-----------------------------------\ncommand: {command}\ncommand length: {len(command)}\ncommand type: {type(command)}")
    #time.sleep(1)
    
    # References the parent command of the input
    parent_cmd = command[0]
    
    # If the program was run through the CLI
    if parent_cmd == 'rttk.py' or parent_cmd == 'c:\\Users\\CM8817\\Github\\RTTK\\Code\\rttk.py':
        cli_cmd_eval(command)
        
    # Utility Command Proccessing
    elif parent_cmd in app_data.functional_commands:
        fun_cmd_eval(parent_cmd)
    
    elif parent_cmd in app_data.utilities:
        util = command[0]
        flags = command[1:]
        utility_eval(parent_cmd, flags)
        
    # Menu Command Proccessing
    elif parent_cmd in app_data.menu_dict:
        # Record the name of the tool/menu in history list in the put module
        menus.record_menu_history(parent_cmd)
        # Displays the menu corresponding with name
        menus.Menu().display_menu(parent_cmd)
        # Prompts user input
        put.user_input()

    # Tool Command Proccessing
    elif parent_cmd in app_data.tool_dict:
        tool = command[0]
        flags = command[1:]
        tool_cmd_eval(tool, flags)
        
    else:
        print('There is no such RTTK command.')
        user_input()
