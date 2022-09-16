# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""
import menus
import functions

#
# Code efficiency tasks . . .
#    - Make menu_setup() function reliable on the command_db
#    and user input to reduce the amount of menu functions in menus.py
#    - Make a db_match() function that matches a menu or tool name to
#    the menu_db() or command_db to view the associated sub-menus or commands.
# UI tasks
#    - Display the command for each menu to to give the user a quick reference.


def main():
    """__main__"""
    functions.threader(functions.load())
    functions.main_title()
    menus.main_menu()

if __name__ == "__main__":
    main()
