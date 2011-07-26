# Project Euler problem 81

# Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix
# from the top left to the bottom right by only moving right and down.

import time

N = 80

def solve():	
	lines = open("matrix.txt", "r")    
    
	matrix = []
    
	for line in lines:
		currRow = [int(x) for x in line.split(',')]
		matrix.append(currRow)

	for i in xrange(N-1,-1,-1):
		for j in xrange(i,-1,-1):
			if i==N-1 and j==N-1:
				continue
			if i==N-1:
				down = matrix[j+1][i]
				matrix[j][i] += down
			else:
				down = matrix[j+1][i]
				right = matrix[j][i+1]
				matrix[j][i] += min(down,right) 
		for j in xrange(i-1,-1,-1):
			if i==N-1:
				right = matrix[i][j+1]				
				matrix[i][j] += right
			else:
				down = matrix[i+1][j]
				right = matrix[i][j+1]
				matrix[i][j] += min(down,right)

	print matrix[0][0]

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"
