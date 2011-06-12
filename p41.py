# Project Euler problem 41
# What is the largest n-digit pandigital prime that exists? (n>1)

import math
import itertools

primes = {}

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def solve():
	# for 8,9 digits the number would be divisible by 3, so not prime
	digits = [1,2,3,4,5,6,7] 
	for i in xrange(len(digits), 5, -1):
		sub_list = digits[:i]

		perm = itertools.permutations(sub_list) # generate sorted permutations
		for p in reversed(list(perm)): # stop on first pandigital prime found 
			if is_prime(reduce(lambda x,y:x*10+y, p)):
				return reduce(lambda x,y:x*10+y, p)
			

if __name__=="__main__":
	print solve()
