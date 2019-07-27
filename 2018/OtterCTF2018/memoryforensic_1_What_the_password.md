# Memory Forensic - 1 - What the password?

## 문제
you got a sample of rick's PC's memory. can you get his user password?  
릭이라는 사람의 메모리를 받을 수 있었다. 문제는 패스워드를 알아보라고 한다.

## 접근1
우선 메모리 분석을 위해 어떤 서비스팩을 이용하는 PC인지 아래 명령을 통해 알 수 있었다.
### Command
```
volatility.exe -f rick.vmem imageinfo
```
`Win7SP1x64`를 이용함을 알 수 있었고, 이를 통해 여러 플러그인을 사용할 수 있었다.

## 접근2 (삽질)
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 hivelist
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a00377d2d0 0x00000000624162d0 \??\C:\System Volume Information\Syscache.hve
0xfffff8a00000f010 0x000000002d4c1010 [no name]
0xfffff8a000024010 0x000000002d50c010 \REGISTRY\MACHINE\SYSTEM
...
0xfffff8a0016d4010 0x00000000214e1010 \SystemRoot\System32\Config\SAM
...
```
SYSTEM과 SAM의 가상 주소를 통해 hashdump 플러그인으로 추출할 수 있었다.
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 hashdump -y 0xfffff8a000024010 -s 0xfffff8a0016d4010
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Rick:1000:aad3b435b51404eeaad3b435b51404ee:518172d012f97d3a8fcc089615283940:::
```
나름 잘 접근했다고 생각했지만 원본 텍스트를 얻어낼 수 없었다.

## 접근3
알아보니 패스워드를 알아낼 수 있는 플러그인이 따로 존재했다.
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 lsadump
```
### Result
```
Volatility Foundation Volatility Framework 2.6
DefaultPassword
0x00000000  28 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   (...............
0x00000010  4d 00 6f 00 72 00 74 00 79 00 49 00 73 00 52 00   M.o.r.t.y.I.s.R.
0x00000020  65 00 61 00 6c 00 6c 00 79 00 41 00 6e 00 4f 00   e.a.l.l.y.A.n.O.
0x00000030  74 00 74 00 65 00 72 00 00 00 00 00 00 00 00 00   t.t.e.r.........

DPAPI_SYSTEM
0x00000000  2c 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ,...............
0x00000010  01 00 00 00 36 9b ba a9 55 e1 92 82 09 e0 63 4c   ....6...U.....cL
0x00000020  20 74 63 14 9e d8 a0 4b 45 87 5a e4 bc f2 77 a5   .tc....KE.Z...w.
0x00000030  25 3f 47 12 0b e5 4d a5 c8 35 cf dc 00 00 00 00   %?G...M..5......
```

## 해결
lsadump라는 플러그인의 결과를 보면 Default Password에 문자열이 보인다. 적절히 유추해보면 `MortyIsReallyAnOtter`가 패스워드임을 알 수 있다.
