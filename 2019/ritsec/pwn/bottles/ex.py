import re

flag = ""
for i in range(1, 1000):
	with open("%03d.c.out"%i,"rb") as f:
		data = f.read()
		res = re.compile(b'\x0f\xb6\x05..\x04\x08').findall(data)[-1]
		cmp = bytes([res[3], res[4]])
		res = re.compile(b'\xC6\x05..\x04\x08.').findall(data)
		for idx in range(len(res)-1, 0, -1):
			if b'\xC6\x05'+ cmp +b'\x04\x08' in res[idx]:
				flag += chr(res[idx][-1])
				break


print(re.compile('RITSEC{[^\}]+}').findall(flag))