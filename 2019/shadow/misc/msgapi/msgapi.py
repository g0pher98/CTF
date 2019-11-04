import requests
import pprint
import json

class MsgAPI:
	sess = requests.Session()
	URL = "http://13.209.63.227:8010/msg/"
	def __init__(self):
		self.recvlist=[]
		self.id=""
		self.pw=""
		self.pkey=""
		
	def create(self, user_id, user_pw):
		res = self.sess.get(self.URL+"create.do", params = {
			"ID" : user_id,
			"Password" : user_pw
		})
		res = json.loads(res.text)
		if res['result'] is not "Fail!":
			self.id = user_id
			self.pw = user_pw
			self.pkey = res['private key']
			print(user_id+" create Success!")
			return True
		else:
			print("createUser Error : "+str(res))
			return False

	def send(self, receiver, message):
		res = self.sess.post(self.URL+"send.do", data = {
			'Sender' : self.id,
			'Receiver' : receiver,
			'Msg' : message
		}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = json.loads(res.text)
		pprint.pprint(res)
	
	def recv(self):
		res = self.sess.post(self.URL+"recent.do", data={
			'ID' : self.id,
			'Pkey' : self.pkey
		}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
		res = json.loads(res.text)
		pprint.pprint(res)

