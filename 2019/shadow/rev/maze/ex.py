# -*- coding: utf8 -*-
from pwn import *

context.log_level="debug"

INF = 10000000000


x = process("./maze")

array = []
costs = []

s_x, s_y = 0,0
d_x, d_y = 0,0

#### Tools ####
def between(a, b, c):
	if a <= b and b < c:
		return True
	return False

#### Logic ####

class Vertex:
	def __init__(self, cost):
		self.visited = False
		self.cost = cost
		self.weight = INF

	def getWeight(self):
		return self.weight
	def updateWeight(self, new):
		self.weight = new
	def visit(self):
		self.visited = True
	def isVisited(self):
		return self.visited
	def getCost(self):
		return self.cost

def getNearXY(loc, limit):
	"""
	Get Near Vertex's XY location
	return(list) : [ (x, y), (x1, y1), ... ]
	"""
	x, y = loc
	lst = []
	for xy in [ (x-1, y), (x, y-1), (x+1, y), (x, y+1) ]:
		if between(0, xy[0], limit) and between(0, xy[1], limit):
			lst.append(xy)
	return lst
   

def getMinistWeightXY(l):
	"""
	Get Minimalist Cost Vertex's index that didn't visited
	return(tuple) : (x, y)
	"""
	mini = INF
	a, b = INF, INF

	for x in range(l):
		for y in range(l):
			#print(len(array[0]))
			#print(array[x][y].getWeight())
			if (not array[x][y].isVisited()) and array[x][y].getWeight() < mini:
				mini = array[x][y].getWeight()
				a, b = x, y      
	return a, b


def init(l):
	"""
	Init cost list and array list
	return(none)
	"""
	global cost
	global array
	global s_x, s_y
	global d_x, d_y
	cost, array = [], []
	cost = [[INF for e in range(l)] for _ in range(l)]
	for line in range(l):
		row = []
		element = x.recvline().split(" ")[:-1]
		for n in range(len(element)):
			if element[n] == "":
				continue
			if element[n] == "1":
				s_x, s_y = line, n-1
				#print(s_x, s_y-1)
			elif element[n] == "2":
				d_x, d_y = line, n-1
			if element[n] == "WW":
				row.append(Vertex(INF))
			else:
				row.append(Vertex(int(element[n])))
		array.append(row)
	#print(array[s_x][s_y].getCost())
	array[s_x][s_y].updateWeight(0)#array[s_x][s_y].getCost())
	

def dijkstra(length):
	while True:
		location = getMinistWeightXY(length)
		print(location)
		if location == (INF, INF) :
			return -1
		locVertex = array[location[0]][location[1]]
		if location == (d_x, d_y):
			return locVertex.getWeight()
		locVertex.visit()
		for xy in getNearXY(location, length):
			element = array[xy[0]][xy[1]]
			newWeight = element.getCost() + locVertex.getWeight()
			if newWeight < element.getWeight():
				element.updateWeight(newWeight)
		
def printa():
	for i in array:
		for j in i:
			print(j.getCost()),
		print("\n")
		
def main():
	p = log.progress("Do It!")
	x.sendlineafter("[SAMPLE]\n\n", "1")
	x.recvuntil("==")
	for gameRound in range(1, 31):
		p.status("Round"+str(gameRound))
		print(x.recvuntil("===\n"))
		init(19)
		printa()
		x.sendline(str(dijkstra(19)))
		
		print("??")
		


main()