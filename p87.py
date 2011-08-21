# Project Euler problem 87

# How many numbers below fifty million can be expressed as the sum of 
# a prime square, prime cube, and prime fourth power?


import time
import math
import itertools

primes = []

LIM = 5*(10**7)

def func(e):
	return e[0]**4 + e[1]**3 + e[2]**2

def solve():
	N = 10**7

	# read primes < 10^7
	f = open('primes', 'r')
	for l in f.readlines():
		primes.append(int(l))
	f.close()	

	l4 = [p for p in primes if p <= 84]
	l3 = [p for p in primes if p <= 368]
	l2 = [p for p in primes if p <= 7071]

	ll = list(itertools.product(l4,l3,l2))
	ll = [func(e) for e in ll]
	ll = filter(lambda x: x<LIM, ll)
	print len(set(ll))


if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
