# RTTK Project
# 9/14/2022
# Cameron Auler

"""This module contains all of the data for the program."""

def menus(menu):
    """This function contains all of the menus for the program."""
    menu_list = {
        "main": ["OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS"],
        "osint": [],
        "probe": [],
        "attack": [],
        "notes": [],
        "options": []
    }
    return menu_list[menu]
