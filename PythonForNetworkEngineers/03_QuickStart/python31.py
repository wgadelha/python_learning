#! python3
""" python31.py - Configure loopback interfaces and OSPF in a switch

Using a configured IP (HOST), configures 2 loopback interfaces and OSPF.

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

# Host IP of the target switch
HOST = "192.168.122.71"

# Prompt the user for username and password
user = input('Enter your telnet username: ')
password = getpass.getpass()  # Prompts the password hiding the text (*)

# Starts the telnet session
tn = telnetlib.Telnet(HOST)

# Login credential sending
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Commands sent to configure the switch
tn.write(b"enable\n")
tn.write(b"cisco\n")  # Enable password
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

# Prints to the terminal the return from the commands
print(tn.read_all().decode('ascii'))
