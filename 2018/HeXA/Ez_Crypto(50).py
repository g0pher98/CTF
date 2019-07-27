def prob(text, key):
    min = 97
    max = 122
    res = ""
    for i in text:
        if i in ['{', '}', '_']:
            res += i
        else :
            idx = ord(i)+key
            if idx > max:
                idx = min+(idx-max)%(max-min+1)
            elif idx < min:
                idx = max-(min-idx)%(max-min+1)
            res += chr(idx)
    return res


for i in range(100):
    result = prob("mshn{jshzzpjhs_ayhkpapvuhs_jhlzhy_jpwoly}", i)
    print(result)
