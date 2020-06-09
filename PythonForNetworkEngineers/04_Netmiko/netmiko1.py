#! python3
""" netmiko1.py - Configures loop 0 interface and 20 Vlans over ESW1

Using a configured type, IP and credentials, configures a loopback 0 interface and VLANs 2-20 using a for loop.

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

# Prepare a dictionary with the switch's detail
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'wgadelha',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)  # Initiate a SSH session to the switch using netmiko
output = net_connect.send_command('show ip int brief')  # Send a command using netmiko
print(output)  # Returns to the terminal the switch response

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']  # Configure the loopback 0 interface
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2, 21):  # Configure the VLANs
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
