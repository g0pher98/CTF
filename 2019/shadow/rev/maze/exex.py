# -*- coding: utf8 -*-
from pwn import *

context.log_level='debug'

value = [449, 499, 436, 467, 235, 304, 320, 467, 137, 445, 955, 977, 283, 971, 960, 620, 962, 979, 480, 979, 557, 837, 505, 1005, 982, 1074, 942, 963, 1014, 589, 950, 1164, 483, 948, 1187, 605, 842, 393, 952, 634, 1192, 1006, 735, 961, 843, 963, 492, 409, 1151, 1065, 730, 963, 1190, 1176, 740, 1062, 598, 952, 1023, 398, 950, 594, 1007, 498, 874, 970, 843, 501, 635, 158, 274, 384, 966, 942, 424, 395, 380, 520, 474, 508, 947, 990, 602, 532, 925, 729, 947, 736, 963, 271, 535, 530, 345, 582, 347, 571, 423, 332, 383, 1137]

for i in range(101):
	x = process("./maze")
	x.sendlineafter("WW WW\n\n", "1")
	for v in value:
		x.sendlineafter("=======\n", str(v))
	for j in range(1,2000):
		x.sendlineafter("=======\n", str(j))
		x.recvuntil("INPUT")
		data = x.recv(1024)#x.recvline()
		if "WRONG" not in data:
			print("Level"+ str(i)+" : "+str(j))
			value.append(j)
			x.close()
			break
		if "shadow" in data or "SHADOW" in data:
			print(data)
			exit(1)
		else:
			x.sendline("y")
	else: 
		print("nono?")
print(value)