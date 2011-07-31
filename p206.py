# Project Euler problem 206

# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each '_' is a single digit.

import time

def valid(n):
	s = str(n)
	
	for i in range(0,9):
		if int(s[2*i]) != i+1 :
			return 0
	if  int(s[2*9]) != 0:
		return 0
		
	return 1
	
def solve():
	# build possible terminations (last 4 digits)
	term = []
	
	for i in range(0,10):
		for j in range(0,10):
			a1 = (7*i+((7*j+4)/10))%10
			b1 = (j*j+7*j/10)%10
			
			a2 = (7*j+4)%10
			b2 = (7*j)%10
			
			if (a1+b1+7*i+(a2+b2)/10)%10==8:
				t = 1000*i+100*j+70
				term.append(t)				
				
	for i in range(0,10):
		for j in range(0,10):
			a1 = (3*i+((3*j)/10))%10
			b1 = (j*j+3*j/10)%10
			
			a2 = (3*j)%10
			b2 = (3*j)%10
			
			if (a1+b1+3*i+(a2+b2)/10)%10==8:
				t = 1000*i+100*j+30
				term.append(t)				
	
	# 
	found = 0
	for t in term:
		if found == 1:
			break
			
		print "Checking termination %d: %d " %(term.index(t), t)
		i = 10**9 + t
		
		while i<1999999999:
			sq = i**2
		
			if sq>2*(10**18):
				break
				
			if valid(sq)==1:
				print i, sq
				found = 1
				break
			i += 10000
		

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
