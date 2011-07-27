# Project Euler problem 62
# Find the smallest cube for which exactly five permutations of its digits are cube.


import time   

d_cubes = {}

def calc_key(n):
	lst = [c for c in str(n)]
	lst.sort()
	lst.reverse()

	return reduce(lambda x,y:x*10+y, map(lambda x:int(x), lst))

	
def solve():
	N = 5 # number of permutations

	for i in range(1,10000):
		key = calc_key(i**3)
		if key not in d_cubes:
			d_cubes[key] = [i**3]
		else:
			if len(d_cubes[key]) == N-1 :
				print d_cubes[key][0]  # print first permutation
				break
			else:
				d_cubes[key].append(i**3)	

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
