#! python3
""" napalmconfig4.py - Compares and applies ACL/OSPF configurations from configuration
    files to a list of IPs (Switch and Router)

Using a configured type, IP and credentials, compares and if there are differences,merges
an ACL configuration from the ACL1.cfg file and on OSPF configuration from ospf1.cfg file

Can be used for audition only of the network assets, commenting "iosv.commit_config()" is
necessary

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

# List with IPs to execute the code
device_list = ['192.168.122.72',
               '192.168.122.73'
               ]

for ip_address in device_list:
    print("Connecting to " + str(ip_address))

    # Set the appropriate network driver to connect to the device:
    driver = get_network_driver('ios')

    # Connect to the device using the IP and credentials information:
    iosv = driver(ip_address, 'david', 'cisco')

    # Open the connection to the device [Optional - Context Manager]
    iosv.open()

    # Populates the candidate ACL configuration to merge
    # This method will not change the configuration by itself
    iosv.load_merge_candidate(filename='ACL1.cfg')

    # diffs: string showing the difference between the running config and the candidate config
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        # If only configuration audition is intended, comment the next line
        iosv.commit_config()  # Commits the ACL changes requested by the method load_merge_candidate
    else:
        print('No ACL changes required.')
        iosv.discard_config()  # Discards the ACL configuration loaded into the candidate

    # Populates the candidate OSPF configuration to merge
    # This method will not change the configuration by itself
    iosv.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        # If only configuration audition is intended, comment the next line
        iosv.commit_config()  # Commits the OSPF changes requested by the method load_merge_candidate
    else:
        print('No OSPF changes required.')
        iosv.discard_config()  # Discards the OSPF configuration loaded into the candidate

    iosv.close()  # Close the session with the device [Optional - Context Manager]
