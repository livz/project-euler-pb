# Project Euler problem 58

# What is the side length of the square spiral for which the ratio of primes 
# along both diagonals first falls below 10%?

import math
import time

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def solve():
    prev = 1
    
    primes = 0
    total = 0
    
    i = 3
    while 1:    
        delta = (i**2 - prev **2 +1)/4
        for j in range (0,4):
            curr = i**2-j*delta
            if j != 0:
                if(is_prime(curr)):
                    primes += 1
            total +=1
            ratio = primes/(total+1.)
        if (ratio <=0.1):
            print "side length: " , i, " ratio: ", ratio
            break
        prev = i
        i += 2
        
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

