# SECARMY CTF 2.0 Junior
with team `t0paz`. (55 / 1655)
## Cryptography
SQUARE(200)  
Flag Basket(200)  
Exclusive OR Non-Exclusive(210)  
Old Days(300)  
## Misc
Directories(100)  
Look Inside(100)  
Get_Me(100)  
Quick Response(500)  
Poor prisoner(550)  
## Web
Prizes(101)  
web_salad(220)  
Silly Mongolian 2.0(300)  
Cookie Bank(300)  
## Binary / Reversing
Stringy(100)  
Smash it!(100)  
F-L-A-S-H(300)  
Backyard COWs(500)  
## Forensics
Its all in your head(100)  
secret(100)  
The_Confusion(300)  
The_B1N(300)  
Save Them(300)  
## Sign OFF
Thanks(50)  
## Starters
16+8(50)  
Die Basis(50)  
Easy Capture(50)  
IMAGE(50)  
Th3_G1F7(50)  
## Welcome
Welcome All(10)  
Netcat(20)  
InstaFamous(20)  

# SQUARE(200)
QR코드 이미지가 주어진다. 내용을 보면
```
43 15 13 11 42 32 54 { 41 42 _ 25 33 0 52 3_ 44 23 3_ 52 @ 54 }
```
이게 나온다. `Polybius square` 디코더로 복호화하면 평문이 나온다.  
> QR image reader : https://zxing.org/w/decode  
> Crypii : https://cryptii.com/  

flag : `secarmy{qr_kn0w_orn_w@y}`

# Flag Basket(200)
이미지가 주어지는데 열어보면 치환암호같이 생긴 암호문이 있다. 구글 드라이브에 업로드 해서 구글 문서로 열면 문자가 자동 추출이 된다. 이를 이용해서 카이사르 디코더로 해독해보면 평문이 나온다.  
flag : `secarmy{OCR_i5_lit}`

# Exclusive OR Non-Exclusive(210)
```
190f090b18071311125a1835035f35080b5f0309350c5a183559040918131a1e035a045f17
```
 라는 텍스트가 주어졌다. 제목에서 알 수 있듯이 XOR을 하면 될 것 같았다. CyberChef에서 `From Hex`로 포맷을 맞추어주고, `XOR Brute Force`를 선택한 뒤, `Crib` 속성을 `secarmy`로 지정해주면 다음과 같은 데이터가 나온다.  
```
Key = 4a: SECARMY[X.R.I..BA.IC.F.R..NCRYPTI.N.]
Key = 6a: secarmy{x0r_i5_ba5ic_f0r_3ncrypti0n5}
```
> CyberChef : https://gchq.github.io/CyberChef/  

flag : `secarmy{x0r_i5_ba5ic_f0r_3ncrypti0n5}`

# Old Days(300)
```
777 33 6 33 6 22 33 777 0 8 44 666 7777 33 0 666 555 3 0 3 2 999 7777 0 9 44 33 66 0 9 33 0 55 33 33 7 0 666 66 0 7777 6 2 7777 44 444 66 4 0 666 88 777 0 55 33 999 7 2 3 0 5 88 7777 8 0 8 666 0 7777 33 66 3 0 2 0 7777 444 66 4 555 33 0 6 33 7777 7777 2 4 33 0 9 33 555 555 0 555 33 8 7777 0 777 33 555 444 888 33 0 666 88 777 0 666 555 3 0 4 666 555 3 33 66 0 3 2 999 7777 0 9 444 8 44 0 8 33 2 0 2 66 3 0 7777 666 6 33 0 333 555 2 4 7777 0 7777 33 222 2 777 6 999 777 33 555 444 888 33 8 44 33 666 555 3 3 2 999 7777 7777 33 222 2 777 6 999 0 7777 666 0 8 44 33 0 333 555 2 4 0 444 7777 0 8 44 33 0 7777 8 777 444 66 4 0 22 33 8 9 33 33 66 0 8 44 33 0 7777 33 222 2 777 6 999 0 9 44 444 222 44 0 444 7777 0 777 33 555 444 888 33 8 44 33 666 555 3 3 2 999 7777 0 44 666 7 33 0 999 666 88 0 2 777 33 0 66 666 8 0 222 666 66 333 88 7777 33 3 0 4 666 666 3 0 555 88 222 55
```
옛날 휴대폰 키패드 숫자와 관련이 있어보여서 매칭되는 문자로 변환해보니 플래그가 나왔다.  
flag : `secarmy{relivetheolddays}`

