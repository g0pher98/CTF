from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Util import number
import jwt

key64 = b'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBquzMGkZlJmZm4pYppxeDmsGd\
8+9mOh5S9O7W7Gu5VByfl7i3JdCfGxRJdHscg6l321PeTXsXGZ7goHd4Xjv/FtKQ\
DyoaKql4Kl692KKKN/9xA6tKdOYQbZvPqyRXUVOGdyZ12qFBOQzI7ox22YL3ul/3\
nyiDR+p+JKbdVU6AWQIDAQAB'

enc_data = 'vi3EkFjU61hYVaUmDQhNcXQIoanmjxl9Ase7L3p8L7C4LIFmSnghxOA_rsd9oOcizxMLjombxNydqgUavZhjb3MCJH7XwzoHsvVLcVwEsDvokgSPyxke-gNp0zNjuzg2zjA6SKy2VgB-6OV1MS5W4-43NCrvWW6uDFFr9aPPLAM'

keyDER = b64decode(key64)
keyPub = RSA.importKey(keyDER)
enc = number.bytes_to_long(b64decode(enc_data))

text = number.long_to_bytes(keyPub.decrypt(enc))

print(text)