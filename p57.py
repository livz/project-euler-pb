# Project Euler problem 57

# n0 = 1 nk=1+1/(1+nk-1)

import time

def add(F1, F2):
	return (F1[0]*F2[1]+F2[0]*F1[1], F1[1]*F2[1])

def inv(F):
	return (F[1], F[0])

def valid(F):
	if (len(str(F[0])) > len(str(F[1]))) :
		return 1
	else:
		return 0

def solve():
	limit = 1000
	
	count = 0

	curr = (1,1)
	for i in range(1,limit+1):
		curr = add((1,1), inv(add((1,1), curr)))
		if valid(curr):
			count += 1

	print "total: ", count
	
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
