# Memory Forensic - 3 - Play Time

## 문제
Rick just loves to play some good old videogames. can you tell which game is he playing? whats the IP address of the server?  
릭이 오래된 비디오 게임을 좋아한다고 한다. 어떤 게임이고, 서버의 IP 주소를 알아오라고 한다.

## 접근1
문제를 통해 해당 비디오 게임은 서버와 통신이 필요한 게임인것을 알 수 있다. netscan 플러그인을 통해 통신중인 내용을 확인해보았지만 너무 많아서 분별하기 어려웠다. 윈도우의 findstr 명령으로 확실히 아닌 통신을 하나씩 검색하며 지워나가니 아래와 같은 결과가 나왔다.
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 netscan | findstr /V "System lsass WebCompanion orrent svchost chrome wininit services"
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x7d6124d0         TCPv4    192.168.202.131:49530          77.102.199.102:7575  CLOSED           708      LunarMS.exe
0x7d72cbe0         TCPv4    192.168.202.131:50340          23.37.43.27:80       CLOSED           3496     Lavasoft.WCAss
0x7d8fd530         TCPv4    192.168.202.131:50327          23.37.43.27:80       CLOSED           3496     Lavasoft.WCAss
0x7dc4bcf0         TCPv4    -:0                            104.240.179.26:0     CLOSED           3        ?4????
0x7e1f7ab0         TCPv4    -:0                            56.187.190.26:0      CLOSED           3        ?4????
0x7e413a40         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe
0x7e521b50         TCPv4    -:0                            -:0                  CLOSED           708      LunarMS.exe
```

## 해결
위의 결과로 미루어 보았을 때, `LunarMS` 가 가장 가능성이 커보였다. 처음엔 MS가 마이크로소프트인줄알고 절대 아니라고 생각했는데 성급한 추측이었던것 같다. 또한, 해당 통신 서버가 `77.102.199.102`의 7575서버임을 알 수 있었다.


