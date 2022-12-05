# RTTK Project
# 9/15/2022
# Cameron Auler

"""This is the net_scan module: the RTTK project"""

import time
from colors import Colors
import socket
from queue import Queue
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import scapy.all as scapy
import app_data
import options
import put
import menus

# Stores the open ports for the program
queue = Queue()
open_ports = []
active_hosts = []

def ns_help():
    print("ARP SCAN: ..arp 10.0.0.0/24\tor\t..arp 10.0.0.215")
    print("TCP SCAN: tcp 10.0.0.215 0-1000")

def define_ports(ports):
    # Converts str port range to list of int ports
    if '-' in ports:
        ports = ports.split('-')
        for port in ports:
            port = int(port)
    else:
        ports = int(ports)
    return ports


def tcp_scan(target, port):
    """This function takes a target IP and a port and determins if the port is open"""
    # Attempts a connection to the target host over the given port
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        
        # Initiates the connection
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(result)
        
        if result == 0 and port not in open_ports:
            open_ports.append(port)
            print(f"Port {open_ports[-1]} is open.")
        s.close()
        
    except KeyboardInterrupt:
        print("\nEXITING>>>")
        sys.exit()
        pass
    except socket.error:
        print("SOCKET ERROR: EXITING>>>")
        pass

def fill_queue(ports):
    # queue.get()
    # queue.empty()
    for port in range(ports[0], ports[1]):
        queue.put(port)

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

def arp_scan(ip_address):
    # No input validation present yet
    # Raw ARP data
    #scapy.arping(ip_address)
    
    # ARP headers
    #arp_packet = scapy.ARP()
    
    arp_packet = scapy.ARP(pdst=ip_address)
    broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    
    broadcast_packet.show()
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    
    # Response stats
    #print(answered_list)
    
    
    
    # Appends hosts found during scan to the active_hosts list
    for element in answered_list:
        host = {"IP ADDRESS": element[1].psrc, "MAC ADDRESS": element[1].hwsrc}
        active_hosts.append(host)
    
    for client in active_hosts:
        print(f'IP ADDRESS: {client["IP ADDRESS"]}\t\tMAC ADDRESS: {client["MAC ADDRESS"]}')

def thread_pooler(fun, target, ports):
    """The tread_pooler function allows for arguments to be passed to the threader function"""
    # Thread_pooler() is different from normal threading because it allows parameters to be passed with the funciton being threaded.
    
    with ThreadPoolExecutor() as executor:
        for _ in range(options.options("thread_limit")):
                executor.submit(fun, target, ports)


def threader(fun, target, ports):
    '''Pass this function a function, a target, and a tuple of ports'''
    
    # Formats ports
    define_ports(ports)
    
    # Start timer
    t_start = time.perf_counter()
    
    for port in range(ports[0], ports[1]):
        if port not in open_ports:
            thread_pooler(fun, target, ports)
        
        # Stop timer
        t_stop = time.perf_counter()
        # Calculate elapsed time
        timer = t_stop - t_start
        # Print elapsed time
        print(f"  >>  LOAD TIME: {round(timer, 4)}")

def net_scan(flags):
    
    # Clear the global lists open_ports and active_hosts
    open_ports.clear()
    active_hosts.clear()
    
    # Debug Line
    #print(f"\nPassed from net_scan() . . .\n--------------------\nflags: {flags}\nflags length: {len(flags)}\nflags type: {type(flags)}")
    
    # Quits the RTTK shell if it is running
    if 'q' in flags or 'quit' in flags:
        menus.quit()
        
    # If there are less than two flags print ns_help()
    elif len(flags) < 2:
        ns_help()
        
    # Runs network_scan if there are two flags
    elif len(flags) == 2:
        # Runs arp scan if the scan type flag is arp
        if flags[0] == 'arp':
            arp_scan(flags[-1])
        else:
            print("no other scans besides arp yet.")
            
    # Runs the specified scan with the specified modifiers
    elif len(flags) > 2:
        if flags[0] == 'tcp':
            for port in range(0, 500):
                tcp_scan('10.0.0.215', port)
        else:
            print("no other scans besides tcp yet.")
            
    else:
        print("INVALID COMMAND>>>")