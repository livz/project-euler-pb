# Project Euler problem 73

# How many fractions lie between 1/3 and 1/2 in the sorted set of 
# reduced proper fractions for d 12,000?

import time
import math

N = 12000

def gcd(n, d):
	while d != 0:
		t = d
		d = n%d
		n = t
	return n

def solve():
	total = 0
	for num in xrange(N,1,-1):
		# for every denominator 'num', get number of fractions in range
		# x/num > 1/3  and x/num < 1/2
		x_inf = num/3.
		x_sup = num/2.
		
		for i in range(int(math.ceil(x_inf+0.0000001)), int(math.ceil(x_sup-0.0000001))):
			if gcd(i,num) == 1:
				total += 1

	print total       

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
