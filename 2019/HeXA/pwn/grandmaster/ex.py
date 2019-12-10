from pwn import *

lst = []

for i in range(10):
	print(lst)
	x = remote("play.hexa.pro", 7882)
	x.sendlineafter("menu:", "1")
	for j in lst:
		x.sendlineafter("direction:", j)
		
	for j in range(1000):
		x.sendlineafter("direction:", "0")
		res = x.recvuntil("Please input")
		if "WIN!!" in res:
			lst.append("0")
		else:
			src = res.index("was:") + 4
			dst = res[src:].index("\n")
			ans = res[src:src+dst]
			if ans == "Left":
				lst.append("1")
			elif ans == "Right":
				lst.append("2")
			else:
				lst.append("3")
	
	