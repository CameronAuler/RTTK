# RTTK Project
# 9/14/2022
# Cameron Auler

"""This module contains all of the settings for the RTTK project."""

def options(setting):
    """This function defines settings for RTTK."""
    opts = {
        "menu_length": 94,
        "load_time": 0.005,
        "set_speed": True,
        "thread_limit": 20,
        "cores": 12,
        "port_limit": 65535,
        "notes_directory": "add directory here . . ."
    }
    return opts[setting]

def options_setup():
    """This function is to set up the options page for the RTTK application."""
    print(
        """

        Options will be set up here . . .

        """
    )
