# Project Euler problem 65

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

import time

def gcd(n, d):
	while d != 0:
		t = d
		d = n%d
		n = t
	return n

def sum_f((a1,b1), (a2,b2)):
	a = a1*b2+a2*b1
	b = b1*b2
	g = gcd(a,b)

	return (a/g, b/g)

def inv_f((a,b)):
	return (b,a)

# sum of digits in n (python style)
def sum_d(n):
	return sum(map(lambda x: ord(x)-ord('0'), [c for c in str(n)]))

def solve():
	v_e = []
	v_e.append(2)

	for k in range (1,33+1):
		v_e.append(1)
		v_e.append(2*k)
		v_e.append(1)

	# get kth numerator
	k = 100

	curr = (1, v_e[k-1])

	for i in xrange(k-2, 0, -1):
		curr = inv_f(sum_f((v_e[i],1),curr)) # 1/(v_e[i]+curr)

	final = sum_f((2,1), curr)
	print final
	
	print sum_d(final[0])

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
