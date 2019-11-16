from pwn import *

x = process("./pages")
e = ELF("./libc-2.23.so")

x.interactive()