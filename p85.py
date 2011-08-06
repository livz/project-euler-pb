# Project Euler problem 85

# Although there exists no rectangular grid that contains exactly two 
# million rectangles, find the area of the grid with the nearest solution. 

# http://www.gottfriedville.net/mathprob/comb-subrect.html
# (m)(m+1)/2 (n)(n+1)/2 = m(m+1)(n)(n+1)/4

import time

# holds m*(m+1)/2 
inc = []

def solve():
	N = 2000000

	min_delta, m_lim, n_lim = N, 0, 0

	inc.append(0)
	for i in range(1, 3000):
		inc.append(inc[i-1] + i)

	for i in range(1, 3000):
		for j in range(1, 3000):
			d = N-inc[i]*inc[j]
			if d>0 and d<min_delta:
				min_delta, m_lim, n_lim = d, i, j

	print min_delta, m_lim, n_lim
	print "area: ", m_lim*n_lim
	
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
