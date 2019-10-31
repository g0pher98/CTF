import base64

data = ["fGdu", "a2B4", "dDpH", "Tks/", "WFBt", "OTtQ", "W09t", "c2py"]


## case 1
b64 = "".join(data)
print(b64)
print(base64.b64decode(b64))

## case 2
b64 = "".join(data[::-1])
print(base64.b64decode(b64))

## case 3
b64 = "".join([i[::-1] for i in data])
print(base64.b64decode(b64))

## case 4
b64 = "".join([i[::-1] for i in data[::-1]])
print(base64.b64decode(b64))