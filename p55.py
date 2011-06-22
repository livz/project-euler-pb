# Project Euler problem 55

# How many Lychrel numbers are there below ten-thousand?

import time 

def is_pali(n):
    return n == int(str(n)[::-1])
   
def is_lychrel(n):
    cnt = 0
    while 1:
        cnt += 1
        if cnt>=50:
            break
        nr = int(str(n)[::-1])
        
        if is_pali(n+nr):
            return False
        n += nr    
    return True
    
def solve(): 
    print sum((1 for i in range(1,10000) if is_lychrel(i)), 0)    
    
    
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"