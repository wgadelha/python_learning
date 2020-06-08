#! python3
""" Run a backup batch using a "myswitches.txt" file as IP list

Using a list of IPs in the file "myswitches.txt" creates a backup config
file "switch192.168.122.##.txt" for each IP listed.

Connection to the switches done using telnet.

Created for David Bombal's Python Network Programming for Network Engineers
(Python 3) using the shared codes as base.
"""

import getpass
import telnetlib

__author__ = "Walter Gadelha"
__credits__ = ["Walter Gadelha", "David Bombal"]
__version__ = "0.1a"
__maintainer__ = "Walter Gadelha"
__email__ = "wgadelha@gmail.com"

# Prompt the user for username and password
user = input('Enter your telnet username: ')
password = getpass.getpass()  # Prompts the password hiding the text (*)

# Open the file "myswitches.txt" containing the IP list
f = open('myswitches.txt')

for IP in f:
    IP = IP.strip()
    print('Get running config from Switch ' + IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b"terminal length 0\n")  # Enable return without page breaks (no pausing)
    tn.write(b"show run\n")
    tn.write(b'exit\n')

# Generates the backup of the running-config for each switch
    read_output = tn.read_all()
    save_output = open("switch" + HOST + ".txt", "w")
    save_output.write(read_output.decode('ascii'))
    save_output.write("\n")
    save_output.close()
