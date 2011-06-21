# Project Euler problem 56

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time

def sum_dig(n):
    sum = 0
    while n>0:
        sum += n%10
        n /= 10
    return sum
    
def solve():
    max = 0
    for i in range(1, 100):
        for j in range(1, 100):
            s = sum_dig(i**j)
            if s > max:
                max = s
    print max
    
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"        