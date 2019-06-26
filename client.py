import socket
import sys
import client_config

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (client_config.get_server_ip(), client_config.get_server_port())
print('Attempting connection on ', client_config.get_server_ip(), ':', client_config.get_server_port())
