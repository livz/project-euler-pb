# Project Euler problem 34

# Find the sum of all numbers which are equal to the sum of the factorial 
# of their digits.

fact_d = {}

def fact(n):
	f = 1
	for i in range(1,n+1):
		f *= i
	return f

def build():
	for i in range(0,10):
		fact_d[i] = fact(i)

def valid(n):
	tmp = n
	s = 0
	while (n>0):
		s += fact_d[n%10]
		n /= 10

	if tmp == s :
		return 1
	else:
		return 0 

def solve():
	build()
	i = 10
	# 7 * 9! < 9999999
	limit = 9999999
	sum = 0
	while (i<limit):
		if valid(i):
			sum += i		
			print  "i:%d sum:%d" % (i, sum)
		i += 1

if __name__=="__main__":
	solve()

