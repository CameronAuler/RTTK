# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""
import sys
import menus
import functions

def rttk():
    """__main__"""
    
    if len(sys.argv) > 1:
        print("Command Passed through command line with the following arguments . . .")
        print(sys.argv)
    else:
        # Loading animation
        functions.load()
        # Setup the menu
        menus.menu_setup(['main'])

if __name__ == "__main__":
    rttk()