# Project Euler problem 102

# Find the number of triangles for which the interior contains the origin.

import time

#		    		|x1  y1  1| 
# Area = abs(1/2 *  |x2  y2  1|  )
#                   |x3  y3  1|
def get_area(x1,y1,x2,y2,x3,y3):
	return abs(x1*y2+x2*y3+x3*y1-x1*y3-x3*y2-x2*y1)/2 

def check(tr):
	eps = 1

	A = get_area(tr[0], tr[1], tr[2], tr[3], tr[4], tr[5])
	a1 = get_area(0, 0, tr[2], tr[3], tr[4], tr[5])
	a2 = get_area(tr[0], tr[1], 0, 0, tr[4], tr[5])
	a3 = get_area(tr[0], tr[1], tr[2], tr[3], 0, 0)
	
	# doesn't check cases when point O is ON triangle
	print A, a1+a2+a3
	if abs(A-a1-a2-a3) <= eps: # sum of areas = big area ==> O(0,0) inside triangle
		print "inside"
		return 1
	else:
		print "outside"
		return 0

def solve():
	file = open("triangles.txt", "r")
	cnt = 0

	for line in file:
		tr = [int(c) for c in line.strip().split(',')]
		if check(tr)==1:
			cnt += 1
	print "Total inside: ", cnt

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
