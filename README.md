# Lightweight encrypted messaging app in python

## Specifications

### Encryption
We use AES-256 symetric encryption. The key must be stored in the project's parent directory in a file named 'key' (default).
You can change this setting by editing [this line](crypto.py#L7).

### Server side
The server decrypts the messages on the fly to check whether it is a client request.
The messages are then stored encrypted. The server has a buffer of 30 messages.

### Client side
The client uses a configuration file [client.cfg](client.cfg) which must be of the form 'pseudo,ipv4_address,port'.
The client consists of two parts, since we won't do any GUI (command line rules).

[client_display.py](client_display.py) is used to display the messages stored in the server.
To do so you must send ```!refresh```.

[client_send.py](client_send.py) is used to send messages. Just type in what you want to say. There are excluded caracters: ```çèüéöàä£```.


Developed by [Hédi Sassi](https://github.com/hedi-sassi "Hédi's GitHub") and [Simon Perriard](https://github.com/simon-perriard "Simon's GitHub") when we were bored
