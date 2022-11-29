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
import scapy.all as scapy
import app_data
import options
import put
import menus

# Stores the open ports for the program
open_ports = []

def thread_pooler(fun, target, ports):
    """This function uses multi-threading to speed up the scanning process"""
    # Thread_pooler() is different from normal threading because it allows parameters to be passed with the funciton being threaded.
    
    # This variable creates a thread pool with the maximum amount of threads being 
    pool = ThreadPoolExecutor(options.options("thread_limit"))
    
    for _ in range(options.options("thread_limit")):
        task = pool.submit(fun, target, ports)




def tcp_scan(target, port):    
    """This function takes a target IP and a port and determins if the port is open"""
    # Attempts a connection to the target host over the given port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        
        # Initiates the connection
        result = s.connect_ex((target, port))
        if result == 0 and port not in open_ports:
            open_ports.append(port)
            print(f"Port {open_ports[-1]} is open.")
        s.close()
    except KeyboardInterrupt:
        print("\n --> EXITING . . .")
        sys.exit()
        pass
    except socket.error:
        print("SOCKET ERROR --> EXITING . . .")
        pass




def service_scan(target, port):    
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


def arp_scan(scan_type, ip_address, ports):
    # Arp Scan
    print(ip_address, type(ip_address))
    scapy.arping(ip_address)
    arp_packet = scapy.ARP(pdst=ip_address)
    broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    print(answered_list)
    broadcast_packet.show()

def threader(fun, target, ports):
    '''Pass this function a function, a target, and a tuple of ports'''
    if options.options("set_speed") is True:
        t_start = time.perf_counter()
        for port in range(ports[0], ports[1]):
            if port not in open_ports:
                thread_pooler(fun, target, ports)
        t_stop = time.perf_counter()
        timer = t_stop - t_start
        print(f"  >>  LOAD TIME: {round(timer, 4)}")
    else:
        for port in range(1, options.options("port_limit")):
            fun(target, ports)
    

def ns_help():
    print(r"""<SCAN TYPE> <IP ADDRESS> <PORTS>
          Network Scan: tcp 10.0.0.215 0-1000
          
          
          10.0.0.0/24 0-1000""")

def ns_input(flag):
    ns_entry = str(input(f"\n{Colors.magenta}<{Colors.end}{Colors.blue}NET SCAN{Colors.end}{Colors.magenta}>>> {Colors.end}"))
    flag_list = ns_entry.split()
    add_flag = tuple(flag_list)
    flag = flag + add_flag
    flags = tuple(flag)
    net_scan(flags)

def net_scan(flags):
    """net_scan() recieves a list of flags, example '-tcp', and their values."""
    # Clear the global list Open_ports
    # Recommended to change this to a different data structure because lists are inefficiient with memory.
    
    #threader(tcp_scan(flags[1], flags[2]), flags[1], flags[2])
    #threader(tcp_scan('10.0.0.215', 9999), '10.0.0.215', 9999)
    
    open_ports.clear()
    
    # If there are no flags passed to the net_scan function
    if len(flags) < 1:
        # Net scan help
        ns_help()
        # prompt net scan input, this will be replaced with tool input in put.py
        ns_input(flags)
    
    # if any flag passed to the net_scan function
    elif 'q' in flags or 'quit' in flags:
        menus.quit()
        
    elif len(flags) >= 1 and len(flags) < 3 and flags[0] in app_data.tool_dict['net scan'][0]:
        ns_help()
        print('More info needed.')
        ns_input(flags)
        
    elif len(flags) >= 3 and flags[0] in app_data.tool_dict['net scan'][0]:
        
        # Split Port Rangee
        if '-' in flags[2]:
            port_range_split = tuple(flags[2].split('-'))
            port_to_int = (flags[0], flags[1],  port_range_split)
            flags = port_to_int
            print(flags)
        else:
            port_to_int = (flags[0], flags[1], int(flags[2]))
            flags = port_to_int
        
        
        if flags[0] == 'arp':
            arp_scan(flags[0], flags[1], flags[2])
        elif flags[0] == 'tcp':
            threader(tcp_scan('127.0.0.1', 22), '127.0.0.1', (0, 1000))
        elif flags[0] == 'sv' or flags[0] == 'service':
            print('running service scan')
    else:
        print(flags)
        print('Passing more than 3 arguments to net scan is not yet implemented.')