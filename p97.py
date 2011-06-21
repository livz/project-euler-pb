# Project Euler problem 97

# Find the last ten digits of 28433x2^7830457+1

import time

def solve():
    num = 2
    pow = 7830457
    
    # exponentiating by squaring
    res = 1
    while 1:
        if pow % 2 == 1:
            res *= num
            res %= 10000000000
        pow /= 2
        if pow == 0:
            break
        num *= num
    
    print (res*28433+1)% 10000000000
       
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

