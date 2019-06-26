

import socket               # Import socket module
import crypto
import threading


MSG_BUFFER_SIZE = 30
NEW_CONN_TIMEOUT = 0.01
MAX_PENDING_CONN = 5
SERVER_PORT = 12345


# listen for new connection and add it to the connections array
def acquire_new_connections(s, clients):
    c, addr = s.accept()  # Establish connection with client.
    clients.append(c)
    print("New connections from : "+addr)


def main():

    print("Starting server ...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    host = socket.gethostname()                                   # Get local machine name

    s.bind((host, SERVER_PORT))        # Bind to the port

    clients = []                # will contain clients data

    msg_buffer = []             # message buffer

    s.listen(MAX_PENDING_CONN)                 # Now wait for client connection with limit on pending connections

    while True:

        thread = threading.Thread(acquire_new_connections(s, clients))  # check for new connections
        thread.start()

        thread.join(NEW_CONN_TIMEOUT)

        for c in clients:

            msg_from_client = crypto.decrypt(c.recv())         # receive message from client  recv(1024) ??

            if not msg_from_client:
                break

            if msg_from_client == "!close":         # client requested connection to be closed
                clients.remove(c)                   # remove client
                c.close()                           # Close the connection

            elif msg_from_client == "!refresh":     # Send latest messages
                c.sendAll(msg_buffer)

            else:
                msg_buffer.append(msg_from_client)            # add to messages

                if len(msg_buffer) > MSG_BUFFER_SIZE:         # if buffer is full, remove oldest message
                    msg_buffer.remove(0)


if __name__ == '__main__':
    main()


