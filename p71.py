# Project Euler problem 71

# By listing the set of reduced proper fractions for d<=1,000,000 in ascending order of size,
# find the numerator of the fraction immediately to the left of 3/7.

import time   

N = 1000000

def gcd(n, d):
	while d != 0:
		t = d
		d = n%d
		n = t
	return n

def solve():
	min_diff = 1
	min_x = -1
	min_y = -1

	for num in xrange(N,1,-1):
		# get the closest numerator 'x' for denominator 'num' 
		x = int(3*num/7.)
		diff = 3/7. - x/(num*1.0)
		if diff != 0 and diff<min_diff:
			min_diff = diff
			min_x = x
			min_y = num

	print min_x, min_y, min_diff

       
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
