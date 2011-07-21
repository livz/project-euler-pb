# Project Euler problem 69

# Find the value of n  1,000,000 for which n/phi(n) is a maximum.
# n/phi(n) = prod(p/(p-1)), p prime, p|n ==>
# 1) more unique divisors results in a higher value for n/phi(n)
# 2) the smaller the prime p, the higher the term
# n/phi(n) is maximum <==> n=p1*p2*...pk, 

import time
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return 0
    return 1

def solve():
	limit = 1000000

	n = 1
	p = 2
	while 1:
		if( 0 == is_prime(p)):
			p += 1
			continue
		if n * p > limit:
			print n
			break
		n *= p
		p += 1

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
