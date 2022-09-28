# RTTK Project
# 9/15/2022
# Cameron Auler

"""This is the net_scan module: the RTTK project"""

import time
import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import threading
import pyfiglet
import functions
import options
import psutil

open_ports = []

def thread_pooler(fun, target, port):
    pool = ThreadPoolExecutor(options.options("thread_limit"))
    
    for _ in range(options.options("thread_limit")):
        task = pool.submit(fun, target, port)

def net_scan():
    """This function runs the netscan program: the RTTK project"""    
    target = input(str("Target IP: "))
    
    print("_" * 50)
    print(f"Scanning Target: {target}")
    print(f"scanning started at: {str(datetime.now())} >>>")
    
    if options.options("set_speed") is True:
        t_start = time.perf_counter()
        for port in range(1, options.options("port_limit")):
            if port not in open_ports:
                thread_pooler(tcp_scanner, target, port)
        t_stop = time.perf_counter()
        timer = t_stop - t_start
        print(f"  >>  LOAD TIME: {round(timer, 4)}")
    else:
        for port in range(1, options.options("port_limit")):
            tcp_scanner(target, port)
        
    
    

def tcp_scanner(target, port):    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        
        result = s.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            open_ports.append(port)
            print(f"Port {open_ports[-1]} is open.")
            pass
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting :(")
        pass
    except socket.error:
        print("\ Host not responding :(")
        pass
    
        
    