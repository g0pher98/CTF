import jwt

pubkey = open('public.pem', 'r').read()

jwtoken = jwt.encode({"data":"test"}, key=pubkey, algorithm='HS256')

print(jwtoken)