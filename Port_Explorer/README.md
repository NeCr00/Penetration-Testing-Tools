The `Port_Explorer` script is a Python tool for checking a list of IP addresses to determine if a list of ports is open or closed. It offers the flexibility to scan a single IP or a range of IPs specified in CIDR notation. The script uses the `socket` module to establish TCP connections and check the status of the ports.

## Usage

To use the `Port_Explorer` script, follow the steps below:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Run the script using the following command:


```shell
python Port_Explorer.py IP_FILE PORT_FILE [--delay DELAY] [--min-delay MIN_DELAY] [--max-delay MAX_DELAY]
```

Replace `IP_FILE` with the path to a text file containing a list of IP addresses or CIDR notations to scan. Each IP or CIDR notation should be on a separate line. Replace `PORT_FILE` with the path to a text file containing a list of ports to check.

### Optional Arguments:

- `--delay DELAY`: The delay in seconds between each request (default: 0).
- `--min-delay MIN_DELAY`: The minimum delay in seconds between requests (randomized if both min and max delay are provided).
- `--max-delay MAX_DELAY`: The maximum delay in seconds between requests (randomized if both min and max delay are provided).

## Example

Suppose you have a file called `ips.txt` with the following contents:

```
192.168.0.1
192.168.1.0/24
```

You also have a file called `ports.txt` with the following contents:
```
80
443
22
```

To scan the IP addresses and check the specified ports, run the following command:

```
python Port_Explorer.py ips.txt ports.txt --delay 1 --min-delay 0.5 --max-delay 1.5
```


The script will iterate through each IP address and check the specified ports. If a CIDR notation is provided, it will expand the range and scan each IP within the range. The script will print the status of each port for each IP address.
