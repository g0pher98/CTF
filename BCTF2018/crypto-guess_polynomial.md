# Crypto - Guess_polynomial

## 문제
파이썬 파일을 하나 던져주고 해당 파이썬으로 nc 서버를 열어주었다. nc에 접속해보면 숫자를 입력하라고 한다. 그러면 엄청 큰 데이터를 보내준다. 이제 내부 데이터를 맞추라고 한다... ang? 코드를 분석해봐야 할 것같다.

## 접근1
코드를 살펴보니 coeff라는 길이가 랜덤하고 값도 랜덤한 리스트를 생성한다. 핵심적인 코드는 다음과 같다.
``` python
def calc(coeff, x):
    num = coeff[0]
    for i in range(1, len(coeff)): # n번 반복
        num = num * x + coeff[i] # num * 입력값 + coeff값
    return num
```
내가 입력한 값을 곱하고 coeff의 요소를 하나 더하고를 반복하는 로직이다. 최종적으로 구해진 결과값을 출력해준다. 즉, 반대로 역연산을 해서 coeff 리스트의 각 요소를 구해야한다.

## 접근2
위의 로직을 특이하게 만드는 입력값이 몇가지 있다. 하나는 0이다. 결과값은 coeff의 마지막 인덱스의 값을 출력하게 만든다. 다른 하나는 1이다. 순수한 coeff의 합을 출력하게 만든다. 마지막은 내가 이 문제를 풀게된 방법인데 coeff보다 훨씬 큰 10의 제곱수를 입력하는 것이다. 그렇게 되면 가시적으로 coeff의 값을 확인할 수 있다. 정확한 리스트의 값을 구하기 위해 코딩을 했다.

## 해결
``` python
import socket

def crack(data):
    data = data[data.index('m:')+2:data.index('It')-1]
    lst = []
    while True:
        num = int(data[-70:])
        data = data[:-70]
        lst.append(str(num))
        if len(data) < 10:
            break

    lst.reverse()
    return ' '.join(lst)+'\n'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('39.96.8.114', 9999)
sock.connect(server)


for i in range(10):
    if i > 1:
        print "clear!",
    print "\n[*] Round %d start ..."%i,
    recv = sock.recv(10000)
    # 길이 70
    send = '10000000000000000000000000000000000000000000000000000000000000000000000\n'
    sock.send(send)
    recv = ''
    while True:
        recv += sock.recv(100000)
        if "It" in recv:
            break

    send = crack(recv)
    sock.send(send)

# 플래그 출력
recv = sock.recv(10000)
print("\n\n"+recv)

sock.close()
```