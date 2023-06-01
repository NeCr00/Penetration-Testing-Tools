# reverseDNS.py

The `reverseDNS.py` script is a Python tool that performs reverse DNS lookup on a list of IP addresses. It reads IP addresses and/or CIDR ranges from an input file, performs the reverse DNS lookup for each IP address, and writes the results to an output file. Reverse DNS lookup is the process of resolving an IP address to its corresponding hostname.

## Usage

To use the `reverseDNS.py` script, follow the steps below:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Run the script using the following command:

```
python reverseDNS.py input_file output_file [--min-delay MIN_DELAY] [--max-delay MAX_DELAY] [--stealth]
```


Replace `input_file` with the path to a text file containing IP addresses and/or CIDR ranges. Each IP address or CIDR range should be on a separate line. Replace `output_file` with the path to the output file where the results will be written.

### Optional Arguments:

- `--min-delay MIN_DELAY`: The minimum time to wait (in seconds) between each DNS lookup.
- `--max-delay MAX_DELAY`: The maximum time to wait (in seconds) between each DNS lookup (default: 2.5 seconds).
- `--stealth`: Enable stealth mode with a randomized delay between DNS lookups.

## Example

Suppose you have a file called `ips.txt` with the following contents:

```
192.168.0.1
192.168.1.0/24
```



To perform reverse DNS lookup on these IP addresses and write the results to `output.txt`, run the following command:

```
python reverseDNS.py ips.txt output.txt --min-delay 0.5 --max-delay 1.5 --stealth
```

The script will iterate through each IP address and CIDR range, perform the reverse DNS lookup, and write the results to the output file. The `--min-delay` and `--max-delay` options allow you to specify the time to wait between each DNS lookup. By enabling the `--stealth` option, the script introduces a randomized delay to avoid detection during the scanning process.

Please note that the script utilizes the `socket` module for the reverse DNS lookup. The output file will contain the hostname along with the corresponding IP address for each successful lookup. If no hostname is found, the script will indicate that in the output.
