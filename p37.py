# Project Euler problem 37

# Find the sum of the only eleven primes that are both truncatable 
# from left to right and right to left.

from math import sqrt

primes = {}

def is_prime(n):
	for i in range(2, int(sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def build():
	primes[0] = 0
	primes[1] = 0

	for i in range(2, 1000001):
		primes[i] = is_prime(i)

def is_valid(n):
	list_d = []
	while n > 0 :
		list_d.append(n%10)
		n /= 10

	list_d.reverse()
	for i in range(0, len(list_d)):
		if primes[reduce(lambda x,y: x*10+y, list_d[i:])]==0:
			return 0
	for i in range(0, len(list_d)):
		if primes[reduce(lambda x,y: x*10+y, list_d[:i+1])]==0:
			return 0
	return 1

def solve():
	build()
	i = 11
	count = 0
	sum_i = 0

	while count < 11:
		if is_valid(i):
			count += 1
			sum_i += i
			print count, i
		i += 1
	print sum_i

if __name__=="__main__":
	solve()
