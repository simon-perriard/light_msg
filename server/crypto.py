
import base64
from Crypto.Cipher import AES
from Crypto import Random


PATH_TO_KEY= "../../key"

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# crypto functions inspired by :
# https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html


def encrypt(msg):

    private_key = read_key(PATH_TO_KEY)

    raw = pad(msg)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)

    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(msg):

    private_key = read_key(PATH_TO_KEY)

    enc = base64.b64decode(msg)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


def read_key(path):
    f = open(path, "r")

    if f.mode == 'r':
        return f.read(16).encode()

    exit(-1)