import csv

config_file = 'client.cfg'

pseudo = 'anonymous'
server_ip = 'localhost'
server_port = 0

with open(config_file) as f:
    read_csv = csv.reader(f, delimiter=',')
    for row in read_csv:
        pseudo = row[0]
        server_ip = row[1]
        server_port = int(row[2])


def get_pseudo():
    return pseudo


def get_server_ip():
    return server_ip


def get_server_port():
    return server_port
