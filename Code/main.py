# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""
import menus
import functions
import psutil

def main():
    """__main__"""
    # Loading animation
    functions.load()
    # Setup the menu
    menus.menu_setup(['main'])

if __name__ == "__main__":
    main()