# Memory Forensic - 6 - Silly Rick

## 문제
Silly rick always forgets his email's password, so he uses a Stored Password Services online to store his password. He always copy and paste the password so he will not get it wrong. whats rick's email password?  
릭이 비밀번호를 자주 까먹어서 온라인으로 암호 저장 서비스를 이용한다고 한다. 그는 암호를 복사하기 때문에 절대 잘못 넣지 않는다는 힌트를 주었다. 이때 이메일의 패스워드를 구하는 것이 목표인것 같다.


## 접근1
우선 릭은 패스워드를 복사하는 버릇이 있으므로 clipboard 플러그인을 사용해서 클립보드에 남아있는 데이터가 있는지 확인해 보았다.
### Command
```
volatility.exe -f OtterCTF.vmem --profile=Win7SP1x64 clipboard
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Session    WindowStation Format                         Handle Object             Data
---------- ------------- ------------------ ------------------ ------------------ -------------------
         1 WinSta0       CF_UNICODETEXT                0x602e3 0xfffff900c1ad93f0 M@il_Pr0vid0rs
         1 WinSta0       CF_TEXT                          0x10 ------------------
         1 WinSta0       0x150133L              0x200000000000 ------------------
         1 WinSta0       CF_TEXT                           0x1 ------------------
         1 ------------- ------------------           0x150133 0xfffff900c1c1adc0
```

## 해결
위의 결과를 보면 비밀번호같이 생긴 클립보드 데이터를 볼 수 있다. `M@il_Pr0vid0rs`를 비밀번호로 추정해볼 수 있다.