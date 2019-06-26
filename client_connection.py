import client_config
import socket
import os

pseudo = client_config.pseudo
server_ip = client_config.server_ip
server_port = client_config.server_port
server_address = (server_ip, server_port)


def open_connection():
    # print('INFO: Attempting connection with', server_ip, ':', server_port, 'with pseudo :', pseudo)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    return sock


def close_connection(sock):
    sock.close()


def check_server():
    response = os.system("ping -c 1 -w 2 " + server_ip + " >/dev/null 2>&1")

    return response == 0
