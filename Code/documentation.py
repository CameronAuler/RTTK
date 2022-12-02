# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module is for the help display of the RTTK project."""
import app_data
import menus
import functions
from colors import Colors

def help_setup():
    """This function is to setup the help menu for the RTTK application."""
    functions.set_ui()
    # Prints the headers for the help menu
    print(f"             {Colors.black}{Colors.white_bg}Elements{Colors.end}", end="")
    print(f"        {Colors.black}{Colors.white_bg}Commands{Colors.end}", end="")
    print(f"        {Colors.black}{Colors.white_bg}Examples{Colors.end}")
    

    
    
    
    print(f"             {Colors.black}{Colors.white_bg}Tools{Colors.end}", end="")
    print(f"        {Colors.black}{Colors.white_bg}Commands{Colors.end}", end="")
    print(f"        {Colors.black}{Colors.white_bg}Examples{Colors.end}")
    
    for key in app_data.tool_dict:
        print(f"\n{Colors.white}[+]{Colors.end}{Colors.cyan}  -->    {key}{Colors.end}", end="")
        for value in app_data.command_dict.get(key):
            print(f"\t     {Colors.black}{value}{Colors.end}", end="")
        if key in app_data.tool_dict:
            print(f"\t     {Colors.black}{app_data.tool_dict.get(key)[1]}{Colors.end}", end="")
        
    
