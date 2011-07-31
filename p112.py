# Project Euler problem 112

# Find the least number for which the proportion of bouncy numbers is exactly 99%

import time

def is_bouncy(n):
	if n<100:
		return 0
		
	s = str(n)
	
	li = [c for c in s]
	orig = [c for c in li]
	
	li.sort()
	if orig == li:
		return 0
		
	li.reverse()
	if orig == li:
		return 0
		
	return 1
	
def solve():
	i = 1
	b, nb = 0, 0
	
	while 1:
		#print i
		if is_bouncy(i):
			b += 1
		else:
			nb += 1
			
		if b*100 == (b+nb)*99 : # 90%
			print i
			break
		
		i += 1
	

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
