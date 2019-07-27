# Misc - ReCurse

## 문제
Found this nested zip in Morty's PC. what is it that he is hiding?  
이 어지럽혀진 압축파일에 무엇이 숨겨져있는지 찾아보자.

## 접근1
압축파일을 풀면 끊임없이 한글자의 파일명을 가진 압축파일이 또 나온다. 여러번 반복해서 문자를 이어보면 어떤 메시지가 나올것이라고 생각해서 직접 압축을 풀다가 중도 포기했다.

## 접근2
그래서 코딩을 해보기로 했다.
### Code
``` python
import os
import zipfile

def unpack(name):
	tmp = zipfile.ZipFile(name)
	tmp.extractall("./a/")
	tmp.close()

def do():
	while True:
		f = "./a/"+list(os.walk("./a/"))[0][2][0]
		print(f[4],end='')
		os.rename(f, "./a/g0pher.zip")
		unpack("./a/g0pher.zip")
		os.remove("./a/g0pher.zip")
    
do()
```
프로그램을 돌려보니 다음과 같은 메시지와 압축이 걸린 파일이 하나 나왔다.
```
aHR0cHM6Ly93d3cuZXhvdGljYW5pbWFsc2ZvcnNhbGUubmV0L3NhbGUvMzkzNTMtMi1mZW1hbGUtc21hbGwtY2xhdy1Bc2lhbi1vdHRlcnMuYXNw
```

## 접근3
Base64라고 생각하여 디코딩 해보니 해당 데이터는 `https://www.exoticanimalsforsale.net/sale/39353-2-female-small-claw-Asian-otters.asp` 이었음을 알 수 있다. 홈페이지에 들어가서 이것저것 찾아보고 압축 비밀번호에 넣어보았지만 잘 되지 않아서 대회 기간 내에 풀지 못했다.

## 해결
홈페이지에 있던 `Brking1991@gmail.com`이 패스워드라고 한다. `Brking1991`만 시도해보고 전체 이메일을 시도해보지 않아서 너무 아쉬웠다... 압축 파일 속에 텍스트 파일을 열어보면 `flag{Recursion_1S_T3rribl3_AnD_1_H4t3_My_L1F3!!}` 라는 문자열이 있다.