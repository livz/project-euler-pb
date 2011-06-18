# Project Euler problem 52

# Find the smallest positive integer, x, such that 
# 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time

def is_valid(n):
	list_d = []

	tmp = n
	while tmp>0:
		list_d.append(tmp%10)
		tmp /= 10
	list_d.sort()

	for i in range(2,7):
		tmp = i*n
		list_tmp = []
		while tmp>0:
			list_tmp.append(tmp%10)
			tmp /= 10
		list_tmp.sort()
		if list_d != list_tmp:
			return 0
	return 1

def solve():
	i = 1
	while not is_valid(i):
		i+=1
	print i
	
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
