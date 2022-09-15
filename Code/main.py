# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""
import menus
import functions
import put

def main():
    """__main__"""
    functions.set_speed(functions.load())
    functions.main_title()
    menus.main_menu()
    put.user_input()

if __name__ == "__main__":
    main()
