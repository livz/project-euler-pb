# Project Euler problem 43

# pandigital numbers

import itertools

f = lambda x,y : 10 *x +y

def is_valid(p):
	if (reduce(f, p[1:4]) % 2) != 0 :
		return 0
	if (reduce(f, p[2:5]) % 3) != 0 :
		return 0
	if (reduce(f, p[3:6]) % 5) != 0 :
		return 0
	if (reduce(f, p[4:7]) % 7) != 0 :
		return 0
	if (reduce(f, p[5:8]) % 11) != 0 :
		return 0
	if (reduce(f, p[6:9]) % 13) != 0 :
		return 0
	if (reduce(f, p[7:10]) % 17) != 0 :
		return 0
	return 1

def solve():
	sum_p = 0

	perm = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
	for p in list(perm):
		if is_valid(p):
			sum_p += reduce(f, p)
			print p
	print "Sum: ", sum_p

if __name__=="__main__":
	solve()
