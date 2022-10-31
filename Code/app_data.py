# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the data required for the RTTK application. """

menu_history = []
commands = ["help", "back", "notes", "options", "clear"]

menu_dict = {
        # Menus
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS", "QUIT"],
        "anonymity" : ["PROXY PONG"],
        "osint": ["DNUM", "SQUEEGEE", "NET SCAN", "CVE DB"],
        "probe": ["VULN SCAN", "pyfi"],
        "attack": ["CRACK", "BRUTUS"],
    }

command_dict = {
        # MENUS
        "main": ["help", "back", "home", "notes", "options"],
        "anonymity": ["anonymity", "a"],
        "osint": ["osint", "o"],
        "probe": ["probe", "p"],
        "attack": ["attack", "atk"],
        "notes": ["notes", "n"],
        "options": ["options", "opt"],
        "back": ["back", "b"],
        "help": ["help", "h"],
        "quit": ["quit", "q"],
        "clear": ["clear", "cls"],
        "home": ["home"],
        # TOOLS
        "pyfi": ["pyfi", "pi"],
        "dnum": ["dnum", "dn"],
        "net scan": ["nscan", "ns"],
        "proxy pong": ["xpong", "xp"],
        "squeegee": ["squg", "sq"],
        "vuln scan": ["Vscan", "vs"],
        "krod": ["krod", "kd"],
        "doS": ["dos", "ds"],
        "cve db": ["cvb", "cb"],
        "crack": ["crack", "ck"],
        "brutus": ["brute", "bt"]
    }

tool_dict = {
        "pyfi": ["pyfi", "pi"],
        "dnum": ["dnum", "dn"],
        "net scan": ["nscan", "ns"],
        "proxy pong": ["xpong", "xp"],
        "squeegee": ["squg", "sq"],
        "vuln scan": ["Vscan", "vs"],
        "krod": ["krod", "kd"],
        "doS": ["dos", "ds"],
        "cve db": ["cvb", "cb"],
        "crack": ["crack", "ck"],
        "brutus": ["brute", "bt"]
    }

def menu_db(menu):
    """This function contains all of the menus for the program."""
    return menu_dict.get(menu)

def command_db(menu):
    """This function contains all of the menus for the program."""
    return command_dict.get(menu)
