# Project Euler problem 76

# How many different ways can one hundred be written as a sum of at least two positive integers?

# http://en.wikipedia.org/wiki/Integer_partition

import time   

def count(value, ns):
	ways = [1]+[0]*value
 
	for n in ns:
		for i in range(n, value+1):
			ways[i] += ways[i-n]
 
	print ways[value]

def solve():
	value = 100
	S = range(1, value)

	count(value, S)

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
