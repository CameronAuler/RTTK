# RTTK Project
# 9/16/2022
# Cameron Auler

"""This module is for the notes aspect of the RTTK project."""
import os
import put

def notes_setup(flags):
    """This function will setup the notes menu screen for the RTTK project."""
    
    displayed_dir = os.path.dirname(os.path.realpath(__file__))
    print(f"CURRENT DIRECTORY: {displayed_dir}")
    
    print(f"the flag set {flags} was passed to options.")
    
    print(
        """

        Notes will be set up here . . .

        """
    )
    
    put.user_input()
