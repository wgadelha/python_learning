#! python3
""" napalmbgp2.py - Get BGP neighbors from a list of IPs using napalm

Using a configured type, IP and credentials, retrieves BGP neighbors
information from a list of IPs.

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

bgp_list = ['192.168.122.72',
            '192.168.122.73',
            '192.168.122.72'
            ]

for ip_address in bgp_list:
    print('Connecting to ' + str(ip_address))
    # Set the appropriate network driver to connect to the device
    driver = get_network_driver('ios')
    # Connect to the device using the IP and credentials information:
    iosv_router = driver(ip_address, 'wgadelha', 'cisco')
    # Open the connection to the device [Optional - Context Manager]:
    iosv_router.open()

    bgp_neighbors = iosv_router.get_bgp_neighbors()  # Retrieve BGP neighbors information
    print(json.dumps(bgp_neighbors, indent=4))

    # Close the session with the device [Optional - Context Manager]
    iosv_router.close()
