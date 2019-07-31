# Memory Forensic - General Info

## 문제
Let's start easy - whats the PC's name and IP address?  
PC의 이름과 IP주소를 찾아오라고 한다.

## 접근1
PC의 이름부터 찾아보기로 했다. 레지스터에는 많은 정보가 담겨져있으므로 검색해보니 PC명은 `HKLM\SYSTEM\CurrentConsolSet\Services\Tcpip\Parameters`에서 확인할 수 있다고 한다. 이 레지스트리를 찾아가보자.
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 printkey -K ControlSet001\services\Tcpip\Parameters
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \REGISTRY\MACHINE\SYSTEM
Key name: Parameters (S)
Last updated: 2018-08-04 19:34:22 UTC+0000

Subkeys:
  (S) Adapters
  (S) DNSRegisteredAdapters
  (S) Interfaces
  (S) PersistentRoutes
  (S) Winsock

Values:
REG_SZ        ICSDomain       : (S) mshome.net
REG_DWORD     SyncDomainWithMembership : (S) 1
REG_SZ        NV Hostname     : (S) WIN-LO6FAF3DTFE
REG_EXPAND_SZ DataBasePath    : (S) %SystemRoot%\System32\drivers\etc
REG_SZ        NameServer      : (S)
REG_DWORD     ForwardBroadcasts : (S) 0
REG_DWORD     IPEnableRouter  : (S) 0
REG_SZ        Domain          : (S)
REG_SZ        Hostname        : (S) WIN-LO6FAF3DTFE
REG_SZ        SearchList      : (S)
REG_DWORD     UseDomainNameDevolution : (S) 1
REG_DWORD     EnableICMPRedirect : (S) 1
REG_DWORD     DeadGWDetectDefault : (S) 1
REG_DWORD     DontAddDefaultGatewayDefault : (S) 0
REG_DWORD     EnableWsd       : (S) 1
REG_DWORD     QualifyingDestinationThreshold : (S) 3
```
결과에서 볼 수 있듯이 PC의 이름은 `WIN-LO6FAF3DTFE`임을 알 수 있다.

## 접근2
IP 주소는 netscan 플러그인을 통해 알 수 있을것이라 판단되어 시도해보았다.
### Command
```
volatility.exe -f rick.vmem --profile=Win7SP1x64 netscan
```
### Result
```
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x7d60f010         UDPv4    0.0.0.0:1900                   *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:17 UTC+0000
0x7d62b3f0         UDPv4    192.168.202.131:6771           *:*                                   2836     BitTorrent.exe 2018-08-04 19:27:22 UTC+0000
...
```

## 해결
위의 결과를 통해 PC 이름은 `WIN-LO6FAF3DTFE`이고, IP주소는 `192.168.202.131`임을 알 수 있다.
