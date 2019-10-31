from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util import number
import random, base64, sys, struct

time = lambda: int(datetime.now().timestamp())
srand = random.seed


bs = AES.block_size


def pad(data):
    return data + (b"\x00" * (bs - len(data) % bs))

def unpad(data, size):
    return data[:-bs+size]

def encrypt(data, key, iv):
    datasize = len(data)
    data = pad(data)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(data)
    return struct.pack("<I", datasize) + iv + enc
    
def decrypt(enc, key):

    datasize = struct.unpack("<I", enc[:4])[0]
    iv = enc[4:4+bs]
    print(iv)
    data = enc[4+bs:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(data)
    
    return unpad(dec, datasize)
    
'''

if len(sys.argv) != 3:
    print("USAGE: %s [SOURCE] [DESTINATION]" % sys.argv[0])
    exit(-1)


try:
    with open(sys.argv[1], 'rb') as fp:
        data = fp.read()
except:
    print("ERROR: Cannot read %d" % sys.argv[1])
    exit(-1)


'''
data = b"aaa"
srand(time())

key = bytes([random.randint(0,0xff) for _ in range(16)])
iv = bytes([random.randint(0,0xff) for _ in range(16)])
print(number.bytes_to_long(iv))
enc = encrypt(data, key, iv)
decrypt(enc, key)


'''
try:
    with open(sys.argv[2], 'wb') as fp:
        data = fp.write(enc)
except:
    print("ERROR: Cannot write %d" % sys.argv[2])
    exit(-1)

'''
