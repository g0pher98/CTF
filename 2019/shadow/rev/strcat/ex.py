from Crypto.Util import number
import base64

print(number.long_to_bytes(0x1525036408702115646923191100970415))
print(number.long_to_bytes(1504970011192369641521700864032515049700))


data = b"\x15\x04\x97\x00\x11\x19\x23\x69\x64\x15\x21\x70\x08\x64\x03\x25"
num = number.bytes_to_long(data)
res = base64.b64decode(data)
print(res)


data = number.long_to_bytes(0x25036408702115646923191100970415)
res = base64.b64decode(data)
print(res)


