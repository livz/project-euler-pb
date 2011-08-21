# Project Euler problem 70

# Find the value of n, 1<n<10^7, for which phi(n) is a permutation of n and 
# the ratio n/phi(n) produces a minimum.


import time
import math

primes = []
factors = []

# build factors list for 2<=n<=N
def gen_factors(n):
	for i in range(0,n+1):
		factors.append([])

	for p in primes:
		k = 1
		while k*p <=n:
			factors[k*p].append(p)
			k += 1

# Euler totient function
def phi(n) :
    for factor in factors[n] :
        n = n * (factor - 1) / factor
 
    return n

def check_perm(fi, nr):
	l1 = sorted([c for c in str(fi)])
	l2 = sorted([c for c in str(nr)])

	if l1 == l2:
		return True
	return False

def solve():
	N = 10**7

	# read primes < 10^7
	f = open('primes', 'r')
	for l in f.readlines():
		primes.append(int(l))
	f.close()	

	gen_factors(N)

	min_r = 100000
	min_i = 1

	for i in range(2,N+1):
		fi = phi(i)
		if check_perm(i, phi(i)):
			r = i/(fi*1.0)
			if r < min_r:
				min_r = r
				min_i = i
	print min_i

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
