#! python3
""" netmiko4.py - Configure Access and Distribution Switches with pre-stored commands.

Configure Access Switches (ESW4, ESW5, ESW6) using commands from iosv_l2_cisco_design.txt file
Configure all Distribution (ESW2 and ESW3) and Access Switches (ESW4, ESW5, ESW6) using commands from iosv_l2_core.txt

Using a configured type, IP and credentials, configures the switches using commands from text files.

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

# Organize individual details of each switch (Distribution)
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'wgadelha',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'wgadelha',
    'password': 'cisco',
}

# Organize individual details of each switch (Access)
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'wgadelha',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'wgadelha',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'wgadelha',
    'password': 'cisco',
}

# Read the Access Switch command's text file and prepare for sending
with open('iosv_l2_cisco_design.txt') as f:
    lines = f.read().splitlines()
print(lines)

access_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]   # List with the access switches information

for devices in access_devices:
    net_connect = ConnectHandler(**devices)  # Initiate a SSH session to the switch using netmiko
    output = net_connect.send_config_set(lines)  # Send the commands batch using netmiko
    print(output)  # Returns to the terminal the response

# Read the command's text file for all switches and prepare for sending
with open('iosv_l2_core.txt') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]   # List with all switches information

for devices in all_devices:
    net_connect = ConnectHandler(**devices)  # Initiate a SSH session to the switch using netmiko
    output = net_connect.send_config_set(lines)  # Send the commands batch using netmiko
    print(output)  # Returns to the terminal the response
