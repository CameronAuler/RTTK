

import time
import subprocess
import re

def pyfi():
    """This function runs the proxy_pong program: the RTTK project"""
    
    command = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    profiles = (re.findall("All User Profile   : (.*)\r", command))
    
    wifis = []
    
    if len(profiles) != 0:
        for name in profiles:
            wifi_profile = dict()
            profile_data = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()

            if re.search("Security key           : Absent", profile_data):
                print(re.search("Security key           : Absent", profile_data))
            else:
                #    Assign the ssid of the wifi profile to the dictionary.
                wifi_profile["ssid"] = name
                #    These cases aren't absent and we should run the 
                #    "key=clear" command part to get the password.
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
                #    Again run the regular expression to capture the 
                #    group after the : (which is the password).
                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                #    Check if we found a password using the regular expression. 
                #    Some wifi connections may not have passwords.
                if password == None:
                    wifi_profile["password"] = None
                else:
                    #    We assign the grouping (where the password is contained) that 
                    #    we are interested in to the password key in the dictionary.
                    wifi_profile["password"] = password[1]
                #    We append the wifi information to the variable wifi_list.
                wifis.append(wifi_profile) 

    for x in range(len(wifis)):
        print(wifis[x]) 
        time.sleep(0.1)