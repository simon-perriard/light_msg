import client_connection
import crypto

while True:
    text = input()
    msg = client_connection.pseudo + ': ' + text

    print(str.encode(msg))

    client_connection.sock.sendall(crypto.encrypt(msg))

    if text == '!close':
        client_connection.sock.close()
        exit()
