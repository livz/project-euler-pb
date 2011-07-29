# Project Euler problem 72

# How many elements would be contained in the set of 
# reduced proper fractions for d<=1,000,000?


import time
import math

def find_factor(n) :
    for i in xrange(2, int(n**0.5 + 1)) :
        if n % i == 0 :
            return i
    return n
 
def find_factors(n) :
    factors = []
    while n != 1 :
        fac = find_factor(n)
        if fac not in factors :
            factors.append(fac)
        n /= fac
    return factors
 
def phi(n) :
    for factor in find_factors(n) :
        n = n * (factor - 1) / factor
 
    return n

# generator ... 
def relatively_prime_generator(n, a=1, b=1):
	### generates all relatively prime pairs <= n.  The larger number comes first.
	yield (a,b)
	k = 1
	while a*k+b <= n:
		for i in relatively_prime_generator(n, a*k+b, a):
			yield i
		k += 1

# find pairs ...
def find_pairs(lim):
	cnt = 0	
	a,b = 1,1
	
	stack=[(a,b)]
	while len(stack)>0:
		(a1,b1) = stack.pop()
		cnt += 1

		k = 1
		while a1*k+b1<=lim:
			print (a1*k+b1, a1)
			stack.append((a1*k+b1, a1))
			k += 1

	print "total: ", cnt-1

def solve():
	N = 1000000

	print sum(map(phi, range(2,N+1)))

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
