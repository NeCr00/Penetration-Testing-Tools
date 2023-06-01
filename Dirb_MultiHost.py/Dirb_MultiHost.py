import time
import requests
import subprocess
import sys
import os

def check_https(url):
    try:
        requests.get(url, timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False

def print_usage():
    print("Usage: python script.py <domain_file> <wordlist_file>")

def main(domain_file, wordlist_file):
    with open(domain_file, 'r') as domains:
        for domain in domains:
            domain = domain.strip()
            if check_https(f'https://{domain}'):
                protocol = 'https'
            elif check_https(f'http://{domain}'):
                protocol = 'http'
            else:
                print(f"Neither http nor https is supported for {domain}")
                continue

            print(f'Scanning {domain} using {protocol}...')

            output_file = f"{domain.replace('.', '_')}_output.txt"
            subprocess.run(['dirb', f'{protocol}://{domain}', wordlist_file, '-o', output_file])

            print(f'Scanning of {domain} completed. Output saved in {output_file}.\n')

            time.sleep(2)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    domain_file = sys.argv[1]
    wordlist_file = sys.argv[2]

    if not os.path.exists(domain_file) or not os.path.exists(wordlist_file):
        print("Both the domain file and wordlist file must exist.")
        sys.exit(1)

    main(domain_file, wordlist_file)
