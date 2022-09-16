# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""
import menus
import functions

def main():
    """__main__"""
    functions.threader(functions.load())
    functions.main_title()
    menus.main_menu()

if __name__ == "__main__":
    main()
