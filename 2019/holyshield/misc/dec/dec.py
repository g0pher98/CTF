from datetime import datetime
from Crypto.Cipher import AES
import random, base64, sys, struct

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
    data = enc[4+bs:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(data)
    
    return unpad(dec, datasize)




'''
print("!!! encrypt")
srand(time())
key = bytes([random.randint(0,0xff) for _ in range(16)])
iv = bytes([random.randint(0,0xff) for _ in range(16)])
enc = encrypt(data, key, iv)
print(key)
print(enc)
'''


time = lambda: int(datetime.now().timestamp())
random.seed(time)

data = open("./flag.txt.enc", 'rb').read()

datasize = struct.unpack("<I", data[:4])[0]
origin_iv = data[4:4+bs]

for t in range(1562800000, 0, -1):
	if t % 100000 == 0:
		print(t)
	time = lambda: t
	random.seed(time)
	key = bytes([random.randint(0,0xff) for _ in range(16)])
	iv = bytes([random.randint(0,0xff) for _ in range(16)])
	if origin_iv == iv:
		print(t)
		print("oh!")
		break
					
