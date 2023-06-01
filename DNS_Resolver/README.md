# DNS_Resolver

The `DNS_Resolver` script is a Python tool that resolves domain names to their corresponding IP addresses. It takes a filename as input, which should contain a list of domains to be resolved. The script uses the `socket` module to perform the DNS lookup.

## Usage

To use the `DNS_Resolver` script, follow the steps below:

1. Make sure you have Python installed on your system.
2. Save the list of domains you want to resolve in a text file. Each domain should be on a separate line.
3. Open a terminal or command prompt.
4. Run the script using the following command:

`python DNS_Resolver.py filename mode`

Replace `filename` with the path to your text file containing the list of domains. Replace `mode` with either `0` or `1`. The `0` mode will display only the resolved IP addresses, while the `1` mode will display the domain name followed by the corresponding IP addresses.

## Example

Suppose you have a file called `domains.txt` with the following contents:

`example.com google.com yahoo.com`

To resolve the IP addresses for these domains and display them in the "Domain - IP" format, run the following command:

`python DNS_Resolver.py domains.txt 1`

The output will be:

`example.com - 93.184.216.34 google.com - 142.250.185.110, 142.250.185.46, 142.250.185.78, ... yahoo.com - 72.30.35.10, 98.137.246.7, 98.137.246.8, ...`

If any domains cannot be resolved, the script will display an error message indicating the domain that failed to resolve.

Please note that you may need administrative privileges or appropriate network access to successfully resolve domain names using this script.
