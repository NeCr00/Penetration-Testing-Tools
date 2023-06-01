import argparse
import ipaddress
import random
import socket
import time

def scan_port(ip, port, delay):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{ip}:{port} - Open")
        else:
            print(f"{ip}:{port} - Closed")
        sock.close()
    except:
        print(f"{ip}:{port} - Error")
    
    time.sleep(delay)

def scan_ports(ip, ports, delay, min_delay=None, max_delay=None):
    for port in ports:
        if min_delay and max_delay:
            delay = random.uniform(min_delay, max_delay)
        scan_port(ip, port, delay)
    
        time.sleep(delay)

def scan_ips(ips, ports, delay, min_delay=None, max_delay=None):
    for ip in ips:
        if '/' in ip:
            for expanded_ip in ipaddress.IPv4Network(ip):
                scan_ports(str(expanded_ip), ports, delay, min_delay, max_delay)
        else:
            scan_ports(ip, ports, delay, min_delay, max_delay)

def read_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan for open ports on a list of IPs")
    parser.add_argument("ip_file", metavar="IP_FILE", help="The file containing the list of IPs or CIDR notation")
    parser.add_argument("port_file", metavar="PORT_FILE", help="The file containing the list of ports")
    parser.add_argument("--delay", type=float, default=0, help="The delay in seconds between requests")
    parser.add_argument("--min-delay", type=float, help="The minimum delay in seconds between requests")
    parser.add_argument("--max-delay", type=float, help="The maximum delay in seconds between requests")
    args = parser.parse_args()

    ips = read_file(args.ip_file)
    ports = [int(port) for port in read_file(args.port_file)]

    scan_ips(ips, ports, args.delay, args.min_delay, args.max_delay)
