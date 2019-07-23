# CyBRICS CTF 2019
with team `ROKA`. (198 / 775)  
[Mic Check (Cyber, Baby, 10 pts)](#mic-check-cyber-baby-10-pts)  
[Caesaref (Web, Hard, 50 pts)](#caesaref-web-hard-50-pts)  
[Oldman Reverse (Reverse, Baby, 10 pts)](#oldman-reverse-reverse-baby-10-pts)  
[Sender (Network, Baby, 10 pts)](#sender-network-baby-10-pts)  
[Warmup (Web, Baby, 10 pts)](#warmup-web-baby-10-pts)  
[ProCTF (CTB, Baby, 10 pts)](#proctf-ctb-baby-10-pts)  
[Zakukozh (Cyber, Baby, 10 pts)](#zakukozh-cyber-baby-10-pts)  
[Honey, Help! (rebyC, Baby, 10 pts)](#honey-help-rebyc-baby-10-pts)  
[Paranoid (Network, Easy, 50 pts)](#paranoid-network-easy-50-pts)  
[Tone (Forensic, Baby, 10 pts)](#tone-forensic-baby-10-pts)  

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

flag를 포함한 이미지가 affine 암호(https://en.wikipedia.org/wiki/Affine_cipher) 를 통해 암호화 되었다고 한다. 실제로 바이너리를 열어보면 알아볼 수 없다. 아핀 암호는 (a, b)인 키를 `(ax + b) mod 256` 형태로 암호화를 진행한다. 아핀암호 특성상 암호문을 암호화를 통해 복호화로 만들 수 있고, 같은 바이트는 암호화 이후 항상 같은 데이터다.  

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

# Honey, Help! (rebyC, Baby, 10 pts)

> HONEY HELP!!!  
> I was working in my Kali MATE, pressed something, AND EVERYTHING DISAPPEARED!  
> I even copied the [text from terminal](https://cybrics.net/files/honey_help.txt)  

무언가를 눌렀더니 모든게 사라졌다고 한다. 텍스트 추출본을 확인한 후 인코딩 문제를 해결하기 위해 개발자도구(F12)로 코드를 열어보니 아래와 같은 데이터가 있었다.
``` bash
root@myLOVELYcomputer:~/cybrics# ls -la
total 12
drwxr-xr-x  2 root root 4096 Jul 22  2019 .
drwxr-xr-x 21 root root 4096 Jul 22  2019 ..
-rw-r--r--  1 root root   44 Jul 22  2019 flag
root@myLOVELYcomputer:~/cybrics# echo $'\e(0'

âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# â”ŒâŽ½ -â”Œâ–’
â”œâŽºâ”œâ–’â”Œ 12
ââŽ¼â”¬â”‚âŽ¼-â”‚âŽ¼-â”‚  2 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ 4096 Jâ”¤â”Œ 22  2019 .
ââŽ¼â”¬â”‚âŽ¼-â”‚âŽ¼-â”‚ 21 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ 4096 Jâ”¤â”Œ 22  2019 ..
-âŽ¼â”¬-âŽ¼--âŽ¼--  1 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ   44 Jâ”¤â”Œ 22  2019 Â°â”Œâ–’Â±
âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# âŒâ–’â”œ Â°â”Œâ–’Â± 
âŒâ‰¤â‰âŽ¼â‹âŒâŽ½Ï€â¤0â”Œâ‰¤_âŒâŽ¼4âŽ»_1âŽ½_â”œâ¤â‹âŽ½_â–’â”Œ13â”¼â‹$â¤_0âŽ¼_â”¬4â”œ?Â£
âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# 

```
직관적으로 `ls -la` 명령어를 `echo $'\e(0'` 이후에 한번 더 작성했음을 알 수 있다. 이것을 힌트로 하나씩 대조해 보았다. 3byte가 한 문자로 매칭될 수 있었다.
``` javascript
{
	'a' : 'â–’'
	'b' : 'â‰'
	'c' : 'âŒ'
	'd' : 'â'
	'e' : 'âŠ'
	'f' : 'Â°â'
	'g' : '’Â±'
	'h' : 'â¤'  // guess
	'i' : 'â‹'
	'j' : ''
	'k' : ''
	'l' : 'â”Œ'
	'm' : 'â””'
	'n' : 'â”¼'       // guess
	'o' : 'âŽº'
	'p' : 'âŽ»'
	'q' : ''
	'r' : 'âŽ¼'
	's' : 'âŽ½'
	't' : 'â”œ'
	'u' : 'â”¤'
	'v' : ''
	'w' : 'â”¬'
	'x' : 'â”‚'
	'y' : 'â‰¤'
	'z'
}
```
약간의 게싱을 더해 테이블을 어느정도 만들어 냈고, 플래그를 얻을 수 있었다.  
flag : `cybrics{h0ly_cr4p_1s_this_al13ni$h_0r_w4t?}`

# Paranoid (Network, Easy, 50 pts)

> My neighbors are always very careful about their security. For example they've just bought a new home Wi-Fi router, and instead of just leaving it open, they instantly are setting passwords!  
> Don't they trust me? I feel offended.  
> [paranoid.zip](https://cybrics.net/files/paranoid.zip)  
> Can you give me their current router admin pw?  

이웃 사람이 보안에 대해 신중한것이 불만이라고 한다. 방금 새로운 Wi-Fi 라우터를 구입했고, 비밀번호를 설정했다고 한다. 패킷을 다운받아 열어보면 802.11 무선통신 패킷이 많이 보인다. 봐도 해석할 수 없기 때문에 `[Statics] - [Portocol Hierarchy]`를 통해 http 통신이 있음을 알 수 있었다.  

`http` 필터를 걸었더니 `wireless`와 같은 키워드가 보였고, Wi-Fi 라우터의 설정을 변경하기 위해 관리 페이지로 접속했음을 예측할 수 있다. 보통 수정 정보는 보통 `POST`를 통해 요청하기 때문에 `http.request.method == "POST"`로 필터링했다.  
``` bash
12809	131.599603	192.168.1.137	192.168.1.1	HTTP	1148	POST /req/admin HTTP/1.1  (application/x-www-form-urlencoded)
19173	189.067132	192.168.1.137	192.168.1.1	HTTP	817	POST /req/wlanApSecurity HTTP/1.1  (application/x-www-form-urlencoded)
```
두 개의 패킷이 보이는데 위의 패킷은 관리 페이지의 계정 정보를 수정하는듯 하고, 아래 패킷에서는 `WLAN_AP_WEP_KEY1=Xi1nvy5KGSgI2`를 발견할 수 있었다. 정확히는 모르지만 WEP 방식의 Key 값이 `Xi1nvy5KGSgI2`임을 알 수 있다. 이 키값을 이용해 802.11 패킷들을 해독할 수 있다. `[Edit] - [Preference...] - [Protocols] - [IEEE 802.11]`로 들어가서 `Decryption keys` 항목의 `Edit`을 클릭하면 키를 추가할 수 있는 창이 뜬다. `wep`형식을 선택하고, 아까 그 키값을 포맷에 맞게 hex로 변환한 `5869316e7679354b4753674932`로 넣는다.
``` bash
(...)
44098	601.596033	192.168.1.137	192.168.1.1	HTTP	1365	POST /req/wlanApSecurity HTTP/1.1  (application/x-www-form-urlencoded)
```
전보다 http post 패킷이 많아졌다. 맨 아래 패킷을 살펴보면 아까와 비슷하게 `WLAN_AP_WPA_PSK_passphrase=2_RGR_xO-uiJFiAxdA33-PsdanuK`라는 키워드를 찾을 수 있다. WEP가 보안에 취약하다는것을 알아서인지 이번에는 WPA로 비밀번호를 바꾼 듯 하다. 위와 같은 방법으로 키를 추가하는데 이번에는 `wpa-pwd`형식에 `2_RGR_xO-uiJFiAxdA33-PsdanuK`를 키로 넣으면 비밀번호를 변경한 이후 패킷들을 해독할 수 있다.
``` bash
(...)
50124	796.263229	192.168.1.137	192.168.1.1	HTTP	1242	POST /req/admin HTTP/1.1  (application/x-www-form-urlencoded)
```
계속 관리 페이지의 비밀번호를 수정하다가 맨 마지막에는 flag 값으로 비밀번호를 수정하는것을 확인할 수 있다.  
flag : `cybrics{n0_w4Y_7o_h1d3_fR0m_Y0_n316hb0R}`


# Tone (Forensic, Baby, 10 pts)

> Ha! Looks like this guy forgot to turn off his video stream and entered his password on his phone!  
> [youtu.be/11k0n7TOYeM](https://youtu.be/11k0n7TOYeM)  

스트리밍중인 상태에서 방송을 끄지 않고 비밀번호를 눌렀다고 한다. 링크를 타고 들어가면 예전 핸드폰의 키패드 누르는 소리가 들린다. DTMF(https://namu.wiki/w/DTMF) 라고 하는 이 소리를 분석해서 어떤 키패드를 눌렀는지 알아야 한다. 해당 영상을 mp3로 다운 받는다. 그리고 mp3를 분석할 Audacity(https://www.audacityteam.org/download/) 도 다운받고 설치한다.  

Audacity를 열어 mp3를 드래그 하면 파형이 나온다. 조금만 확대를 해보면 음이 나오는 부분이 어느 부분인지 알 수 있다. 분석이 필요한 `한개의 음` 영역을 드래그 하고, `[분석] - [스펙트럼 도식화]`를 선택하여 도식화된 보라색 그래프를 볼 수 있다.  

음을 찾는 방법은 그래프의 가장 높은 두개의 봉우리에 마우스를 가져다 대면 피크값이 나온다. 이 두 주파수 값을 DTMP 주파수 값과 비교하여 다음과 같은 값을 도출해냈다.  
`222 999 22 777 444 222 7777 7777 33 222 777 33 8 8 666 66 2 555 333 555 2 4`  
이를 키패드의 문자와 연결시키면 플래그가 나온다.  
flag : `cybrics{secrettonalflag}`

