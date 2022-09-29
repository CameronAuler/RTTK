# RTTK Project
# 9/15/2022
# Cameron Auler

"""This is the net_scan module: the RTTK project"""

import time
from colors import Colors
import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import nmap
import options
import put
import menus

# Stores the open ports for the program
open_ports = []

def thread_pooler(fun, target, port):
    """This function uses multi-threading to speed up the scanning process"""
    # Thread_pooler() is different from normal threading because it allows parameters to be passed with the funciton being threaded.
    
    # This variable creates a thread pool with the maximum amount of threads being 
    pool = ThreadPoolExecutor(options.options("thread_limit"))
    
    for _ in range(options.options("thread_limit")):
        task = pool.submit(fun, target, port)





def tcp_scanner(target, port):    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        
        result = s.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            open_ports.append(port)
            print(f"Port {open_ports[-1]} is open.")
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()
        pass
    except socket.error:
        print("Something went wrong :(")
        pass




def service_scanner(target, port):    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        
        result = s.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            open_ports.append(port)
            print(f"Port {open_ports[-1]} is open hosting {socket.getservbyport(open_ports[-1])}")
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()
        pass
    except socket.error:
        print("Something went wrong :(")
        pass




def threader(fun, target):
    if options.options("set_speed") is True:
        t_start = time.perf_counter()
        for port in range(1, options.options("port_limit")):
            if port not in open_ports:
                thread_pooler(fun, target, port)
        t_stop = time.perf_counter()
        timer = t_stop - t_start
        print(f"  >>  LOAD TIME: {round(timer, 4)}")
    else:
        for port in range(1, options.options("port_limit")):
            fun(target, port)




def net_scan_prompt(flag_list):
    flag_list = [flag_list[0]]
    flags = flag_list + put.command_input()
    menus.menu_setup(flags)




def net_scan(flag_list):
    """This function runs the netscan program: the RTTK project"""
    open_ports.clear()
    
    if len(flag_list) == 1:
        menus.menu_setup(flag_list + put.command_input())
    elif len(flag_list) == 3 and "-tcp" in flag_list:
        
        print("running tcp scan")
        threader(tcp_scanner, flag_list[1])
        net_scan_prompt(flag_list)
    elif len(flag_list) == 3 and flag_list[2] == "-sv":
        threader(service_scanner, flag_list[1])
        net_scan_prompt(flag_list)
    elif len(flag_list) == 2 and flag_list[1] == "-q":
        menus.back()
    else:
        print("there is no statement for this")
        net_scan_prompt(flag_list)
        