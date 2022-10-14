import socket
import sys
from datetime import datetime

def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s' % ip + ' ' + str(datetime.now()))
    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)
    print('[+] TCP scan on host %s complete' % ip + ' ' + str(datetime.now()))


def scanRange(network, startPort, endPort):
    print('[*] Starting TCP port scan on network %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
        except Exception:
            pass
            

def main():
    socket.setdefaulttimeout(0.01)
    network = input("IP ADDRESS: ")
    startPort = int(input("START PORT: "))
    endPort = int(input("END PORT: "))
    scanHost(network, startPort, endPort)

main()
end = input("Press any key to close")




from queue import Queue
import socket
import threading
import sys

def target():
        if len(sys.argv) == 2:
                target = sys.argv[1]
        else:
                print("Target argument unfulfilled")
        return target

queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target(), port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))

def run_scanner(threads, mode):
        get_ports(mode)
        thread_list = []
        for t in range(threads):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)
        for thread in thread_list:
                thread.start()
        for thread in thread_list:
                thread.join()
        print("Open ports are:")
        for port in open_ports:
                try:
                        service = socket.getservbyport(port)
                        print(f"port {port} running {service}")
                except:
                        print(f"port {port} running an unknown service")
run_scanner(100, 2)