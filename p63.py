# Project Euler problem 63

# How many n-digit positive integers exist which are also an nth power?

#Sol: power - must be < 10
# base: starting from x, (with b^x <10^(x-1) ) all bases are invalid. 
#(it can't be obtained an n dig number from an n power)

import time
import math

def solve():
    cnt = 0
    for i in range (2,10):
        limit = math.ceil(math.log(10,i)/(math.log(10,i)-1))        
        cnt += (limit-1)
    print int(cnt)+1 # for 1^1
    
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
