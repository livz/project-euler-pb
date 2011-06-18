# Project Euler problem 49

import math 

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0 :
			return 0
	return 1

def is_valid(i):
	if i+6660>9999:
		return 0

	if not is_prime(i) or not is_prime(i+3330) or not is_prime(i+6660):
		return 0

	list1 = []
	n1 = i
	while n1>0:
		list1.append(n1%10)
		n1 /= 10
	list1.sort()

	list2 = []
	n2 = i+3330
	while n2>0:
		list2.append(n2%10)
		n2 /= 10
	list2.sort()

	list3 = []
	n3 = i
	while n3>0:
		list3.append(n3%10)
		n3 /= 10
	list3.sort()

	if list1 != list2 or list1 != list3 :
		return 0

	return 1

def solve():
	
	for i in range (1000, 10000):
		if is_valid(i):
			print "%d%d%d" % (i,i+3330,i+6660)

if __name__=="__main__":
	solve()
