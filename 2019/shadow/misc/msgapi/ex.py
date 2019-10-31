import requests
import json

grizzly = ['47', '72', '69', '7a', '7a', '6c', '79']

class MsgAPI:
	URL = "http://13.209.63.227:8010/msg/"
	def __init__(self):
		self.recvlist=[]
		self.id=""
		self.pw=""
		self.pkey=""
		
	def createUser(self, user_id, user_pw):
		res = requests.get(self.URL+"create.do", params = {
			"ID" : user_id,
			"Password" : user_pw
		})
		res = json.loads(res.text)
		print(res)
		return
		if res['result'] == "Success!":
			self.id = user_id
			self.pw = user_pw
			self.pkey = res['private key']
			print(user_id+" create Success!")
			return True
		else:
			print("createUser Error : "+res['result'])
			return False

	def sendMsg(self, uid, msg, msgto):
		res = requests.post(self.URL+"send.do", data = {
			'Receiver' : msgto,
			'Sender' : uid,
			'Msg' : msg
		}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = json.loads(res.text)
		print(res)
		if res['result'] == "Success!":
			print("Send Message to "+msgto+" Success!")
			return True
		else:
			print("sendMsg Error : "+res['result'])
			return False
	
	def recvMsg(self, uid, pkey):
		res = requests.post(self.URL+"recent.do", data={
			'ID' : uid,
			'Pkey' : pkey
		}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = json.loads(res.text)
		#mail = [res['sender'], res['msg']]
		#recvlist.append(mail)
		print("===recv===")
		print(res)
		return res
		if res['result'] == "Success!":
			print(mail)
			return True
		else:
			print("recvMsg Error : "+res['result'])
			return False

#sender = MsgAPI()
#recver = MsgAPI()

#sender.createUser("send01", "pwg0pher")
#recver.createUser("recv01", "pwg0pher")

#sender.sendMsg("hi", "Grizzly") # admin : Grizzly




#MsgAPI().createUser("hi", "hi")
pk = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI8EUQvSHgJQF5zuWR0jfGC0aOAgveEo2ma73v7FryV/FORDZOpdEEjvWz4kpmNwBanUl73uLiHFaHco81FVwIK9z/KdnglawjTrV1Gg4XVPvWE1PqVRDFkAVRZX/y9jY7MsuN0b10Ozk8h+sLv0nQDEGFy7DdhWvzjDJb6j2j13AgMBAAECgYAtbx2gN7w41+Dohf/hdeiJgEbhDQXFhgj8IisRnROrQdgNPCvPGImX4hKGh3YkmO3zqgoa2JPnPqOVV3kVGbzyUgZnpcb5wR3YLzfmkeU+QkFKCD+A59jRc2TJOIV8FL8v+KS4NW2RN+nru63OEN6tJg9LkH4fUMN/SRK9WRIeAQJBAM+7O2PTOkj6LhInHvUChlLFzUWzspPnHOVjaxkONa1/OGbJtU5GdCyj2AOa15DOzMurlJCQLk22GKAF8n5vmbcCQQCwP5VJcxJAwaqEl3YUb+yuxVumokvRb+Ec+3LqKje0FOqeVT/5kCODpw3GRKTpCM4NnhfL8IKN/kFg0xcz1XpBAkA6pGuGqcmpcl7xJvQZTKYo1cg2Jh2CnVrN8vv37cf/e4urkMPLHh6Lv5Eqq1qxeX/c+0oMaXd43rAi9KrZQJ4PAkAYbqgGR5JnMbGuscRnruBTlf5Pij4SaXz+ZIkYlwOjziZ8DntQ4D9cF8NcEdX+i/7selb4KX4fqvhrMLgNsnFBAkEAr5MuiHM+QFurgHDYlddURe9Ux/m27oMlhbxpxqBRokzWRSR1QnSyzafgh3hjQloYfdStccLRM4oxz8j4m/HPiQ=="

#MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI8EUQvSHgJQF5zuWR0jfGC0aOAgveEo2ma73v7FryV/FORDZOpdEEjvWz4kpmNwBanUl73uLiHFaHco81FVwIK9z/KdnglawjTrV1Gg4XVPvWE1PqVRDFkAVRZX/y9jY7MsuN0b10Ozk8h+sLv0nQDEGFy7DdhWvzjDJb6j2j13AgMBAAECgYAtbx2gN7w41+Dohf/hdeiJgEbhDQXFhgj8IisRnROrQdgNPCvPGImX4hKGh3YkmO3zqgoa2JPnPqOVV3kVGbzyUgZnpcb5wR3YLzfmkeU+QkFKCD+A59jRc2TJOIV8FL8v+KS4NW2RN+nru63OEN6tJg9LkH4fUMN/SRK9WRIeAQJBAM+7O2PTOkj6LhInHvUChlLFzUWzspPnHOVjaxkONa1/OGbJtU5GdCyj2AOa15DOzMurlJCQLk22GKAF8n5vmbcCQQCwP5VJcxJAwaqEl3YUb+yuxVumokvRb+Ec+3LqKje0FOqeVT/5kCODpw3GRKTpCM4NnhfL8IKN/kFg0xcz1XpBAkA6pGuGqcmpcl7xJvQZTKYo1cg2Jh2CnVrN8vv37cf/e4urkMPLHh6Lv5Eqq1qxeX/c+0oMaXd43rAi9KrZQJ4PAkAYbqgGR5JnMbGuscRnruBTlf5Pij4SaXz+ZIkYlwOjziZ8DntQ4D9cF8NcEdX+i/7selb4KX4fqvhrMLgNsnFBAkEAr5MuiHM+QFurgHDYlddURe9Ux/m27oMlhbxpxqBRokzWRSR1QnSyzafgh3hjQloYfdStccLRM4oxz8j4m/HPiQ==

# pk = "MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgEk1m0ghvk9tzEJY2S19lQxUqEkbp1P00BsvrR445wQ7jEpYcbdm7x6IotqomRuRnIsJ+7ADqB7QQMelpijIz4jwEGn0/u0f79m8Kt08+mO8DbOlmPzuPGVTc6FGFOWNUAkMlWnbYMLMG/gfBrx/Q6BO3xsYFX1c8j9zain7HqFVAgMBAAE="

#MsgAPI().createUser("0", "0")

#MsgAPI().createUser("Grizzly", "grizzly")
#MsgAPI().sendMsg("<spt>", "", "Grizzly")
MsgAPI().createUser("a", "Grizzly")
MsgAPI().sendMsg('a', 'a', "Ｇrizzly")
MsgAPI().recvMsg('', "a")


