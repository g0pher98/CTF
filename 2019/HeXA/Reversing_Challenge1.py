s = chr(95)+chr(85)+chr(88)+chr(94)+chr(66)+chr(87)+chr(80)+chr(90)
r = ""
for i in s:
    r += chr(ord(i)^int('0x39',16))

print(r)
