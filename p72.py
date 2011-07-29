# Project Euler problem 72

# How many elements would be contained in the set of 
# reduced proper fractions for d<=1,000,000?


import time
import math

primes = []
factors = []

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

# build primes list
def build_primes(n):
	for i in range(2, n+1):
		if is_prime(i):
			primes.append(i)

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

def solve():
	N = 1000000

	build_primes(N)
	gen_factors(N)

	print sum(map(phi, range(2,N+1)))

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
