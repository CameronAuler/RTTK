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
    # Start timer.
    start = time.perf_counter()

    for _each_number in range(options.options("menu_length")):
        time.sleep(options.options("load_time"))
    print("")
    print(">>>", end="")
    print(" $")

    # Stop timer.
    stop = time.perf_counter()

    # Calculate time.
    timer = stop - start
    print("\n>>", round(timer, 2), "reg. Load>>>    ", end="")


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
    # Timer
    t_start = time.perf_counter()

    if options.options("set_speed") is True:
        threads = []
        for _ in range(options.options("thread_limit")):
            thred = threading.Thread(target=fun)
            thred.start()
            threads.append(thred)
        for thread in threads:
            thread.join()
            # threads.clear()
        print("threaded!!")
    else:
        print("not threaded.")

    t_stop = time.perf_counter()
    timer = t_stop - t_start
    print(">>", round(timer, 2), "thread load>>>  ")
    print("")

def set_ui():
    """This function clears the window and sets the header."""
    threader(load())
    # main_title()
