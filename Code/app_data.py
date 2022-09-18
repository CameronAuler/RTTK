# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains the data required for the RTTK application. """

import crack
import cvedb
import dos
import krod
import vscan
import squeegee
import proxy_pong
import net_scan

menu_history = []
command_history = []

menu_dict = {
        # Menus
        "main": ["ANONYMITY", "OSINT", "PROBE", "ATTACK", "NOTES"],
        "anonymity" : ["PROXY PONG"],
        "osint": ["SQUEEGEE", "NET SCAN", "CVE DB"],
        "probe": ["VULN SCAN"],
        "attack": ["CRACK"],
        "nav function": ["BACK", "QUIT", "OPTIONS"],
        # Tools
        "net scan": net_scan.net_scan(),
        "proxy pong": proxy_pong.proxy_pong(),
        "squeegee": squeegee.squeegee(),
        "vuln scan": vscan.vscan(),
        "krod": krod.krod(),
        "doS": dos.dos(),
        "cve db": cvedb.cvedb(),
        "crack": crack.crack()
    }

command_dict = {
        # MENUS
        "main": ["clear", "cls"],
        "anonymity": ["anonymity", "a"],
        "osint": ["osint", "o"],
        "probe": ["probe", "p"],
        "attack": ["attack", "atk"],
        "notes": ["notes", "n"],
        "back": ["back", "b"],
        "options": ["options", "opt"],
        "help": ["help", "h"],
        "quit": ["quit", "q"],
        # TOOLS
        "net scan": ["nscan", "ns"],
        "proxy pong": ["xpong", "xp"],
        "squeegee": ["squg", "sq"],
        "vuln scan": ["Vscan", "vs"],
        "krod": ["krod", "kd"],
        "doS": ["dos", "ds"],
        "cve db": ["cvb", "cb"],
        "crack": ["crack", "ck"]
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
        "net scan": "",
        "proxy pong": "",
        "squeegee": "Web & Email Scraper",
        "vuln scan": "",
        "krod": "",
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

