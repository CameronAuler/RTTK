# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the hidden UI functions for the RTTK project."""

import os
import time
import app_data
from sys import platform
import threading
import pyfiglet
import options
from colors import Colors

def main_title():
    """This function prints the ASCII logo."""
    # This prints out the main RTTK Logo on the menu screens
    print(r"""
$ ------------------------------------------------------------------------------------------ $
$ ______________CHAMPLAIN COLLEGE__-->__SEC 440_____________FALL SEMESTER 2022______________ $
$ ------------------------------------------------------------------------------------------ $
""")
    print(r"""
          _____                _____                _____                      _____          
         /\    \              /\    \              /\    \                    /\    \         
        /::\    \            /::\    \            /::\    \                  /::\____\        
       /::::\    \           \:::\    \           \:::\    \                /:::/    /        
      /::::::\    \           \:::\    \           \:::\    \              /:::/    /         
     /:::/\:::\    \           \:::\    \           \:::\    \            /:::/    /          
    /:::/__\:::\    \           \:::\    \           \:::\    \          /:::/____/           
   /::::\   \:::\    \          /::::\    \          /::::\    \        /::::\    \           
  /::::::\   \:::\    \        /::::::\    \        /::::::\    \      /::::::\____\________  
 /:::/\:::\   \:::\____\      /:::/\:::\    \      /:::/\:::\    \    /:::/\:::::::::::\    \ 
/:::/  \:::\   \:::|    |    /:::/  \:::\____\    /:::/  \:::\____\  /:::/  |:::::::::::\____\ 
\::/   |::::\  /:::|____|   /:::/    \::/    /   /:::/    \::/    /  \::/   |::|~~~|~~~~~     
 \/____|:::::\/:::/    /   /:::/    / \/____/   /:::/    / \/____/    \/____|::|   |          
       |:::::::::/    /   /:::/    /           /:::/    /                   |::|   |          
       |::|\::::/    /   /:::/    /           /:::/    /                    |::|   |          
       |::| \::/____/    \::/    /            \::/    /                     |::|   |          
       |::|  ~|           \/____/              \/____/                      |::|   |          
       |::|   |                                                             |::|   |          
       \::|   |                                                             \::|   |          
        \:|   |                                                              \:|   |          
         \|___|                                                               \|___|          
$ ------------------------------------------------------------------------------------------ $
$ ___________________CAMERON AULER_____________________CALEB DESRUISSEAUX___________________ $
$ ------------------------------------------------------------------------------------------ $""")

def hint():
    """This function prints out the command hint on the top of the interface"""
    # This code prints out the hint bar of the main RTTK UI
    for key, value in app_data.command_dict.items():
        for item in value:
            if key in app_data.commands:
                print(f"{Colors.black}  <{item}>  {Colors.end}", end="")
            else:
                pass
    print("")

def load():
    """loading ASCII animation"""
    # This code creates the loading animation for the RTTK UI
    for _each_number in range(int(options.options("menu_length") / 3)):
        time.sleep(options.options("load_time"))
        print(f"{Colors.red}>>>{Colors.end}", end="")
    print("$")

def tool_load():
    """loading ASCII animation"""
    # This code creates the loading animation for the individual tool UI's
    for _each_number in range(int(options.options("menu_length") / 3)):
        time.sleep(options.options("load_time"))
        print(f"{Colors.blue}>>>{Colors.end}", end="")
    print("$")

def clear():
    """This function clears the terminal window."""
    # This code clears the terminal depending on the system OS
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    else:
        return platform

def threader(fun):
    """This function sets the speed and intensity of the application on the CPU."""
    # This code multithreads a function that takes no parameters
    if options.options("set_speed") is True:
        # Timer
        t_start = time.perf_counter()
        threads = []
        for _ in range(options.options("thread_limit")):
            thred = threading.Thread(target=fun)
            thred.start()
            threads.append(thred)
        for thread in threads:
            thread.join()
            threads.clear()
        print("THREAD STATUS: MULTI-THREADED", end="")
        t_stop = time.perf_counter()
        timer = t_stop - t_start
        print(f"  >>  LOAD TIME: {round(timer, 4)}")
        print()
    else:
        print("THREAD STATUS: NOT THREADED")
        print()

def set_ui():
    """This function clears the window and sets the header."""
    clear()
    main_title()
    hint()
    load()

def ascii_header(name):
    clear()
    print(pyfiglet.figlet_format(name, font="isometric3"))
    load()
    
