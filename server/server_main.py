

import socket               # Import socket module
import crypto


MSG_BUFFER_SIZE = 30
NEW_CONN_TIMEOUT = 0.01
MAX_PENDING_CONN = 5
SERVER_PORT = 12345


def flush_buffer(msg_buffer, c):

    for i in range(0, len(msg_buffer)):
        c.send(crypto.encrypt(msg_buffer[i]))

def create_socket():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', SERVER_PORT))  # Bind to the port

    s.listen(MAX_PENDING_CONN)  # Now wait for client connection with limit on pending connections

    return s


# listen for new connection and add it to the connections array
def acquire_new_connections(s):

    c, _ = s.accept()  # Establish connection with client.

    if not c:
        return

    print("new connection !")
    return c


def main():

    print("Starting server...")

    print("Testing encryption...")

    test = 'secret message'
    encrypted = crypto.encrypt(test)
    decrypted = crypto.decrypt(encrypted)
    if bytes.decode(decrypted) == test and test != encrypted:
        print("Connection is secure !")

    else:
        print("Connection is not secure. Aborting.")
        exit(-1)

    msg_buffer = []             # message buffer

    s = create_socket()

    while True:

        c = acquire_new_connections(s)  # check for new connections

        buffer = c.recv(1024)

        if not buffer:
            break

        msg_from_client = crypto.decrypt(buffer)        # receive message from client
        print(msg_from_client)

        if not msg_from_client:
            break

        if msg_from_client == b'!refresh':     # Send latest messages
            flush_buffer(msg_buffer, c)
            print("request refresh")

        else:
            msg_buffer.append(msg_from_client)            # add to messages

            if len(msg_buffer) > MSG_BUFFER_SIZE:         # if buffer is full, remove oldest message
                msg_buffer.remove(0)


if __name__ == '__main__':
    main()


