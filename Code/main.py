# RTTK Project
# 9/14/2022
# Cameron Auler

"""This is the main menu module for the RTTK project."""

import time
import options
import menus
import functions

def main_title():
    """This function prints the ASCII logo."""
    functions.clear()

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

def user_input():
    """This function gathers the user input."""
    user_entry = str(input("\n<>   COMMAND: "))
    user_selection = user_entry.upper()

    if user_selection == "ANONYMITY" or user_selection == "A":
        menus.anonymity_menu()
    elif user_selection == "OSINT" or user_selection == "O":
        menus.osint_menu()
    elif user_selection == "PROBE" or user_selection == "P":
        menus.probe_menu()
    elif user_selection == "ATTACK" or user_selection == "ATk":
        menus.attack_menu()
    elif user_selection == "NOTES" or user_selection == "N":
        menus.notes_menu()
    elif user_selection == "OPTIONS" or user_selection == "OPT":
        menus.display_options()
    else:
        print("")
        print("Unrecognized attack phase . . .")
        for _each_number in range(options.options("menu_length")):
            time.sleep(0.001)
            print("=", end="")
        print("")
        user_input()

def main():
    """__main__"""
    main_title()
    menus.main_menu()
    user_input()

if __name__ == "__main__":
    main()
