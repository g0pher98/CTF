# Memory Forensic - 5 - Game Name 2

## 문제
From a little research we found that the username of the logged on character is always after this signature: 0x64 0x??{6-8} 0x40 0x06 0x??{18} 0x5a 0x0c 0x00{2} What's rick's character's name?  
로그인한 유저명은 어떠한 시그니처 뒤에 존재한다는 것을 발견했다고 한다. 해당 시그니처가 `0x64 0x??{6-8} 0x40 0x06 0x??{18} 0x5a 0x0c 0x00{2}` 이 부분인 것 같다. 이때 릭의 캐릭터 이름이 플래그가 된다.

## 접근1
해당 시그니처를 yarascan 플러그인을 통해 LunarMS 프로세스에서 추출해보았다.(PID는 708. 4번문제 참고)
### Command
```
volatility.exe -f OtterCTF.vmem --profile=Win7SP1x64 yarascan -Y "/\x64(.{6,8})\x40\x06(.{18})\x5a\x0c\x00\x00/i" -p 708
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Rule: r1
Owner: Process LunarMS.exe Pid 708
0x5ab4dfa8  44 64 00 00 00 00 00 00 40 06 00 00 b4 e5 af 00   Dd......@.......
0x5ab4dfb8  01 00 00 00 00 00 00 00 b0 e5 af 00 5a 0c 00 00   ............Z...
0x5ab4dfc8  4d 30 72 74 79 4c 30 4c 00 00 00 00 00 00 00 21   M0rtyL0L.......!
0x5ab4dfd8  4e 00 00 55 75 00 00 00 00 00 00 00 00 00 00 00   N..Uu...........
0x5ab4dfe8  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 b4   ................
0x5ab4dff8  10 95 6f d5 cd 66 36 66 36 b4 ab ee fa a4 73 9f   ..o..f6f6.....s.
0x5ab4e008  70 f2 ab 6e ba 3a c4 3f c4 3c ac ee 25 ac d9 a8   p..n.:.?.<..%...
0x5ab4e018  d9 60 ac 6e a0 d6 25 d2 25 a8 ab ee ee e1 aa d2   .`.n..%.%.......
0x5ab4e028  a2 29 ac 2e 9b d1 5e f4 57 d8 ab 2e 27 86 01 7c   .)....^.W...'..|
0x5ab4e038  07 87 ab ee 0a e8 5f 12 59 d7 ab 6e 31 96 49 96   ......_.Y..n1.I.
0x5ab4e048  49 cb ab ee 9e dd e6 dd e6 6a ac 2e 2c 12 bd 3e   I........j..,..>
0x5ab4e058  25 1f 03 6d 29 87 9d 69 26 f8 4a f8 4a cb ab 6e   %..m)..i&.J.J..n
0x5ab4e068  ad 60 35 ef a2 01 c2 38 65 2c d8 fa cd e4 f8 90   .`5....8e,......
0x5ab4e078  31 c7 87 8c 21 0e 70 e6 6d 78 20 af 00 00 00 00   1...!.p.mx......
0x5ab4e088  00 00 00 00 00 00 00 00 00 00 00 00 00 5e 81 ee   .............^..
0x5ab4e098  8f 7c 6a 4e 74 06 86 f8 0d 06 00 00 00 00 00 00   .|jNt...........
```

## 해결
위의 덤프에서 볼 수 있듯이 `M0rtyL0L`이 캐릭터명으로 추정된다.