# Directories(100)
```
It is a type of illusionary filesystem. It does not exist on a disk. Can U name it ?
```
가상 파일시스템의 일종이라고 한다.  
flag : `secarmy{/proc}`

# Look Inside(100)
wav 파일이 주어졌다. 나는 음원 관련된 문제는 `Audacity`을 이용한다. 파일을 열면 파형이 나오는데 별다른 특이사항은 보이지 않는다. 파형 말고 스펙트로그램(소리나 파동을 시각화)을 선택하면 숨겨진 플래그가 나온다.
flag : `secarmy{5p3ctrum5_@r3_@w3s0m3}`

# Get_Me(100)
압축파일이 주어져서 풀어보니 다음과 같은 문자가 나왔다.
```
EAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCA (...) AQAUIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQCAIBAEAQA====
```
데이터 끝에 패딩이 있는것으로 보아 base encoding 시리즈 중 하나일 거 같아서 몇개 넣어보니 Base32일 때 결과가 나왔다.
```
                                                                          
,adPPYba,  ,adPPYba,  ,adPPYba, ,adPPYYba, 8b,dPPYba, 88,dPYba,,adPYba,   
I8[    "" a8P_____88 a8"     "" ""     `Y8 88P'   "Y8 88P'   "88"    "8a  
 `"Y8ba,  8PP""""""" 8b         ,adPPPPP88 88         88      88      88  
aa    ]8I "8b,   ,aa "8a,   ,aa 88,    ,88 88         88      88      88  
`"YbbdP"'  `"Ybbd8"'  `"Ybbd8"' `"8bbdP"Y8 88         88      88      88  
                                                                          
                                                                          
                                                                   
            88 88          ,a8888a,   8b           d8  ad888888b,  
            88 88        ,8P"'  `"Y8, `8b         d8' d8"     "88  
            88 88       ,8P        Y8, `8b       d8'          a8P  
8b       d8 88 88       88          88  `8b     d8'        aad8"   
`8b     d8' 88 88       88          88   `8b   d8'         ""Y8,   
 `8b   d8'  88 88       `8b        d8'    `8b d8'             "8b  
  `8b,d8'   88 88        `8ba,  ,ad8'      `888'      Y8,     a88  
    Y88'    88 88888888888 "Y8888P"         `8'        "Y888888P'  
    d8'                                                            
   d8'                                                             
                                                       
       db        ad88888ba    ,ad8888ba,    88     88  
      d88b      d8"     "8b  d8"'    `"8b ,d88   ,d88  
     d8'`8b     Y8,         d8'         888888 888888  
    d8'  `8b    `Y8aaaaa,   88              88     88  
   d8YaaaaY8b     `"""""8b, 88              88     88  
  d8""""""""8b          `8b Y8,             88     88  
 d8'        `8b Y8a     a8P  Y8a.    .a8P   88     88  
d8'          `8b "Y88888P"    `"Y8888Y"'    88     88  
                                                       
                                       
```
ascii art를 표현한것 같다.  
flag : `secarmy{IL0V3ASC11}`

# Quick Response(500)
그나마 문제같았던(?) 문제가 나왔다. 문제에 있는 IP 주소로 nc 접속을 하면 엄청 큰 데이터를 볼 수 있는데, 글자를 작게 하고 화면을 최대로 키우면 QR코드임을 알 수 있다. 이 데이터를 받아서 이미지로 변환하는 코드를 짜야했다.
``` python
from PIL import Image

img = Image.new("RGB", (200,200), (255, 255, 255)) #200x200크기, 흰색채우기
dot = Image.new("RGB", (1,1), (0,0,0)) #1x1크기, 검은색 채우기

f = open("qr.txt","r")
data = f.read().replace("\n", "")

for y in range(200):
    for x in range(200):
        if data[200*y + x] == 'A':
            img.paste(dot, (x,y))

