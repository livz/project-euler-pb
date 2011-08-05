# Project Euler problem 74

# How many chains, with a starting number below one million, 
# contain exactly sixty non-repeating terms?

import time
import math

f_d = {}

# stores length of chains beginning with key k
ch_len_d = {}

def build():
	for i in range(0, 10):
		f_d[i] = math.factorial(i)

def next_term(n):
	r = 0
	while n>0:
		r += f_d[n%10]
		n/=10
	return r

def len_chain(start):
	terms = {}
	
	terms[start] = 1
	next = next_term(start)	
	
	len_ch = 1

	while next not in terms:
		if next in ch_len_d:
			terms[next] = len_ch + 1
			len_ch += ch_len_d[next]
			break
		else:
			len_ch += 1
			terms[next] = len_ch
			next = next_term(next)

	for key in terms:
		if terms[key]<=terms[next]:
			ch_len_d[key] = len_ch - terms[key] + 1

	return len_ch

def solve():
	build()

	i = 0
	limit = 1000000
	cnt = 0
	
	while i<limit:
		len_c = len_chain(i)

		if len_c == 60:
			cnt += 1
				
		i += 1

	print cnt	

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
