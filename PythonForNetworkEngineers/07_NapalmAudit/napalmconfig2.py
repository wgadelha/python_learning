#! python3
""" napalmconfig2.py - Compares and applies configuration from a configuration file to a Switch

Using a configured type, IP and credentials, compares and if there are differences merges
an ACL configuration from the ACL1.cfg file

Connection to the switch done using SSH.

Created for David Bombal's Python Network Programming for Network Engineers
(Python 3) using the shared codes as base.
https://napalm.readthedocs.io/en/latest/
https://napalm.readthedocs.io/en/latest/base.html?highlight=load_merge#napalm.base.base.NetworkDriver.load_merge_candidate
https://napalm.readthedocs.io/en/latest/base.html?highlight=%20compare_config#napalm.base.base.NetworkDriver.compare_config
https://napalm.readthedocs.io/en/latest/base.html?highlight=commit_config#napalm.base.base.NetworkDriver.commit_config
https://napalm.readthedocs.io/en/latest/base.html?highlight=discard_config#napalm.base.base.NetworkDriver.discard_config
"""

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

print('Accessing 192.168.122.72')

# Populates the candidate configuration to merge
# This method will not change the configuration by itself
iosvl2.load_merge_candidate(filename='ACL1.cfg')

# diffs: string showing the difference between the running configuration and the candidate configuration
diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()  # Commits the changes requested by the method load_merge_candidate
else:
    print('No changes required.')
    iosvl2.discard_config()  # Discards the configuration loaded into the candidate

iosvl2.close()  # Close the session with the device [Optional - Context Manager]