img.save("resultQR.jpg")
```
생성된 QR 코드를 인식해보니 플래그가 있었다.  
flag : `secarmy{L3t5_m4K3_QR_gr3AT_4ga1N}`

# Poor prisoner(550)
```
57,95
43,91
33,96
31,107

...

553,311
552,314
543,322
542,323
```
SDR 통신을 가로챈 데이터라고 한다. SDR이 중요한것 같아서 SDR만 겁나 파다가 아닌것 같아서 다시 데이터에 집중했다. 좌표값같이 생긴것 같아서 이미지로 변환해보니 플래그가 나왔다.  
> X,Y to image : https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php  

flag : `secarmy{coordinates-everytime}`  

# Prizes(101)
링크는 `Prizes` 탭 링크였다. 소스를 잘 뒤져보니 다음과 같은 주석이 있었다.
``` html
<!--One step closer to  prizes: c2VjYXJteXtzMHVyYzNfaTVfbjNjZXM1YXJ5fQo= -->
```
`base64` decode를 진행했다.  
flag : `secarmy{s0urc3_i5_n3ces5ary}`  

# web_salad(220)
링크 들어가면 로그인 페이지가 나온다. 한참을 SQLi를 날리다가 주석을 보니 아래와 같이 있었다.
```html
<!--username: ee11cbb19052e40b07aac0ca060c23ee-->
<!--password: bdc87b9c894da5168059e00ebffb9077-->
```
`md5` 디코딩을 해보면 `user`와 `password1234`가 나온다. 로그인해서 코드보면
```
<!--
c2VjYXJteXt3M2JfYnVjazN0XzNuYzB1bjdlcjNkfQo=
-->
```
`base64` 디코딩을 하면 플래그가 나온다.
> https://www.md5online.org/md5-decrypt.html  

flag : `secarmy{w3b_buck3t_3nc0un7er3d}`  

# Silly Mongolian 2.0(300)
사이트 들어가면 로그인 페이지 나온다. 이젠 기본적인 SQLi도 안나올거라는 걸 안다. 소스를 잘 살펴보면 flag의 조각들이 있다.
``` html
<!--Here's the first part of flag :  	
secarmy{why   
-->


/*Here's the second part of flag : 
  _1s_th1s_
  */


/*Here's the third part of flag : 
  m0ng0li@n_$uch
  */


/*Here's the fourth part of flag : 
_@_f00l}
*/
```
순서대로 로그인 페이지, index.js, process.js, style.css에 하나씩 있다.
flag : `secarmy{why_1s_th1s_m0ng0li@n_$uch_@_f00l}`

# Cookie Bank(300)
링크에 들어가서 문제 제목에 있듯이 쿠키를 확인했다.
```
Cookie1 : VGhpcyBhaW4ndCBpdCBjaGllZg==
Cookie2 : WW91IHNob3VsZCBwcm9iYWJseSBzdWJzdHJhY3QgOC0z
Cookie3 : SSBqdXN0IGdhdmUgeW91IGEgaGludCBhbHJlYWR5ISE=
Cookie4 : YXJlIHlvdSBzZXJpb3VzPz8/Pw==
Cookie5 : c2VjYXJteXt0aGVfJGh5X2MwMGtpZV93MXRoMW59
Cookie6 : Z2V0IGEgdGltZSBtYWNoaW5lIHlvdSBuMDBi
Cookie7 : SGV5IHlvdSdyZSBzdGlsbCBhbGl2ZT8=
Cookie8 : U2lyIGZpeCB5b3VyIEdQUw==
Cookie9 : U2lyIHlvdSBuZWVkIHRvIHJldGhpbmsgYWJvdXQgeW91ciBkZWNpc2lvbg==
Cookie10 : U3RhcnRpbmcgZnJvbSB0aGUgbGFzdCBpIHNlZS4uLg==
```
`base64` 디코딩을 하면 플래그가 나온다.  
flag : `secarmy{the_$hy_c00kie_w1th1n}`

# Stringy(100)
주어진 바이너리 열어보면 변수에 아래와 같이 값을 넣는다.
```c++
v5 = 'tJXYjV2c';
v6 = 'rBDMstXe';
v7 = 'oR3X3E2X';
v8 = 'xIHdz91M';
v9 = '9FSI1cmb';
```
리틀엔디안을 고려해서 차후에 문자 순서를 역전하기 위해 v9부터 이어서 적는다.
`9FSI1cmbxIHdz91MoR3X3E2XrBDMstXetJXYjV2c` 이것을 reverse 후 `From Base64`로 디코딩하면 플래그가 나온다.  
flag : `secarmy{l00k_a7_th3_str1ng5!!}` 

# Smash it!(100)
바이너리를 헥스레이로 열어보면 아래와 같다.
``` c++
int __cdecl main(int argc, const char **argv, const char **envp)
{

(...)

  v4 = argv;
  v47 = 0;
  v5 = 115;
  v6 = 101;
  v7 = 99;

(...)

  v40 = 102;
  v41 = 117;
  v42 = 110;
  v43 = 125;
  s1 = 1380013139;
  v46 = 84;
  while ( !v47 )
  {
    puts("hahaha, you are locked in the loop of eternity! ");
    printf("smash me:): ", v4);
    gets(&s2);
    if ( !strncmp((const char *)&s1, &s2, 5uLL) )
      v47 = 1;
  }
  if ( !strncmp((const char *)&s1, "START", 5uLL) )
  {
    puts("meh, you got out of it the usual way. Boring.");
  }
  else
  {
    for ( *(_DWORD *)((char *)&v46 + 1) = 0; *(_DWORD *)((char *)&v46 + 1) <= 38; ++*(_DWORD *)((char *)&v46 + 1) )
      putchar(*(&v5 + *(signed int *)((char *)&v46 + 1)));
    putchar(10);
  }
  return 0;
}
```
for문을 간략화 하면 아래와 같다.
``` c++
for (i=0;i<=38;++i) {
    putchar(&v5+i)
    putchar(10)
}
```
변수에 들어가는 값을 문자로 변환하면 된다.  
flag : `secarmy{sm@sh1ng_st@ck_1s_t00_much_fun}`

# F-L-A-S-H(300)
바이너리를 헥스레이해보면 아래와 같다.
``` c++
int __cdecl main(int argc, const char **argv, const char **envp)
{

(...)

  memset(&s, 0, 0x200uLL);
  s = 25971;
  v5 = 99;
  v6 = 97;
  v7 = 114;

(...)

  v25 = 31284;
  v26 = 121;
  v27 = 125;
  v30 = strlen((const char *)&s);
  puts(" _______      _         _______         _______                 ");
  puts("(  ____ \\    ( \\       (  ___  )       (  ____ \\       |\\     /|");
  puts("| (    \\/    | (       | (   ) |       | (    \\/       | )   ( |");
  puts("| (__  _____ | | _____ | (___) | _____ | (_____  _____ | (___) |");
  puts("|  __)(_____)| |(_____)|  ___  |(_____)(_____  )(_____)|  ___  |");
  puts("| (          | |       | (   ) |             ) |       | (   ) |");
  puts("| )          | (____/\\ | )   ( |       /\\____) |       | )   ( |");
  puts("|/           (_______/ |/     \\|       \\_______)       |/     \\|");
  puts("\n");

(...)

  if ( v29 == v28 )
  {
    puts("Are You Flash!? Here, take it...");
    for ( i = 0; i < v30; ++i )
      putchar(*((_BYTE *)&s + i));
    result = putchar(10);
  }
  else
  {
    result = puts("Haha, slow poke!!");
  }
  return result;
}
```
변수 s 부터 한글자씩 출력한다. 변수에 넣은 값을 한바이트씩 차례대로 뽑으면 플래그가 나온다.  
flag : `secarmy{7h1s_w45_345y_p34zy}`  

# Backyard COWs(500)
바이너리를 헥스레이로 보면 아래와 같다.
``` c++
int __cdecl main(int argc, const char **argv, const char **envp)
{

(...)

  v6 = 0LL;
  v7 = 0;
  v4 = 'b//:ptth';
  v5 = '0m/yl.ti';
  LODWORD(v6) = '0m_0';
  BYTE4(v6) = '0';
  puts(" ____________________________");
  puts("< moo! select your language! >");
  puts(" ----------------------------");
  puts("        \\   ^__^");
  puts("         \\  (oo)\\_______");
  puts("            (__)\\       )\\/\\");
  puts("                ||----w |");
  puts("                ||     ||");
  printf(
    "1. English\n2. My Native Language\n\nYour choice: ",
    argv,
    7074925467663627368LL,
    3489497484834534505LL,
    v6,
    *(_QWORD *)&v7);
  __isoc99_scanf("%d", &v9);
  if ( v9 == 1 )
  {
    puts("give me a number");
    __isoc99_scanf("%li", &v8);
    if ( v8 == 13337 )
    {
      puts("moo moo moo!!");
      for ( i = 0; i <= 20; ++i )
        putchar(*((_BYTE *)&v4 + i));
      putchar(10);
    }

(...)

  }

(...)

}
```
결론적으로 우리가 원하는 로직에서는 v4와 v5, v6을 출력한다. 그 값은 `http://bit.ly/m00_m0` 이다. 들어가면 텍스트 파일이 하나 나오는데 `cow programming language`로 되어있었다. cow 온라인 실행기로 실행하면 플래그가 나온다.  
> https://tio.run/#cow  

flag : `secarmy{d0_y0u_l1k3_c0w_languag3____?}`


# Its all in your head(100)
주어진 png 파일이 열리지 않는다. `hxd`로 확인해보니 시그니처 부분이 png 시그니처랑 비슷하면서도 달랐다. 다른 부분을 `png 시그니처`로 바꾸어주니 플래그가 있는 이미지가 열렸다.  
flag : `secarmy{h3ad3rs_t3ll_a_l0t}`

# secret(100)
pdf 파일이 주어지는데 텍스트 영역을 드래그해보면 보이는 텍스트보다 좀 더 드래그가 된다. 메모장에 붙여넣기 해보니 플래그가 보였다.
flag : `secarmy{ain’t_visible?}`

# The_Confusion(300)
압축파일을 풀면 4개의 이미지가 있다. `zsteg`를 이용하여 숨은 데이터를 찾아보면 아래와 같다.
``` bash
root@raspberrypi:~/ctf/tmp/theconfusion# zsteg flag1.png 
b1,rgb,lsb,xy       .. text: "     secarmy{h3r3_is_y0u4_fl@g}"
root@raspberrypi:~/ctf/tmp/theconfusion# zsteg flag1_Rebuilt.png 
b1,rgb,lsb,xy       .. text: "    frpnezl{JN3_V7_f"
root@raspberrypi:~/ctf/tmp/theconfusion# zsteg FILE2.png 
b1,rgb,lsb,xy       .. text: "     secarmy{01101100 01101111 01101100 01110100 01101000 01101001 01110011 01101001 01110011 01110100 01101000 01100101 01100110 01101100 01000000 01100111}  /*THIS IS YOUR FLAG*/"
root@raspberrypi:~/ctf/tmp/theconfusion# zsteg FLAG3.png 
b1,rgb,lsb,xy       .. text: "_04_?7Fb:?8N"
```
`zsteg flag1_Rebuilt.png`에 숨어있는 데이터는 카이사르 암호 key 13으로 해독하면 `secarmy{WA3_I7_s`이다. `zsteg FILE2.png`에 있던 데이터는 binary를 string으로 바꾸면 `secarmy{lolthisisthefl@g}`가 나온다.
`zsteg FLAG3.png`에 있던 데이터는 ROT47 로 DECODE해서 `0_c0nfu3ing}`을 얻을 수 있었다.  
flag : `secarmy{WA3_I7_s0_c0nfu3ing}`

# The_B1N(300)
똑같은 사진 두장이 주어졌다. 하나는 png, 하나는 jpg 파일이다. png 먼저 `zsteg`로 보니 데이터가 숨어있었고, base64 디코딩을 하니 url이 두개가 이어져서 나왔다. 앞의 url은 잘 동작했지만 진짜 플래그가 아니었고, 뒤 url은 뒷부분이 없는듯 하다. Online Steganography Tool로 해독하니 뒷부분까지 완전하게 나왔다.  
> https://stylesuxx.github.io/steganography/  

flag : `secarmy{PAST3_B1N_H@S_S0LUT10N}`

# Save Them(300)
압축파일이 주어져서 풀어보니 고양이 사진이 있었고, `binwalk`로 보니 압축파일이 있었다. `-e` 옵션으로 카빙해서 보니 pastebin 사이트 주소를 두개 알려준다.
``` bash
root@raspberrypi:~/tmp# binwalk -e cute_cats.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
504           0x1F8           Copyright string: "Copyright 2000 Adobe Systems Incorporated"
29168         0x71F0          Zip archive data, at least v2.0 to extract, name: flag1/
29236         0x7234          Zip archive data, at least v2.0 to extract, uncompressed size: 83, name: flag1/flags
29391         0x72CF          Zip archive data, at least v2.0 to extract, uncompressed size: 55852, name: flag1/.sauce
30879         0x789F          End of Zip archive

root@raspberrypi:~/tmp# cd _cute_cats.jpg.extracted/flag1/
root@raspberrypi:~/tmp/_cute_cats.jpg.extracted/flag1# ls
flags
root@raspberrypi:~/tmp/_cute_cats.jpg.extracted/flag1# cat flags 
 Here is your flag :- https://pastebin.com/4ffrJKEChttps://pastebin.com/mN89JJE2
```
들어가보면 각각 아래와 같은 데이터가 있었다.
```
secarmy{i3_th1s_th3_fl@g}
secarmy{y3s_this_1s_r1ght}
```
페이크다. 디렉토리를 자세히 보면 `.sauce`가 숨어있다.
```bash
root@raspberrypi:~/tmp/_cute_cats.jpg.extracted/flag1# ll
total 68
drwxr-xr-x 2 root root  4096 Aug  8 09:49 .
drwxr-xr-x 3 root root  4096 Aug 20 18:28 ..
-rw-r--r-- 1 root root    83 Aug  8 09:44 flags
-rwx--x--x 1 root root 55852 Aug  8 09:49 .sauce
root@raspberrypi:~/tmp/_cute_cats.jpg.extracted/flag1# cat .sauce 
There are 3 flags , Best Of Luck :-[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])

(...)

(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])()
```
열어보면 `jsfuck` 코드가 있다. 복호화 하면
> jsfuck decode : https://enkhee-osiris.github.io/Decoder-JSFuck/   

flag : `secarmy{c0ng4atulat10ns_y0u_h@v3_th3_fl@g}`

# Thanks(50)
대회가 거의 끝날즈음 나온 마지막 문제다. `base64` 디코딩하면 플래그가 나온다.
flag : `secarmy{you_guys_are_awesome}`

# 16+8(50)
2개의 첨부파일을 열어보면 하나는 16진수 하나는 8진수다. 각각 문자로 나타내보니 플래그가 나왔다.  
flag : `secarmy{Num3er_sys73m}`

# Die Basis(50)
압축파일 안에 텍스트 파일이 두개 들어있는데 각각 `base64`와 `base32`로 디코딩해서 이으면 플래그가 나온다.  
flag : `secarmy{fl@g_1s_th3_b@s3}`

# Easy Capture(50)
2진수가 들어있는 텍스트 파일이 주어진다. 문자로 변환하면 플래그가 나온다.  
flag : `secarmy{h3r3_y0u_c@ptur3}`

# IMAGE(50)
zsteg를 이용해 풀었다.
flag : `secarmy{th3_im@ge_s4ys_i7_a11}`

# Th3_G1F7(50)
zsteg를 이용해 풀었다.
flag : `secarmy{h3re_1s_th3_g1ft}`

# Welcome All(10)
그냥 플래그 주는 문제다.  
flag : `secarmy{w3lc0me_y0u_all}`

# Netcat(20)
nc 접속하면 플래그를 바로 준다.
``` bash
root@raspberrypi:~/tmp# nc 68.183.44.136 2200
Welcome To SecArmyCTF!!
Here, Take your flag:
secarmy{W3lc0m3_T0_S3c4RmyC7F0x02}
```
flag : `secarmy{W3lc0m3_T0_S3c4RmyC7F0x02}`

# InstaFamous(20)
인스타 첫번째 게시물에 플래그가 있다. 인스타 홍보용.
flag : `secarmy{w3lc0me_1n$t@_f@m1ly}`