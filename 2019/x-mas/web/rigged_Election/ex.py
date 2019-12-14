import requests

URL = "http://challs.xmas.htsp.ro:11001/"
md5table = eval(open("./md5table.txt", "r").read())

def hashing(depth, now=0, string=""):
	if depth == now:
		enc = md5()
		enc.update(salt+string)
		md5table[string] = enc.hexdigest()
		return
	for e in elements:
		hashing(depth, now = now+1, string = string+e)

def vote(id):
	key = requests.get(URL+"vote.php", params={'g':1}).text()
	for string_v,hash_v in md5table:
		if hash_v[:len(key)] == key:
			requests.get(URL+"vote.php", params={'id':id, 'h':string_v})

for i in range(200):
	vote(16793)