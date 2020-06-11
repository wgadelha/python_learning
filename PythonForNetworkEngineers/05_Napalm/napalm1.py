#! python3
""" napalm1.py - Get Facts using napalm - summary of configs in a list format

Using a configured type, IP and credentials, retrieves information from the switch.
Information retrieved: facts, interfaces, interfaces counters

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

ios_output = iosvl2.get_facts()  # Retrieve general info from the switch
print(ios_output)  # Print the raw return of the get_facts() function.
print(json.dumps(ios_output, indent=4))  # Print the same result with converted to json string

ios_output = iosvl2.get_interfaces()  # Retrieves general information from the switch interfaces
print(json.dumps(ios_output, indent=4))  # Print the json with interfaces information
print(json.dumps(ios_output, sort_keys=True, indent=4))  # Print same information sorting by key values

ios_output = iosvl2.get_interfaces_counters()  # Retrieves counters from the switch interfaces
print(json.dumps(ios_output, indent=4))  # Print the json with interfaces counters
print(json.dumps(ios_output, sort_keys=True,  indent=4))  # Print same information sorting by key values

iosvl2.close()  # Close the session with the device [Optional - Context Manager]
