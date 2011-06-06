# Project Euler problem 67
# Similar with problem 18

# Solution 1 : bottom up. Build maximum path from bottom. So initial triangle becomes:
#   3
#  7 4
# 2 4 6
#9 5 9 3
#
#     3
#   7  4
# 11 13 15
#9  5  9  3
#
#     3
#   20 19
# 11 13 15
#9  5  9  3
#
#     23
#   20 19
# 11 13 15
#9  5  9  3

# Solution 2 : top down. Build maximum path from top vertex. So initial triangle becomes:
#   3
#  7 4
# 2 4 6
#9 5 9 3
#
#     3
#   10  7
#  2  4  6
#9  5  9  3
#
#       3
#     10  7
#  12  14  13
#9    5   9   3
#
#       3
#     10  7
#  12  14  13
#21  19  23  16

#Solve using first solution 

def get_numbers():
    #lines = open("tri_small.txt", "r")    
    lines = open("tri.txt", "r")    
    
    listOfRows = []
    
    for line in lines:
        currRow = [int(x) for x in line.split()]
        listOfRows.append(currRow)
    
    return listOfRows
    
def solve():
    row_list = get_numbers()
    length = len(row_list)
    
    for i in xrange(length-2, -1, -1) :
        len_row = len(row_list[i])                   
        for j in range(0, len_row) :
            row_list[i][j] += max(row_list[i+1][j], row_list[i+1][j+1])
        
    print row_list[0]
    return 0
    
if __name__ == "__main__":
    max = solve()
