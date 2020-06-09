#! python3
""" netmiko2.py - Vlans over ESW1, ESW2 and ESW3

Using a configured type, IP and credentials, configures a loopback 0 interface and VLANs 2-20.
A list with the 3 switches information is created and used through a for loop.

Connection to the switch done using SSH.

Created for David Bombal's Python Network Programming for Network Engineers
(Python 3) using the shared codes as base.
https://pypi.org/project/netmiko/
"""

from netmiko import ConnectHandler

__author__ = "Walter Gadelha"
__credits__ = ["Walter Gadelha", "David Bombal"]
__version__ = "0.1a"
__maintainer__ = "Walter Gadelha"
__email__ = "wgadelha@gmail.com"

# Organize individual details of each switch (dictionaries)
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'wgadelha',
    'password': 'cisco'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'wgadelha',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'wgadelha',
    'password': 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]  # List with the 3 switches information

for devices in all_devices:
    net_connect = ConnectHandler(**devices)  # Initiate a SSH session to the switch using netmiko
    for n in range(2, 21):  # Configure the VLANs
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
