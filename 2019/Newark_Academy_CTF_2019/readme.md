# NACTF (Newark Academy's Computer Science Club)
with team `༼ つ ◕_◕ ༽つ 뀨` (43/1335)  

## Forensics
[Least Significant Avenger](#Least-Significant-Avenger)  
[The MetaMeme](#The-MetaMeme)  
[My Ears Hurt](#My-Ears-Hurt)  
[Unzip Me](#Unzip-Me)  
[Kellen's Broken File](#Kellen's-Broken-File)  
[Kellen's PDF sandwich](#Kellen's-PDF-sandwich)  
[Filesystem Image](#Filesystem-Image)  
[Phuzzy Photo](#Phuzzy-Photo)  
[File recovery](#File-recovery)  

## Web Exploitation
[Pink Panther](#pink-panther)  
[Scooby Doo](#Scooby-Doo)  
[Dexter's Lab](#dexter-s-lab)  
[Sesame Street](#sesame-street)  


# Least Significant Avenger
```
I hate to say it but I think that Hawkeye is probably the Least Significant avenger. Can you find the flag hidden in this picture?

Hiding messages in pictures is called stenography. I wonder what the least significant type of stenography is.
```
## solve
``` bash
➜ strings insignificant_hawkeye.png | grep "nactf"
➜ binwalk insignificant_hawkeye.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 332 x 152, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed

➜ zsteg insignificant_hawkeye.png
/usr/lib/ruby/2.5.0/open3.rb:199: warning: Insecure world writable dir /mnt/c in PATH, mode 040777
imagedata           .. file: MIPSEL-BE MIPS-III ECOFF executable not stripped - version 0.1
b1,rgb,lsb,xy       .. text: "nactf{h4wk3y3_15_th3_l34st_51gn1f1c4nt_b1t}"
b3,g,lsb,xy         .. text: "L4Xe\"Bm\""
b4,r,msb,xy         .. text: "0s%S@%3dBbQSa"
b4,g,lsb,xy         .. text: "8vURSDS\"#"
b4,g,msb,xy         .. text: "NPcDa0P '"
b4,b,msb,xy         .. text: "veq1q#AR"
b4,rgb,msb,xy       .. text: "\"qVBvtAqF"
b4,bgr,msb,xy       .. text: "sFUcS1sDQ2Q!qgs&c1E"
b4,rgba,lsb,xy      .. text: ";oHO8_vOg_"
b4,abgr,msb,xy      .. text: "/^O4Op?5"
```
## flag
`nactf{h4wk3y3_15_th3_l34st_51gn1f1c4nt_b1t}`


# The MetaMeme
```
Phil sent me this meme and its a little but suspicious. The meme is super meta and it may be even more meta than you think.

Wouldn't it be really cool if it also had a flag hidden somewhere in it? Well you are in luck because it certainly does!
```
## solve
``` bash
➜ strings metametametameta.pdf | grep "nactf"
/Subject (nactf{d4mn_th15_1s_s0_m3t4})
```
## flag
`nactf{d4mn_th15_1s_s0_m3t4}`


# My Ears Hurt
```
The20thDuck sent me this really annoying audio file. It's way too high pitched to be his voice. What he is trying to tell me? Maybe its a code; he is the crypto master after all.

You may have to convert file types.

You will need to insert the string into the nactf{...} form before submitting.
```
## solve
음원파일이 주어진다. 바로 `audacity`를 열어보면 모스무호의 직감이 온다. 그대로 옮겨보면 `-.. .---- -.. ..- -.. ----- - .... .---- ..... -... -.-- .... ....- -. -..`
## flag
`nactf{D1DUD0TH15BYH4ND}`


# Unzip Me
```
I stole these files off of The20thDucks' computer, but it seems he was smart enough to put a password on them. Can you unzip them for me?

All the passwords are real words and all lowercase
```
## solve
모든 패스워드는 lowercase로 이루어진 실제 단어라고 한다. 브루트포스하라는 얘기. `fcrackzip`으로 딕셔너리 기반 브루트포스를 진행했다.
``` bash
 ~/ctf/nactf/unzip  fcrackzip -u -D -p google-10000-english/20k.txt zip1.zip

PASSWORD FOUND!!!!: pw == dictionary
 ~/ctf/nactf/unzip  fcrackzip -u -D -p google-10000-english/20k.txt zip2.zip
PASSWORD FOUND!!!!: pw == rock
 ~/ctf/nactf/unzip  fcrackzip -u -D -p google-10000-english/20k.txt zip3.zip


PASSWORD FOUND!!!!: pw == dog
```
위 패스워드로 압축을 풀어서 나온 문서의 내용을 이어보면 플래그가 나온다.
## flag
`nactf{w0w_y0u_unz1pp3d_m3}`

# Kellen's Broken File
```
Kellen gave in to the temptation and started playing World of Tanks again. He turned the graphics up so high that something broke on his computer!

Kellen is going to lose his HEAD if he can't open this file. Please help him fix this broken file.
```
## solve
``` bash
➜ file Kellens_broken_file.pdf
Kellens_broken_file.pdf: data
➜ binwalk Kellens_broken_file.pdf

DECIMAL       HEXADECIMAL     DESCRIPTION
---------------------------------------------------------------

➜ xxd Kellens_broken_file.pdf | head -3
0000: 312e 330a 25c4 e5f2 e5eb a7f3 a0d0 c4c6  1.3.%...........
0010: 0a34 2030 206f 626a 0a3c 3c20 2f4c 656e  .4 0 obj.<< /Len
0020: 6774 6820 3520 3020 5220 2f46 696c 7465  gth 5 0 R /Filte
```
pdf 파일인데 pdf 시그니처가 없다. pdf 시그니처인 `%PDF-`를 추가해주었다.
``` bash
➜ echo "%PDF-" > result.pdf
➜ cat Kellens_broken_file.pdf >> result.pdf
```
## flag
`nactf{kn0w_y0ur_f1l3_h34d3rsjeklwf}`

# Filesystem Image
```
Put the path to flag.txt together to get the flag! for example, if it was located at ab/cd/ef/gh/ij/flag.txt, your flag would be nactf{abcdefghij}
```
## analysis
압축을 풀면 iso 이미지 파일이 있다.
``` bash
➜ file img.iso 
img.iso: DOS/MBR boot sector; partition 1 : ID=0xc, start-CHS (0x0,0,2), end-CHS (0x0,130,2), startsector 1, 8191 sectors
```
디스크 파일이라 바로 마운트가 안되고, 마운트할 파티션의 위치를 찾아주어야 하는데, 위 파일에서 첫번째 파티션은 1섹터에서 시작이다. 오프셋을 인자로 줘서 mount 시키면 된다.

## solve
``` bash
➜ sudo mount -o loop,offset=512 img.iso /mnt/loop0
➜ cd /mnt/loop0/
➜ find ./ | grep flag
./lq/wk/zo/py/hu/flag.txt
```
## flag
`nactf{lqwkzopyhu}`

# Phuzzy Photo
```
Joyce's friend just sent her this photo, but it's really fuzzy. She has no idea what the message says but she thinks she can make out some black text in the middle. She gave the photo to Oligar, but even his super eyes couldn't read the text. Maybe you can write some code to find the message?

Also, you might have to look at your screen from an angle to see the blurry hidden text

P.S. Joyce's friend said that part of the message is hidden in every 6th pixel
```
## can't solve
겁나 삽질했는데 도저히 모르겠음...근데 많은 사람이 푼걸로 보아 나만 모르는듯,,

# File recovery
```
Uh oh! Lillian has accidentally deleted everything on her flash drive! Here's an image of the drive; find the PNG and get the flag.
```
## solve
플래시 드라이브에서 이미지를 삭제했다고 한다. 디스크에 png 데이터가 있을 것이므로 `winhex`를 이용해서 카빙(Tools - Disk Tools - File Recovery by Type..)했다.
## flag 
`nactf{f1l3_r3c0v3ry_15_c0ol}`

# Pink Panther
```
Rahul loves the Pink Panther. He even made this website:

http://pinkpanther.web.2019.nactf.com

I think he hid a message somewhere on the webpage, but I don't know where... can you INSPECT and find the message?

https://www.youtube.com/watch?v=2HMSnfeNf8c
```
## solve
홈페이지 들어가서 코드를 보면 주석으로 플래그가 있다.
## flag
`nactf{1nsp3ct_b3tter_7han_c10us3au}`

# Scooby Doo
```
Kira loves to watch Scooby Doo so much that she made a website about it! She also added a clicker game which looks impossible. Can you use your inspector skills from Pink Panther to reveal the flag?

http://scoobydoo.web.2019.nactf.com
```
## solve
`GAME`탭에 들어가면 1,000,000,000번 클릭하면 flag를 준다고 한다. javascript 코드에서 `clickCount ++;` 이 부분을 `clickCount += 1000000000;`로 바꿔줘서 한번 클릭으로 성공할 수 있도록 수정한다. 이후 `Click Me!` 버튼을 오지게 따라다니면서 한번 클릭을 성공한다. 는 아니고 콘솔에서 `document.getElementsByTagName("button")[0].click()`로 클릭한다.

## flag
`nactf{ult1m4T3_sh4ggY}`

# Dexter's Lab
```
Dee Dee,

Please check in on your brother's lab at dexterslab.web.2019.nactf.com We know his username is Dexter, but we don't know his password! Maybe you can use a SQL injection?

Mom + Dad
```
## solve
홈페이지 들어가면 로그인 창밖에 없다. 아이디에 SQLinjection을 넣어서 로그인을 우회한다.

## payload
`'||1#`

## flag
`nactf{1nj3c7ion5_ar3_saf3_in_th3_l4b}`


# Sesame Street
```
Surprisingly, The20thDuck loves cookies! He also has no idea how to use php. He accidentally messed up a cookie so it's only available on the countdown page... Also why use cookies in the first place?

sesamestreet.web.2019.nactf.com
```
## solve
홈페이지에 `I love cookies!`라는 문구로 보아 쿠키를 변조하는 문제인것 같다. `Countdown`탭에 들어가면 ctf가 끝나야 flag를 보여주는것 같다. 예상했던대로 쿠키에 `session-time`이라는 쿠키에 현재시간 데이터가 있었고, 이를 변조해서 현재시간을 속일 수 있었다.

## flag
`nactf{c000000000ki3s}`










