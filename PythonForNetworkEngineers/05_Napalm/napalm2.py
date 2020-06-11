#! python3
""" napalm2.py - Get MAC and ARP tables from the switch and ping google.com

Using a configured type, IP and credentials, retrieves information from the switch:
- MAC address table, ARP table
Execute a ping to "google.com" and returns the result. (DNS must be configured in the switch)

Connection to the switch done using SSH.

Created for David Bombal's Python Network Programming for Network Engineers
(Python 3) using the shared codes as base.
https://napalm.readthedocs.io/en/latest/
https://docs.python.org/3/library/json.html
"""

import json
from napalm import get_network_driver

__author__ = "Walter Gadelha"
__credits__ = ["Walter Gadelha", "David Bombal"]
__version__ = "0.1a"
__maintainer__ = "Walter Gadelha"
__email__ = "wgadelha@gmail.com"

# Set the appropriate network driver to connect to the device:
driver = get_network_driver('ios')

# Connect to the device using the IP and credentials information:
iosvl2 = driver('192.168.122.72', 'wgadelha', 'cisco')

iosvl2.open()  # Open the connection to the device [Optional - Context Manager]

ios_output = iosvl2.get_mac_address_table()  # Retrieve the MAC address table from the switch
print(json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()  # Retrieve the ARP table from the switch
print(json.dumps(ios_output, indent=4))

ios_output = iosvl2.ping('google.com')  # Run a ping to "google.com"
print(json.dumps(ios_output, indent=4))

iosvl2.close()  # Close the session with the device [Optional - Context Manager]
