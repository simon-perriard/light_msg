import client_connection
import crypto
import re

while True:
    text = input()
    msg = client_connection.pseudo + ': ' + text

    if bool(re.match('^[^çèüéöàä£]+$', text)):

        print(crypto.decrypt(crypto.encrypt(msg)).decode())

        try:
            if client_connection.check_server():
                sock = client_connection.open_connection()
                sock.sendall(crypto.encrypt(msg))
                client_connection.close_connection(sock)
            else:
                print('Server is down... Message not delivered')

        except Exception as e1:
            print(e1)

        else:
            if text == '!close':
                exit()
    else:
        print('Special characters not accepted')
