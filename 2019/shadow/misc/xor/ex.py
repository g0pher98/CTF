from Crypto.Util import number

a = "4d616368696e65204c616e67756167650a0a" # 0 b'Machine Language\xaa
b = "5589e5b91200000031d280b200204000ff4283f900740349ebf089ecc3"
c = "7756167650a0a"
d = "466c6167" # flag
e = "8c979e9b908884979acecfa8a088cf8dcebb82"

for k in range(0x100):
	prob = e
	flag = ""
	for i in range(len(prob)//2):
		#print(prob[i*2:i*2+2])
		flag += hex(int(prob[i*2:i*2+2],16)^k)[2:]
		
	#flag = int(flag, 16)
	flag = number.long_to_bytes(int(flag,16))
	print(k , flag)
	