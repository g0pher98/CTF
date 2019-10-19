import sys
from Crypto.Cipher import AES
from Crypto.Util.number import inverse
import base64

def decrypt(key, text):
	d = ''
	for i in range(len(text)):
		f = ord(text[i]) - 0x20 # (a+b) % m 
		m = 0x7f - 0x20
		b = ord(key[i%len(key)]) - 0x20

		if f < b: # a = m + f - b
			d += chr(m + f - b + 0x20)
		else: # a = f - b
			d += chr(f - b + 0x20)
	return d


key1 = "SECCON"
key2 = "seccon2019"

cipher = AES.new(key2 + chr(0x00) * (16 - (len(key2) % 16)), AES.MODE_ECB)
res = "FyRyZNBO2MG6ncd3hEkC/yeYKUseI/CxYoZiIeV2fe/Jmtwx+WbWmU1gtMX9m905"
res = base64.b64decode(res)
res = cipher.decrypt(res).decode('ascii')
res = decrypt(key1, res)
print(res)

# SECCON{Success_Decryption_Yeah_Yeah_SECCON}?AA56

