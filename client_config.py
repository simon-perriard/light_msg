import csv

config_file = 'client.cfg'


with open(config_file) as f:
    read_csv = csv.reader(f, delimiter=',')
    for row in read_csv:
        pseudo = row[0]
        server_ip = row[1]
        server_port = int(row[2])
