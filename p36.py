# Project EUler problem 36

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_pali(n):
	if n == n[::-1]: 	#n == n reversed
		return 1
	return 0

def solve():
	sum = 0
	for i in range (1, 1000000):
		if is_pali(str(i)) and is_pali(bin(i)[2:]):
			sum += i
	print sum
	
if __name__=="__main__":
	solve()
