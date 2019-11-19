import requests
from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Util import number

url = "http://ctfchallenges.ritsec.club:3000"

s = requests.Session()

res = s.get(url + "/auth", params={'name':"g0pher'"})
#data = res.json()
#print(b64decode(data['token']))
#data['name'] = 'admin'

#res = s.post(url + "/api/normal", params=data)
print(res.text)