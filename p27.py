# Project Euler problem 27

# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
#starting with n = 0.

from math import sqrt

def is_prime(n):
    for i in range (2, int(sqrt(n))):
        if n %i == 0:
            return 0
    return 1

def solve():
    max_num_primes = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            num_primes = 0
            n = 0
            while n*n+n*a+b>0 and is_prime(n*n+n*a+b):
                n += 1
                num_primes += 1
            if a==1 and b==41:
                print num_primes
            if num_primes>max_num_primes:
                max_num_primes = num_primes
    print "seq len %d a=%d b=%d a*b=%d" %(max_num_primes, a, b, a*b)
    
if __name__=="__main__":
    solve()