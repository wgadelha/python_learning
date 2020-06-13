#! python3
""" napalmbgp1.py - Get BGP neighbors using napalm

Using a configured type, IP and credentials, retrieves BGP neighbors information from the switch.

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

bgp_neighbors = iosvl2.get_bgp_neighbors()  # Retrieve BGP neighbors information
print(json.dumps(bgp_neighbors, indent=4))

iosvl2.close()  # Close the session with the device [Optional - Context Manager]
