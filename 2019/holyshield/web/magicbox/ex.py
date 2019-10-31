from z3 import *

num = [BitVec('a%d'%i, 32) for i in range(0,26)]
andres = [513, 512, 512, 8, 28, 540, 28, 12, 520, 544, 512, 516]
a = Int('a')
t = Int('t')
s = Solver()
'''
for i in range(0, len(num)-2, 2):
	u = num[i + 1] - 56320
	a += u
	i.append(u)
	if u < 0:
		u = n[l]
		'''

s.add(55306 <= num[0])
s.add(55383 > num[0])

for i in range(0, len(num)-2, 2):
	s.add(num[i] & num[i+1] == andres[i//2])

s.add(num[0] + num[2] + num[4] + num[6] + num[8] + num[10] + num[12] + num[14] + num[16] + num[18] + num[20] + num[22] + num[24] - 56320*13 == 6998)

for i in num[1:]:
	s.add(i < 56320)

	
print(s.check())
print(s.model())