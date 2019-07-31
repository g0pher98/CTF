def re_tok(result) :
	orginal = ""
	for i in result:
		orginal += chr(ord(i)+1)
	return orginal

result_text = "ci^dxs0ov\\pm1oh..k3\\c.^d\\kf`bz"

orginal_text = result_text
for i in range(3):
        orginal_text = re_tok(orginal_text)

print(orginal_text)
