# Project Euler problem 39

squares = {}

def build():
	for i in range(1, 999):
		squares[i] = i**2

def num_sol(p):
	count = 0
	for i in range(1, p):
		for j in range(i, p):
			k = p-i-j			
			if (k>0) and (squares[i]+squares[j]==squares[k]):
				count += 1
	return count

def solve():
	build()

	max_sol = 0
	p = 0

	for i in range(1,1000):
		n = num_sol(i)
		if max_sol<n:
			max_sol = n
			p = i
	print p

if __name__=="__main__":
	solve()
