# CyBRICS CTF 2019
with team `ROKA`. (198 / 775)  
[Mic Check (Cyber, Baby, 10 pts)](#mic-check-cyber-baby-10-pts)  
[Caesaref (Web, Hard, 50 pts)](#caesaref-web-hard-50-pts)  
[Oldman Reverse (Reverse, Baby, 10 pts)](#oldman-reverse-reverse-baby-10-pts)  
[Sender (Network, Baby, 10 pts)](#sender-network-baby-10-pts)  
[Warmup (Web, Baby, 10 pts)](#warmup-web-baby-10-pts)  
[ProCTF (CTB, Baby, 10 pts)](#proctf-ctb-baby-10-pts)
[Zakukozh (Cyber, Baby, 10 pts)](#zakukozh-cyber-baby-10-pts)

# Mic Check (Cyber, Baby, 10 pts)
> Have you read the [game rules](https://cybrics.net/rules)? There's a flag there.  

문제에서 game rules를 확인했는지 물어보았다. 실제로 확인해보니 `What's a CTF` 섹션에서 flag를 발견할 수 있었다.  
flag : `cybrics{W3lc0M3_t0_t3h_G4M#}`

# Caesaref (Web, Hard, 50 pts)
> There is an additional one: Fixaref  
> This web resource is highly optimized:  
> http://45.77.218.242/

# Oldman Reverse (Reverse, Baby, 10 pts)
> I've found this file in my grandfather garage. Help me understand what it does  
> [oldman.asm](https://cybrics.net/files/oldman.asm)

문제에서는 할아버지의 차고에서 아래 코드를 찾았다고 한다.
``` asm
.MCALL  .TTYOUT,.EXIT
START:
    mov #MSG r1
    mov #0d r2    ; for idx change
    mov #32d r3   ; for loop count
loop:       
    mov #MSG r1   ; r1 = 0
    add r2 r1     ; r1 = r2
    movb (r1) r0  ; r0 = msg[r1]
    .TTYOUT       ; print(r0)
    sub #1d r3    ; i-- 
    cmp #0 r3     ; 32 time loop check
    beq DONE      ; ``
    add #33d r2   ; r2 += 33
    swab r2       ; swap byte(8bit)
    clrb r2       ; clear byte(8bit)
    swab r2       ; swap byte(8bit)
    br loop
DONE: 
    .EXIT

MSG:
    .ascii "cp33AI9~p78f8h1UcspOtKMQbxSKdq~^0yANxbnN)d}k&6eUNr66UK7Hsk_uFSb5#9b&PjV5_8phe7C#CLc#<QSr0sb6{%NC8G|ra!YJyaG_~RfV3sw_&SW~}((_1>rh0dMzi><i6)wPgxiCzJJVd8CsGkT^p>_KXGxv1cIs1q(QwpnONOU9PtP35JJ5<hlsThB{uCs4knEJxGgzpI&u)1d{4<098KpXrLko{Tn{gY<|EjH_ez{z)j)_3t(|13Y}"
.end START
```
무슨 asm 문법인지 몰라서 검색해보니 PDP-11(https://en.wikipedia.org/wiki/PDP-11) 이라는 옛날 16bit 컴퓨터에 사용되는 asm 문법(https://en.wikipedia.org/wiki/PDP-11_architecture) 이었다. loop의 swab과 clrb 부분의 이해가 어려웠는데, `PDP-11에서 레지스터는 16bit`이다. 예를들어 r2의 값이 `0011110011111111` 라면 앞 8bit에 데이터가 있어서 전체 값에 큰 영향을 주게 된다.  

문제는 `msg 데이터의 크기가 256byte`라는 것이다. 8bit를 넘어가는 순간 out of range가 발생하기 때문에 swab과 clrb를 통해 막아준 것이다. `swab r2` 과정을 거치면 r2의 데이터가 왼쪽으로 8bit만큼 시프트 되면서 앞에있던 데이터가 뒤로 간다. 즉 `r2 == 1111111100111100`이 된다. 16bit기 때문에 앞 1바이트와 뒤 1바이트가 전환된 것이다. 그 다음 `clrb`를 통해 뒤 1바이트를 0으로 만들고 다시 `swab`으로 역전하여 올림된 데이터를 제거하는 과정이다. 위 asm을 python 코드로 간략하게 바꿔보면
``` python
if __name__ == '__main__':
	msg = """cp33AI9~p78f8h1UcspOtKMQbxSKdq~^0yANxbnN)d}k&6eUNr66UK7Hsk_uFSb5#9b&PjV5_8phe7C#CLc#<QSr0sb6{%NC8G|ra!YJyaG_~RfV3sw_&SW~}((_1>rh0dMzi><i6)wPgxiCzJJVd8CsGkT^p>_KXGxv1cIs1q(QwpnONOU9PtP35JJ5<hlsThB{uCs4knEJxGgzpI&u)1d{4<098KpXrLko{Tn{gY<|EjH_ez{z)j)_3t(|13Y}"""
	r2 = 0
	for i in range(32):
		print(msg[r2], end='')
		r2 += 33
		r2 %= 256

# result
# cybrics{pdp_gpg_crc_dtd_bkb_php}
```
위와 같은 코드가 되며, 출력 결과로 플래그를 얻을 수 있다.  
flag : `cybrics{pdp_gpg_crc_dtd_bkb_php}`

# Sender (Network, Baby, 10 pts)
> We've intercepted this text off the wire of some conspirator, but we have no idea what to do with that.  
> [intercepted_text.txt](https://cybrics.net/files/intercepted_text.txt)  
> Get us their secret documents

데이터를 가로챘다고 한다. 데이터 내용은 아래와 같다.  
``` smtp
220 ugm.cybrics.net ESMTP Postfix (Ubuntu)
EHLO localhost
250-ugm.cybrics.net
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-AUTH PLAIN LOGIN
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
AUTH LOGIN
334 VXNlcm5hbWU6
ZmF3a2Vz
334 UGFzc3dvcmQ6
Q29tYmluNHQxb25YWFk=
235 2.7.0 Authentication successful
MAIL FROM: <fawkes@ugm.cybrics.net>
250 2.1.0 Ok
RCPT TO: <area51@af.mil>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
From: fawkes <fawkes@ugm.cybrics.net>
To: Area51 <area51@af.mil>
Subject: add - archive pw
Content-Type: text/plain; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable
MIME-Version: 1.0

=62=74=77=2E=0A=0A=70=61=73=73=77=6F=72=64 =66=6F=72 =74=68=65 =61=72=63=
=68=69=76=65 =77=69=74=68 =66=6C=61=67=3A =63=72=61=63=6B=30=57=65=73=74=
=6F=6E=38=38=76=65=72=74=65=62=72=61=0A=0A=63=68=65=65=72=73=21=0A
.
250 2.0.0 Ok: queued as C4D593E8B6
QUIT
221 2.0.0 Bye
```
SMTP 메일서버인 ugm.cybrics.net에서 메일을 작성한 것 같다. AUTH LOGIN 명령을 보니 ID, PW가 base64로 인코딩 되어있는 것이 보인다. 메일 내용도 마치 ascii 코드처럼 보인다. F12(개발자도구)를 눌러 console로 디코딩 해보면 아래와 같은 데이터를 추출할 수 있다.
``` javascript
id = atob("ZmF3a2Vz")
pw = atob("Q29tYmluNHQxb25YWFk=")

c_raw = "=62=74=77=2E=0A=0A=70=61=73=73=77=6F=72=64 =66=6F=72 =74=68=65 =61=72=63==68=69=76=65 =77=69=74=68 =66=6C=61=67=3A =63=72=61=63=6B=30=57=65=73=74==6F=6E=38=38=76=65=72=74=65=62=72=61=0A=0A=63=68=65=65=72=73=21=0A"

c_ascii = c_raw.replace(/(=| )/g,'')

c_text = ""
for (i=0;i<c_ascii.length/2;i++) {
    c_text += String.fromCharCode('0x' + c_ascii[i*2] + c_ascii[i*2+1])
}

console.log("ID : " + id + "\nPW : " + pw + "\nContent : " + c_text)

/* result
ID : fawkes
PW : Combin4t1onXXY
Content : btw.

passwordforthearchivewithflag:crack0Weston88vertebra

cheers!
*/
````
smtp 메일서버에 접근할 수 있는 메일 발신자 계정 로그인 정보와 메일의 내용을 확인했다. 패스워드가 있는 아카이브의 비밀번호가 `crack0Weston88vertebra` 라고 한다.  
``` bash
root@raspberrypi:~# nmap ugm.cybrics.net -p pop3

Starting Nmap 7.40 ( https://nmap.org ) at 2019-07-22 04:14 UTC
Nmap scan report for ugm.cybrics.net (136.244.67.129)
Host is up (0.28s latency).
rDNS record for 136.244.67.129: 136.244.67.129.vultr.com
PORT    STATE SERVICE
110/tcp open  pop3
```
해당 메일에 pop3 포트가 열려있는 것을 확인했다. 110번으로 접속하여 송신했던 메일을 열람했다. (pop3 command : https://www.electrictoolbox.com/article/networking/pop3-commands/)
데이터가 생각보다 컸고, 코드를 짜서 데이터를 가져올까 했지만 gmail에 pop3 계정을 등록해서 메일을 가져왔다. 메일에 첨부되어있던 암호가 걸려있는 zip 파일을 `crack0Weston88vertebra` 비밀번호로 열었고, 안에있던 pdf 파일을 열어보니 플래그가 있었다.  
flag : `cybrics{Y0uV3_G0T_m41L}`

# Warmup (Web, Baby, 10 pts)
> E_TOO_EASY  
> [Just get the flag](http://45.32.148.106/)

쉽다고 하는것 같다. 링크를 클릭해서 들어가면 `/`에 접속했다가 `/final.html`로 리다이렉트 된다. `/`에 접속 후 리다이렉트 되기 때문에 `/`의 데이터를 볼 수 있다.
``` bash
root@raspberrypi:~# wget 45.32.148.106
--2019-07-22 04:59:46--  http://45.32.148.106/
Connecting to 45.32.148.106:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 123240 (120K) [text/html]
Saving to: ‘index.html’

index.html                100%[====================================>] 120.35K   140KB/s    in 0.9s    

2019-07-22 04:59:47 (140 KB/s) - ‘index.html’ saved [123240/123240]

root@raspberrypi:~# cat index.html | grep flag
Here is your base64-encoded flag: Y3licmljc3s0YjY0NmM3OTg1ZmVjNjE4OWRhZGY4ODIyOTU1YjAzNH0=
root@raspberrypi:~# echo "Y3licmljc3s0YjY0NmM3OTg1ZmVjNjE4OWRhZGY4ODIyOTU1YjAzNH0=" | base64 -d
cybrics{4b646c7985fec6189dadf8822955b034}
```
flag : `cybrics{4b646c7985fec6189dadf8822955b034}`

# ProCTF (CTB, Baby, 10 pts)

> We Provide you a Login for your scientific researches. Don't try to find the flag.  
> ssh pro@95.179.148.72  
> Password: iamthepr0

ssh에 접속하면 아래와 같이 나온다.
```bash
root@raspberrypi:~# ssh pro@95.179.148.72

(...)

WARNING: Your kernel does not support swap limit capabilities or the cgroup is not mounted. Memory limited without swap.
?-
```
여러 키를 눌러보다가 이 프로그램을 종료시키면 쉘이 나올것 같아서 CTRL+C를 연타했다.
``` bash
?- ^C
^C

WARNING: By typing Control-C twice, you have forced an asynch
WARNING: interrupt.  Your only SAFE operations are: c(ontinue
WARNING: s(stack) and e(xit).  Notably a(abort) often works, 
WARNING: leaves the system in an UNSTABLE state

Action (h for help) ? Options:
a:           abort         b:           break
c:           continue      e:           exit
g:           goals         s:           C-backtrace
t:           trace         p:		  Show PID
h (?):       help
```
사용할 수 있는 명령들이 나온다. `abort`를 선택하면 아까 그 입력 환경이 다시 나온다. 혹시 여기서도 명령같은 것을 사용할 수 있지 않을까 싶어 탭을 연타했다.
``` bash
?- 
abort
abs
access
access_level
acos
acosh
active
acyclic_term
add_import
address
... skipped 246 rows
?- base
base            base32_char     base64_encoded
base32          base64          base64url
?- sh
sha_hash                   shift
sha_hash_ctx               shift_time
sha_new_ctx                shlib
shared                     shlib_atom_to_term
shared_object              show_again
shared_object_extension    show_completions
shared_object_handle       show_coverage
shared_object_search_path  show_non_termination
shell                      show_profile
?- shell
|    ^C
^C
```
shell 명령을 쓸 수 있는듯 했으나 아무런 반응이 없었다. 그래서 위에서 보았던 `WARNING: s(stack) and e(xit).  Notably a(abort) often works` 에러를 기준으로 검색해봤다. `SWI-Prolog`라는 환경인것 같다(https://www.swi-prolog.org/). 잘 살펴보니 shell 관련 명령에 대한 설명이 있다(https://www.swi-prolog.org/pldoc/man?section=system). 명령 체계가 모두 온점(.)으로 끝난다. 이제 명령을 실행해보자.
``` bash
?- shell.
$ bash
user@b4e55f39ad8b:/$ ls
bin   dev  home  lib64	mnt  proc  run	 srv  tmp  var
boot  etc  lib	 media	opt  root  sbin  sys  usr
user@b4e55f39ad8b:/$ cd ~
user@b4e55f39ad8b:~$ ls
flag.txt
user@b4e55f39ad8b:~$ cat flag.txt 
cybrics{feeling_like_a_PRO?_that_sounds_LOGical_to_me!____g3t_it?_G37_1T?!?!_ok_N3v3Rm1nd...}
```
인자를 주지 않아서 에러가 뜰 줄 알았는데 바로 sh가 떴고, bash로 변경해서 flag를 확인할 수 있었다.  
flag : `cybrics{feeling_like_a_PRO?_that_sounds_LOGical_to_me!____g3t_it?_G37_1T?!?!_ok_N3v3Rm1nd...}`

# Zakukozh (Cyber, Baby, 10 pts)
> This image containing flag is encrypted with affine cipher. Scrape it
> [zakukozh.bin](https://cybrics.net/files/zakukozh.bin)

flag를 포함한 이미지가 affine 암호(https://en.wikipedia.org/wiki/Affine_cipher) 를 통해 암호화 되었다고 한다. 실제로 바이너리를 열어보면 알아볼 수 없다. 아핀 암호는 (a, b)인 키를 (ax + b) mod 256 형태로 암호화를 진행한다. 아핀암호 특성상 암호문을 암호화를 통해 복호화로 만들 수 있고, 같은 바이트는 암호화 이후 항상 같은 데이터다.  

원본 파일이 이미지 파일인 것은 문제에서 알려주었으니 png, jpg, jpeg 중 하나일 가능성이 매우 높다. 아핀 암호의 특성을 통해 시그니처에 중복되는 위치가 바이너리에서도 중복되는지 검사하여 직관적으로 jpg와 jpeg는 아님을 알 수 있다. png라고 가정하고 코드를 작성했다.
```python
def findKey(signature):
    png = ['89', '50', '4e', '47', '0d', '0a', '1a', '0a']
    for i in range(256):
        for j in range(256):
            if png == ["%02x"%((int(c, 16)*i+j)%256) for c in signature]:
                print("[*] Find Key! : ({}, {})".format(i,j))
                return (i, j)

def affineEncrypt(key, origin_data):
    result = ''
    for i in origin_data:
        result += chr((key[0]*int(i, 16)+key[1])%256)
    return result

if __name__ == '__main__':
    f = open("./zakukozh.bin", "rb")
    data = ["%02x"%int(ord(i)) for i in f.read()]
    key = findKey(data[:8])
    f.close()

    f = open("./result.dat", "wb")
    f.write(affineEncrypt(key, data))
    print("[*] Make Decrypt File : ./result.dat")
    f.close()

# result
# [*] Find Key! : (239, 233)
# [*] Make Decrypt File : ./result.dat
```
암호화 전, 후 데이터를 일부 알고 있고, 암호화 방식이 복잡하지 않으므로 경우의 수를 모두 대입해서 찾는 방식으로 코드를 작성했다. 평문으로 되돌리기 위해 필요한 키는 `(239, 233)`이다. 암호문을 위 키로 다시 암호화하면 원본 이미지 파일이 나온다.  
``` bash
root@raspberrypi:~# file result.dat 
result.dat: PNG image data, 621 x 219, 8-bit/color RGB, non-interlaced
```
이미지를 열어보면 flag가 들어있다.
flag : `cybrics{W311_C0M3_2_CY13R1C5}`

