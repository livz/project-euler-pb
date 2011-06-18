# Project Euler problem 50
# Which prime, below one-million, can be written as the sum 
# of the most consecutive primes?

import math

primes = []
limit = 1000000

import time

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def build():
	# longest sequence wiht sum <100000 has length 183.
	# so it's safe to build only until limit/200 primes, if we search for a longer sequence
	for i in range(2, limit/200):
		if is_prime(i):
			primes.append(i)
	
def solve():
	build()

	max_len = 0
	start_prime = 0
	sum_seq = 0

	while len(primes)>1:		
		tmp = [i for i in primes]

		if len(primes)<max_len:
			break # can't obtain longer than current sequence 
		
		ok = 1
		for i in xrange(len(tmp)-2, -1, -1):
			tmp[i] += tmp[i+1]
			if (tmp[i] > limit):
				ok = 0
				break
		if ok == 0:
			primes.pop()
			continue

		for i in range(0, len(tmp)-1):
			if is_prime(tmp[i]) and (tmp[i]<limit):
				if len(tmp)-i>max_len: #found longer sequence
					sum_seq, start_prime, max_len = tmp[i], primes[i], len(tmp)-i
				break # break anyway			 
	
		primes.pop()

	print "longest sum: %d, starting prime=%d len=%d" % \
				(sum_seq, start_prime, max_len)
	
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
