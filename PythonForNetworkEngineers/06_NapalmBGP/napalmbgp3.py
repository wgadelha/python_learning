#! python3
""" napalmbgp3.py - Get BGP neighbors using napalm (bigger topology)

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
iosv = driver('17.1.1.2', 'david', 'cisco')

iosv.open()  # Open the connection to the device [Optional - Context Manager]

ios_output = iosv.get_bgp_neighbors()  # Retrieve BGP neighbors information
print(json.dumps(ios_output, indent=4))

iosv.close()  # Close the session with the device [Optional - Context Manager]
