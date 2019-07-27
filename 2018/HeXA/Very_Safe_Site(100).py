import requests

URL = "http://play.hexa.pro/problem/99f02f561cce563e851d22c4fb85e93a/"
HEADERS = {"User-Agent" : "JOMUJE", "Referer":"jandimuje.ac.kr" }
res = requests.get(URL, headers = HEADERS)
print(res.text)

#flag{N0W_y0u_caN_mak3_S3V3ral_T00ls!}
