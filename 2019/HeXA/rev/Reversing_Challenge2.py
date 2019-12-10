result = "}xhzbbo_tangvup{tnys"
orginal = ""

def re_Func1(v2):
    a1 = ord(v2)
    if a1 >= 77 and a1 <= 90 or a1 >= 109 and a1 <= 122:
        a1 -= 13
    elif a1 >= 65 and a1 <= 77 or a1 >= 97 and a1 <= 109:
        a1 += 13
    return a1

def re_Func2(v5):
    return v5[::-1]



result = re_Func2(result)

for i in result:    
    org = re_Func1(i)
    orginal += chr(org)


print(orginal)
