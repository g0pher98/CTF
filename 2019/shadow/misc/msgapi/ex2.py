from Crypto.PublicKey import RSA
from Crypto.Util import *
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode,b64encode
from Crypto.Cipher import PKCS1_v1_5

pkey = """MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI8EUQvSHgJQF5zuWR0jfGC0aOAgveEo2ma73v7FryV/FORDZOpdEEjvWz4kpmNwBanUl73uLiHFaHco81FVwIK9z/KdnglawjTrV1Gg4XVPvWE1PqVRDFkAVRZX/y9jY7MsuN0b10Ozk8h+sLv0nQDEGFy7DdhWvzjDJb6j2j13AgMBAAECgYAtbx2gN7w41+Dohf/hdeiJgEbhDQXFhgj8IisRnROrQdgNPCvPGImX4hKGh3YkmO3zqgoa2JPnPqOVV3kVGbzyUgZnpcb5wR3YLzfmkeU+QkFKCD+A59jRc2TJOIV8FL8v+KS4NW2RN+nru63OEN6tJg9LkH4fUMN/SRK9WRIeAQJBAM+7O2PTOkj6LhInHvUChlLFzUWzspPnHOVjaxkONa1/OGbJtU5GdCyj2AOa15DOzMurlJCQLk22GKAF8n5vmbcCQQCwP5VJcxJAwaqEl3YUb+yuxVumokvRb+Ec+3LqKje0FOqeVT/5kCODpw3GRKTpCM4NnhfL8IKN/kFg0xcz1XpBAkA6pGuGqcmpcl7xJvQZTKYo1cg2Jh2CnVrN8vv37cf/e4urkMPLHh6Lv5Eqq1qxeX/c+0oMaXd43rAi9KrZQJ4PAkAYbqgGR5JnMbGuscRnruBTlf5Pij4SaXz+ZIkYlwOjziZ8DntQ4D9cF8NcEdX+i/7selb4KX4fqvhrMLgNsnFBAkEAr5MuiHM+QFurgHDYlddURe9Ux/m27oMlhbxpxqBRokzWRSR1QnSyzafgh3hjQloYfdStccLRM4oxz8j4m/HPiQ=="""

keyDER = b64decode(pkey)
keyPub = RSA.importKey(keyDER)

grizzly = "01000111011100100110100101111010011110100110110001111001"

print(number.long_to_bytes(keyPub.p))
'''
print(keyPub.n)
print(keyPub.e)
print(keyPub.d)
print(keyPub.p)
print(keyPub.q)
print(keyPub.u)

print(bin(keyPub.n))
print(bin(keyPub.e))
print(bin(keyPub.d))
print(bin(keyPub.p))
print(bin(keyPub.q))
print(bin(keyPub.u))

print(number.long_to_bytes(keyPub.n))
print(number.long_to_bytes(keyPub.e))
print(number.long_to_bytes(keyPub.p))
print(number.long_to_bytes(keyPub.q))
print(number.long_to_bytes(keyPub.d))
print(number.long_to_bytes(keyPub.u))



enc = pow(number.bytes_to_long(b"Grizzly"), keyPub.d, keyPub.n)


pkcs = PKCS1_v1_5.new(keyPub)
print(pkcs)

php= 0x84E04661F55E8D47623029DF0A60B0B5
print("\n\n\n\n")
msg = pow(number.bytes_to_long(b"Grizzly"), keyPub.d, keyPub.n)
print(number.long_to_bytes(msg))

'''
