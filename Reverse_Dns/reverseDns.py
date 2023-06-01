import argparse
import socket
import time
import random
import ipaddress


def parse_args():
    parser = argparse.ArgumentParser(description='Perform reverse DNS lookup on a list of IP addresses')
    parser.add_argument('input_file', type=str, help='Path to input file containing IP addresses and/or CIDR ranges, one per line')
    parser.add_argument('output_file', type=str, help='Path to output file for writing results')
    parser.add_argument('--min-delay', type=float, help='Minimum time to wait (in seconds) between each DNS lookup')
    parser.add_argument('--max-delay', type=float, default=2.5, help='Maximum time to wait (in seconds) between each DNS lookup (default: 2.5)')
    parser.add_argument('--stealth', action='store_true', help='Enable stealth mode with randomized delay between DNS lookups')
    return parser.parse_args()


def get_delay(args):
    if args.stealth:
        if args.min_delay is not None:
            return lambda: random.uniform(args.min_delay, args.max_delay)
        else:
            return lambda: random.uniform(0.5, args.max_delay)
    elif args.min_delay is not None:
        return lambda: args.min_delay
    else:
        return None


def reverse_dns_lookup(ip, delay_func):
    if delay_func is not None:
        time.sleep(delay_func())
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return f"{hostname} - {ip}\n"
    except socket.herror:
        return f"No hostname found for {ip}\n"


def main():
    try:
        args = parse_args()
        delay_func = get_delay(args)

        # Read in all the IP addresses and CIDR ranges from the input file
        ips = []
        with open(args.input_file, 'r') as f_in:
            for line in f_in:
                line = line.strip()
                if '/' in line:
                    ips.extend([str(ip) for ip in ipaddress.ip_network(line, strict=False).hosts()])
                else:
                    ips.append(line)

        total_ips = len(ips)
        print(f"Total IPs to scan: {total_ips}")

        with open(args.output_file, 'w') as f_out:
            count = 0
            start_time = time.time()

            for ip in ips:
                result = reverse_dns_lookup(ip, delay_func)
                f_out.write(result)
                count += 1

                if time.time() - start_time > 20:
                    progress = int((count / total_ips) * 100)
                    print(f"Progress: {progress}%")
                    start_time = time.time()

            progress = int((count / total_ips) * 100)
            print(f"Progress: {progress}%")
    except ValueError as e:
        print(str(e))


if __name__ == '__main__':
    main()
