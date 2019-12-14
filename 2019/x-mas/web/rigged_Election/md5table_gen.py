from hashlib import md5

md5table = {}


elements = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
salt = "watch__bisqwit__"

def hashing(depth, now=0, string=""):
	if depth == now:
		enc = md5()
		enc.update(salt+string)
		md5table[string] = enc.hexdigest()
		return
	for e in elements:
		hashing(depth, now = now+1, string = string+e)

# length = 7~25
for i in range(7,25):
	print("=== %d ===" % i)
	hashing(i)
	
		
with open("./md5table.txt", "w") as f:
	f.write(str(md5table))