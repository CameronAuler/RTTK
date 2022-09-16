# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the data required for the RTTK application. """

history = []

def menu_db(menu):
    """This function contains all of the menus for the program."""

    menu_list = {
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS", "HELP", "QUIT"],
        "osint": ["SQUEEGEE", "SCANNER", "BACK"],
        "probe": ["NET SCAN", "BACK"],
        "attack": ["CVE DB", "CRACK", "BACK"],
        "notes": ["CHANGE NOTES DIRECTORY", "BACK"],
        "anonymity" : ["PROXY PONG", "BACK"],
        "options": ["MENU SETTINGS", "PROXY SETTINGS", "NOTES SETTINGS", "BACK"]
    }
    return menu_list[menu]

def command_db(menu):
    """This function contains all of the menus for the program."""

    command_list = {
        "main": ["clear", "cls"],
        "anonymity": ["ANONYMITY", "A"],
        "osint": ["OSINT", "O"],
        "probe": ["PROBE", "P"],
        "attack": ["ATTACK", "ATK"],
        "notes": ["cnd"],
        "back": ["BACK", "B"],
        "options": ["MENU SETTINGS", "PROXY SETTINGS", "NOTES SETTINGS", "BACK"],
        "help": ["HELP", "H"],
        "quit": ["QUIT", "Q"]
    }
    return command_list[menu]