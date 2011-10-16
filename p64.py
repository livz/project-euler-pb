# ProjectEuler problem 64
# How many continued fractions for N  10000 have an odd period?
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

import math
import time

def periodLen(N):
	m0, d0, a0 = 0, 1, int(math.floor(math.sqrt(N)))
	li = [] 		# triplets list
	li.append((m0, d0, a0))
	
	m1 = int(d0*a0-m0)
	d1 = int((N-m1*m1)/d0)
	if d1 == 0:
		#print "period of", N, ":", 0
		return 0
	a1 = int(math.floor((int(math.floor(math.sqrt(N)))+m1)/d1))
	
	period = 0
	while (m1, d1, a1) not in li:
		#print (m1, d1, a1)
		li.append((m1, d1, a1))
		m0, d0, a0 = m1, d1, a1
		m1 = int(d0*a0-m0)
		d1 = int((N-m1*m1)/d0)
		a1 = int(math.floor((int(math.floor(math.sqrt(N)))+m1)/d1))
		period += 1
	#print "period of", N, ":", period
	return period

def solve():
	limit = 10001
	cnt = 0
	
	for i in range(2,limit):
		if periodLen(i)%2 == 1:
			cnt += 1
	print cnt
	
if __name__ == "__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

