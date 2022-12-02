# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the data required for the RTTK application. """

menu_history = []
functional_commands = ("home", "help", "back", "clear", "quit")
utilities = ("notes", "options")

menu_dict = {
        # Menus
        "home": ("ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES", "OPTIONS"),
        "anonymity" : ("PROXY PONG",),
        "osint": ("DNUM", "SQUEEGEE", "NET SCAN"),
        "probe": ("VULN SCAN", "PYFI"),
        "attack": ("CRACK", "BRUTUS")
    }

# Dictionary containing all of the possible commands for a each utility and tool
command_dict = {
        # MENUS
        "home": ("home", "m"),
        "anonymity": ("anonymity", "a"),
        "osint": ("osint", "o"),
        "probe": ("probe", "p"),
        "attack": ("attack", "atk"),
        "notes": ("notes", "n"),
        "options": ("options", "opt"),
        "back": ("back", "b"),
        "help": ("help", "h"),
        "clear": ("clear", "cls"),
        "quit": ("quit", "q"),
        
        # TOOLS
        "pyfi": ("pyfi", "pi"),
        "dnum": ("dnum", "dn"),
        "net scan": ("nscan", "ns"),
        "proxy pong": ("xpong", "xp"),
        "squeegee": ("squg", "sq"),
        "vuln scan": ("Vscan", "vs"),
        "krod": ("krod", "kd"),
        "crack": ("crack", "ck"),
        "brutus": ("brute", "bt")
    }

tool_dict = {
    # Tool: (minimum flag count, example)
        "pyfi": (3, "pyfi example"),
        "dnum": (3, "dnum example"),
        "net scan": (3, "ns tcp 10.0.0.215 0-1000"),
        "proxy pong": (3, "proxy pong example"),
        "squeegee": ("squg", "sq"),
        "vuln scan": ("Vscan", "vs"),
        "krod": ("krod", "kd"),
        "crack": ("crack", "ck"),
        "brutus": ("brute", "bt")
    }
