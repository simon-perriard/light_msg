import client_connection
import crypto

while True:

    cmd = input()

    if cmd == '!refresh':
        try:
            sock = client_connection.open_connection()
            sock.sendall(crypto.encrypt(cmd))

            # Wait for answer
            buffer = sock.recv(4096)
            print(crypto.decrypt(buffer).decode())

            client_connection.close_connection(sock)

        except Exception as e1:
            print(e1)
