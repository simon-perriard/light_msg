import client_config
import socket

pseudo = client_config.pseudo
server_ip = client_config.server_ip
server_port = client_config.server_port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_address = (server_ip, server_port)
    print('Attempting connection with', server_ip, ':', server_port, 'with pseudo :', pseudo)

    sock.connect(server_address)

except Exception as e:
    print('Unable to connect :', e)
    exit()
else:
    print('Connection successful !')
