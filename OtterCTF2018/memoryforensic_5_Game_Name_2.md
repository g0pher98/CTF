# Memory Forensic - 5 - Game Name 2

## 문제
From a little research we found that the username of the logged on character is always after this signature: 0x64 0x??{6-8} 0x40 0x06 0x??{18} 0x5a 0x0c 0x00{2} What's rick's character's name?  
로그인한 유저명은 어떠한 시그니처 뒤에 존재한다는 것을 발견했다고 한다. 해당 시그니처가 `0x64 0x??{6-8} 0x40 0x06 0x??{18} 0x5a 0x0c 0x00{2}` 이 부분인 것 같다. 이때 릭의 캐릭터 이름이 플래그가 된다.

## 접근1
