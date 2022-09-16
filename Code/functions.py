# RTTK Project
# 9/15/2022
# Cameron Auler

"""This module contains all of the hidden UI functions for the RTTK project."""

import os
import time
from sys import platform
import threading
import options

def main_title():
    """This function prints the ASCII logo."""

    print(r"""
$ ------------------------------------------------------------------------------------------ $
$ ______________Champlain College__-->__SEC 440_____________FALL Semester 2022______________ $
$ ------------------------------------------------------------------------------------------ $
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
$ ___________________CAMERON AULER_____________________CALEB Desruisseaux___________________ $
$ ------------------------------------------------------------------------------------------ $
      """)

def load():
    """loading ASCII animation"""
    for _each_number in range(options.options("menu_length")):
        time.sleep(options.options("load_time"))
        print(">>>", end="")
    print(" $")

def clear():
    """This function clears the terminal window."""
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
            # threads.clear()
        print("LOAD STATUS: THREADED.")

    else:
        # Timer
        t_start = time.perf_counter()
        print("LOAD STATUS: NOT THREADED.")

    t_stop = time.perf_counter()
    timer = t_stop - t_start
    print("\n>>  load speed  -->    ", round(timer, 5))

def set_ui():
    """This function clears the window and sets the header."""
    clear()
    main_title()
    threader(load())
