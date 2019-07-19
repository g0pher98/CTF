result = "7b717c7a66772e5748422d6f29537a2e42757460"

def re_Tok(res):
    org = ""
    for i in res:
        org += chr(ord(i)^int('1d',16))
    return org



r1 = ""
for i in range(0, len(result), 2):
    r1 += chr(int(result[i:i+2], 16))

r2 = re_Tok(re_Tok(re_Tok(r1)))


print(r2)

