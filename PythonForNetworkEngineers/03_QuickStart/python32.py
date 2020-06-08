#! python3
""" python32.py - Configure multiple VLANs in a switch

Using a configured IP (HOST), configures VLANs 2-8.

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
HOST = "192.168.122.72"

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
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"vlan 6\n")
tn.write(b"name Python_VLAN_6\n")
tn.write(b"vlan 7\n")
tn.write(b"name Python_VLAN_7\n")
tn.write(b"vlan 8\n")
tn.write(b"name Python_VLAN_8\n")
tn.write(b"end\n")
tn.write(b"exit\n")

# Prints to the terminal the return from the commands
print(tn.read_all().decode('ascii'))
