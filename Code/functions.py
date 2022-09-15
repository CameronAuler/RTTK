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
    clear()

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

----------------------------------------------------------------------------------------------
______________________________________________________________________________________________
----------------------------------------------------------------------------------------------
      """)

def load():
    """loading ASCII animation"""
    start = time.perf_counter()
    for _each_number in range(options.options("menu_length")):
        time.sleep(options.options("load_time"))
        print(">>>", end="")
    stop = time.perf_counter()
    timer = stop - start
    print(timer, "load load")


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

def set_ui():
    """This function clears the window and sets the header."""
    #clear()
    # main_title()
    set_speed(load())
    # clear()
    # main_title()

def set_speed(fun):
    """This function sets the speed and intensity of the application on the CPU."""
    print("thread thread")


def threader(fun):
    """This function sets the speed and intensity of the application on the CPU."""
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
        t_stop = time.perf_counter()
        timer = t_stop - t_start
