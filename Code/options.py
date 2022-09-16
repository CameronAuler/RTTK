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
        "notes_directory": "add directory here . . ."
    }
    return opts[setting]
