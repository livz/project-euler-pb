# Project Euler problem 60

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

import time
import itertools
import math

LIM = 10000

primes_l = [] 	# primes list

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return False
	return True

def is_prime2(nr):
	for pr in primes_l:
		if pr>math.sqrt(nr):
			break
		if nr%pr == 0:
			return False

	return True

def build():
	for i in range(3, LIM):
		if is_prime(i):
			primes_l.append(i)

def solve():
	build()

	for i1 in primes_l:
		for i2 in primes_l:
			if i2<=i1:
				continue
			if not is_prime2(int(str(i1)+str(i2))) or not is_prime2(int(str(i2)+str(i1))):
				continue
			for i3 in primes_l:
				if i3<=i2:
					continue
				if (not is_prime2(int(str(i1)+str(i3))) or not is_prime2(int(str(i3)+str(i1))) or
					not is_prime2(int(str(i2)+str(i3))) or not is_prime2(int(str(i3)+str(i2)))) :
					continue
				for i4 in primes_l:
					if i4<=i3:
						continue
					if( not is_prime2(int(str(i1)+str(i4))) or not is_prime2(int(str(i4)+str(i1))) or
						 not is_prime2(int(str(i2)+str(i4))) or not is_prime2(int(str(i4)+str(i2))) or
						 not is_prime2(int(str(i3)+str(i4))) or not is_prime2(int(str(i4)+str(i3)))) :
						continue
					for i5 in primes_l:
						if i5<=i4:
							continue
						if(is_prime2(int(str(i1)+str(i5))) and is_prime2(int(str(i5)+str(i1))) and
							is_prime2(int(str(i2)+str(i5))) and is_prime2(int(str(i5)+str(i2))) and
							is_prime2(int(str(i3)+str(i5))) and is_prime2(int(str(i5)+str(i3))) and
							is_prime2(int(str(i4)+str(i5))) and is_prime2(int(str(i5)+str(i4)))):
							print i1,i2,i3,i4,i5, "sum: ", i1+i2+i3+i4+i5
							return

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
