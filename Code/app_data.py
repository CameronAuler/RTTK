# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the data required for the RTTK application. """

menu_history = []
commands = ["help", "back", "home", "notes", "options"]

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
        "home": ["home", "main"],
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

dict_dict = {
        # MENUS
        "main": "",
        "anonymity": "",
        "osint": "",
        "probe": "",
        "attack": "",
        "notes": "",
        "back": "",
        "options": "",
        "help": "",
        "quit": "",
        # TOOLS
        "net scan": "Network scanner.",
        "proxy pong": "",
        "squeegee": "Web & Email scraper.",
        "vuln scan": "Vulnerability scanner.",
        "krod": "Google OSINT tool.",
        "doS": "dos.dos()",
        "cve db": "",
        "crack": ""
    }

def menu_db(menu):
    """This function contains all of the menus for the program."""
    return menu_dict.get(menu)

def command_db(menu):
    """This function contains all of the menus for the program."""
    return command_dict.get(menu)

def dict_db(menu):
    """This function contains all of the definitions for the program."""
    return dict_dict.get(menu)
