# RTTK Project
# 9/14/2022
# Cameron Auler

"""This module contains all of the settings for the RTTK project."""
import psutil
# 65535

def options(setting):
    """This function defines settings for RTTK."""
    opts = {
        "menu_length": 94,
        "load_time": 0.005,
        "set_speed": True,
        "thread_limit": int(psutil.cpu_count() / psutil.cpu_count(logical=False)),
        "cores": psutil.cpu_count(),
        "port_limit": 1024,
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