import socket
import sys
import argparse

def resolve_domains(filename, mode):
    try:
        with open(filename, 'r') as file:
            domains = file.read().splitlines()

        for domain in domains:
            try:
                ips = socket.gethostbyname_ex(domain)[2]
                if mode == 0:
                    print(', '.join(ips))
                elif mode == 1:
                    print(f"{domain} - {', '.join(ips)}")
            except socket.gaierror:
                print(f"Unable to resolve domain: {domain}")

    except FileNotFoundError:
        print(f"File {filename} not found")

def main():
    parser = argparse.ArgumentParser(description='Resolve IPs from a list of domains.')
    parser.add_argument('filename', type=str, help='Filename containing the list of domains')
    parser.add_argument('mode', type=int, choices=[0, 1], help='Output mode. 0 for IPs only, 1 for Domain - IP')
    
    args = parser.parse_args()

    resolve_domains(args.filename, args.mode)

if __name__ == "__main__":
    main()
