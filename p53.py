# Project Euler problem 53

# How many, not necessarily distinct, values of  nCr, for 1<=n<=100, 
# are greater than one-million?

import time

facts = {}

limit = 100

def fact(n):
	rez = 1
	for i in range(1, n+1):
		rez *= i
	return rez

def build():
	facts[0] = 1

	for i in range(1, limit+1):
		facts[i] = fact(i)

def comb(n,r):
	return facts[n]/(facts[r]*facts[n-r])

def solve():
	build()
	
	count = 0

	for n in range(1, limit+1):
		for r in range(1, n+1):
			if comb(n,r)>1000000:
				count += 1
	print count			

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
