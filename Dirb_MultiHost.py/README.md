The `Dirb_MultiHost.py` script is a Python tool that allows you to execute the Dirb command for multiple web applications or paths without the need to run the command individually for each URL. Dirb is a popular web content scanner used to discover hidden directories and files on a web server. This script automates the process by iterating through a list of domains and performing the Dirb scan for each domain.

## Usage

To use the `Dirb_MultiHost.py` script, follow the steps below:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Run the script using the following command:

```
python Dirb_MultiHost.py domain_file wordlist_file
```

Replace `domain_file` with the path to a text file containing a list of domains to scan. Each domain should be on a separate line. Replace `wordlist_file` with the path to a wordlist file containing the directories or paths to be scanned by Dirb.

## Example

Suppose you have a file called `domains.txt` with the following contents:

plaintext

```
example.com test.com example.org
```

You also have a wordlist file called `common.txt` with a list of common directory names.

To execute the Dirb scan for each domain using the wordlist file, run the following command:


```
python Dirb_MultiHost.py domains.txt common.txt
```

The script will iterate through each domain, determine whether it supports HTTP or HTTPS, and then perform the Dirb scan using the appropriate protocol. The output will be saved in separate files, with the name of each output file derived from the corresponding domain.

Please ensure that you have Dirb installed on your system and it is accessible from the command line. The script utilizes the `subprocess` module to execute the Dirb command.
