# Project Euler problem 27

# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
#starting with n = 0.

from math import sqrt

def is_prime(n):
    for i in range (2, int(sqrt(n))+1):
        if n %i == 0:
            return 0
    return 1

def solve():
    max_num_primes = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while n*n+n*a+b>0 and is_prime(n*n+n*a+b):
                n += 1
            if n>max_num_primes:
                max_num_primes = n
                max_a = a
                max_b = b
    print "seq len %d a=%d b=%d a*b=%d" %(max_num_primes, max_a, max_b, max_a*max_b)
    
if __name__=="__main__":
    solve()