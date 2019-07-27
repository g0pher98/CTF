# Memory Forensic - 4 - Game Name

## 문제
We know that the account was logged in to a channel called Lunar-3. what is the account name?  
계정이 Lunar-3이라는 채널에 로그인 되어있다고 한다. 계정 이름이 플래그인 문제다.

## 접근1
해당 채널에 어떻게 접근해야하는지는 모르겠지만 혹시 프로세스가 사용한 메모리 영역에 남아있지 않을까 생각되어 프로세스 덤프를 떠보았다.
### CMD
```
g0pher> volatility.exe -f OtterCTF.vmem --profile=Win7SP1x64 pslist | findstr Lunar
Volatility Foundation Volatility Framework 2.6
0xfffffa801b5cb740 LunarMS.exe             708   2728     18      346      1      1 2018-08-04 19:27:39 UTC+0000

g0pher> volatility.exe -f OtterCTF.vmem --profile=Win7SP1x64 procdump -p 708 -D ./
Volatility Foundation Volatility Framework 2.6
Process(V)         ImageBase          Name                 Result
------------------ ------------------ -------------------- ------
0xfffffa801b5cb740 0x0000000000400000 LunarMS.exe          OK: executable.708.exe
```

## 접근2
덤프파일을 어떻게 분석할까 고민하다가 칼리에서 분석하는것이 좋을것 같아서 칼리로 옮겨서 분석했다. strings 툴을 사용하여 바이너리에서 문자열들을 추출하고, grep으로 luna-3 문자열 +-1 행을 출력했다.
### CMD
```
g0pher# strings 708.dmp  | grep -C 1 -i lunar-3
b+YLc+Y
Lunar-3
Lunar-4
--
keyFocused
Lunar-3
0tt3r8r33z3
```

## 해결
위의 결과로 미루어 보았을 때, Lunar-3의 계정명은 `0tt3r8r33z3`라고 추측해볼 수 있다.
