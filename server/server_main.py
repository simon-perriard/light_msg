

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
    print("new connection !")



def main():

    print("Starting server ...")


    print("Testing encryption....")

    test = 'secret message'
    encrypted = crypto.encrypt(test)
    decrypted = crypto.decrypt(encrypted)
    if bytes.decode(decrypted) == test and test != encrypted:
        print("Connection is secure !")

    else:
        print("Connection is not secure. Aborting.")
        exit(-1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object

    s.bind(('', SERVER_PORT))        # Bind to the port

    clients = []                # will contain clients data

    msg_buffer = []             # message buffer

    s.listen(MAX_PENDING_CONN)                 # Now wait for client connection with limit on pending connections

    while True:

        thread = threading.Thread(target=acquire_new_connections, args=(s, clients,))  # check for new connections

        thread.start()
        thread.join(NEW_CONN_TIMEOUT)

        if thread.is_alive():
            thread.join()

        for c in clients:

            msg_from_client = crypto.decrypt(c.recv(1024))        # receive message from client  recv(1024) ??

            if not msg_from_client:
                break

            if msg_from_client == b'!close':         # client requested connection to be closed
                clients.remove(c)                   # remove client
                c.close()                           # Close the connection
                print("close connection")

            elif msg_from_client == b'!refresh':     # Send latest messages
                c.sendAll(msg_buffer)
                print("request refresh")

            else:
                msg_buffer.append(msg_from_client)            # add to messages

                if len(msg_buffer) > MSG_BUFFER_SIZE:         # if buffer is full, remove oldest message
                    msg_buffer.remove(0)


if __name__ == '__main__':
    main()


