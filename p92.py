# Project Euler problem 92

# How many starting numbers below ten million will arrive at 89?

import time

final = {}

sums_sq = {0:0} 

limit = 10**7

def calc_sum_squares():
	i = 1;
	while i<=limit:
		if i not in sums_sq:
			sums_sq[i] = (i%10)**2 + sums_sq[i/10]
		i += 1

def next(n):
	sum = 0

	while (n>0):
		sum += (n%10)**2
		n /= 10


def solve():
	calc_sum_squares()

	curr = 1

	while(curr <= limit):
		if curr in final:
			curr += 1
			continue

		num = curr
		lst = []

		lst.append(num)
		while(num != 1) and (num != 89):
			if num in sums_sq:
				num = sums_sq[num]
			else:
				num = next(num)

			lst.append(num)

		for el in lst:
			final[el] = num
		
		curr += 1

	total = 0
	for key in final:
		if ( key<=limit ) and (final[key] == 89) :
			total += 1
	print total
		
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
