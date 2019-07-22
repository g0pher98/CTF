# CyBRICS CTF 2019
with team `ROKA`. (198 / 775)  
[Mic Check (Cyber, Baby, 10 pts)](#mic-check-cyber-baby-10-pts)  
[Caesaref (Web, Hard, 50 pts)](#caesaref-web-hard-50-pts)  
[Oldman Reverse (Reverse, Baby, 10 pts)](#oldman-reverse-reverse-baby-10-pts)  
[Sender (Network, Baby, 10 pts)](#sender-network-baby-10-pts)  
[Warmup (Web, Baby, 10 pts)](#warmup-web-baby-10-pts)  

# Mic Check (Cyber, Baby, 10 pts)
`Have you read the game rules? There's a flag there.`  
문제에서 game rules를 확인했는지 물어보았다. 실제로 확인해보니 `What's a CTF` 섹션에서 flag를 발견할 수 있었다.  
flag : `cybrics{W3lc0M3_t0_t3h_G4M#}`

# Caesaref (Web, Hard, 50 pts)

# Oldman Reverse (Reverse, Baby, 10 pts)
`I've found this file in my grandfather garage. Help me understand what it does`  
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
`We've intercepted this text off the wire of some conspirator, but we have no idea what to do with that.`  
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
`E_TOO_EASY`  
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
