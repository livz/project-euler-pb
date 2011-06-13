# Project Euler problem 40

# If dn represents the nth digit of the fractional part, find the value of the following expression:
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

def solve():
	list_d = [0]
	num = 1

	while len(list_d)<1000000+1:
		i = num
		list_tmp = []
		while i>0:
			list_tmp.append(i%10)
			i /= 10
		list.reverse(list_tmp)
		list_d += list_tmp
		num += 1

	print "Len: ", len(list_d)
	prod = 1
	for i in range (0,7):
		prod *= list_d[10**i]
	print prod

if __name__=="__main__":
	solve()
