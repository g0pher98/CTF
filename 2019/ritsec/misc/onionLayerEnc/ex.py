import base64

def isBase64(s):
	try:
		return base64.b64encode(base64.b64decode(s)) == s
	except Exception:
		return False

def isBase32(s):
	try:
		return base64.b32encode(base64.b32decode(s)) == s
	except Exception:
		return False

def isBase16(s):
	try:
		return base64.b16encode(base64.b16decode(s)) == s
	except Exception:
		return False
	
with open("encode.txt", "r") as f:
	data = f.read()
	for i in range(150):
		if isBase16(data):
			data = base64.b16decode(data)
		elif isBase32(data):
			data = base64.b32decode(data)
		elif isBase64(data):
			data = base64.b64decode(data)
		else:
			print(data)
			break