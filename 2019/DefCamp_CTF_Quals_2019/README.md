(115 / 483)


Salad (Warmup - 1 pcts.) No bonus points.
Can you guess my favorite salad name? ONEQ{m3nq67n8l4559247641o321qm60q1mp7751m4075oqp72nl351q0072131p6oom1}
Author: Lucian



Address (Warmup - 1 pcts.) No bonus points.
What is your address?
Target: 206.81.24.129:9947
Author: Lucian



Cross or zero (Warmup - 1 pcts.) No bonus points.
Can you find the key and the flag? I bet. It is not an encryption. It is ZERO. Code:
```
import itertools
import base64

def string_xor(s, key):
    key = key * (len(s) / len(key) + 1)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key)) 

flag = """"
key = """"

print base64.b64encode(string_xor(flag, key))

# dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ==
```
Author: Lucian



Mountain (Warmup - 1 pcts.) No bonus points.
Take a look at those mountains!
Author: Lucian



Corrupt file (Warmup - 1 pcts.) No bonus points.
I can not recover this corrupt file!
Author: Lucian



Password (Warmup - 1 pcts.) No bonus points.
Can you find the password? I am asking for a friend.
Author: Lucian




imgur (Web - 211 pcts.) Bonus points for first 3 solvers.
This is an out of the box challenge with a very "professional" and complex interface. Get in and print the flag.
Target: https://imgur.dctfq19.def.camp
Author: Andrei


Downloader v1 (Web -)
https://downloader-v1.dctfq19.def.camp


게임
nc 206.81.24.129 2337

base
nc 206.81.24.129 4441

numbers
nc 206.81.24.129 2337