# Project Euler problem 51

# Find the smallest prime which, by replacing part of the number (not necessarily 
# adjacent digits) with the same digit, is part of an eight prime value family.

import math
import time

primes = {}

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def build():
	for i in range(2, 1000000):
		primes[i] = is_prime(i)

def test_nr(n):
	# how many primes can be obtained by replacing all 0's, all 1's  and all 2's
	if primes[n] == 0 :
		return 0

	list_d = []
	while n>0:
		list_d.append(n%10)
		n /= 10
	list_d.reverse()

	f_sum = lambda x,y: x*10+y
	
	max_cnt = 1

	for i in range(0,3):
		cnt_primes = 1
		for j in range(i+1, 10):
			# replace all 'i' with 'j'
			n_j=map(lambda x:x if x!=i else j, list_d)
			if n_j == list_d:
				break
			nj = reduce(f_sum, n_j)
			if primes[nj] == 1:
				cnt_primes += 1
		if cnt_primes>max_cnt:
			max_cnt = cnt_primes
	return max_cnt

def solve():
	build()

	nbr = 2

	while test_nr(nbr) < 8 :
		nbr += 1

	print nbr
	
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

