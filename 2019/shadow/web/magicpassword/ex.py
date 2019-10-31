import requests

res = requests.post("http://52.231.24.87:55555", data={
	'a' : 48291204,
	'b' : 48291204
})
print(res.text)