# Project Euler problem 99

# Using base_exp.txt, a 22K text file containing one thousand lines with a 
# base/exponent pair on each line, determine which line number has 
# the greatest numerical value.

import time   

# p1 = (base, exp)
def cmp(p1,p2):
	p_min = min(p1[1],p2[1])

	if p1[1] == p_min:
		return p1[0]/(p2[0]*1.0) > p2[0]**((p2[1]-p1[1]*1.0)/p1[1])
	else:
		return p2[0]/(p1[0]*1.0) < p1[0]**((p1[1]-p2[1]*1.0)/p2[1])
	
	 

def solve():
	file = open("base_exp.txt", "r")
	
	line_num = 1

	max_p = (519432,525806)  # first line
	max_l = 1

	for line in file:
		pi = (int(line.split(',')[0]),int(line.split(',')[1]))
		if cmp(pi, max_p):
			max_p = pi
			max_l = line_num
		line_num += 1
	print "pair: ", max_p, "in line: ", max_l
   
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
