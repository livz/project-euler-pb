# Project Euler problem 35

# How many circular primes are there below one million?

from math import sqrt

primes = {}

def is_prime(n):
	for i in range(2, int(sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def build():
	for i in range(2, 1000001):
		primes[i] = is_prime(i)

def rotations(l):
	list_r = []
	
	for i in range(1, len(l)+1):
		list_r.append(l)
		l = l[1:] + l[:1]

	return list_r

def is_valid(n):
	list_d = []

	while n > 0 :
		list_d.append(n%10)
		n /= 10
	
	list_d.reverse()
	rot = rotations(list_d)
	
	for r in rot:
		a = reduce(lambda x,y: x*10+y, r)
		if primes[a] == 0:
			return 0
	return 1

def solve():
	build()

	count = 0
	for i in range(2, 1000001):
		if is_valid(i):
			count += 1

	print count

if __name__=="__main__":
	solve() 
