# Project Euler problem 38

# What is the largest 1 to 9 pandigital 9-digit number that can be formed 
# as the concatenated product of an integer with (1,2, ... , n) where n  1?


def is_pandigi(n):
	list_d = []
	while n>0:
		list_d.append(n%10)
		n /= 10

	list_d.sort()
	if list_d==[1,2,3,4,5,6,7,8,9]:
		return 1
	else:
		return 0

def solve():
	limit = 987654321
	start = 2

	while start<99999:	
		n = 2
		num = int(str(start) + str(n*start))
		n += 1

		while int(str(num) + str(n*start))<limit:
			num = int(str(num) + str(n*start))
			n += 1

		if is_pandigi(num):
			print start,num

		start += 1

if __name__=="__main__":
	solve()
