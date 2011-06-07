# Project Euler problem 28
# What is the sum of the numbers on the diagonals in a 
# 1001 by 1001 spiral matrix?

mat_s = []

#build spiral matrix
def build_mat(n):    
    for i in range (0, n+1):
        row = []
        for j in range (0,n+1):
            row.append(0)
        mat_s.append(row)
    
    #current number
    n_c = 1
    
    # current position
    i_c = n/2
    j_c = n/2
    
    # start from center,
    mat_s[i_c][j_c] = n_c    
    n_c +=1
    
    #start to right
    j_c += 1
    mat_s[i_c][j_c] = n_c
    n_c += 1
      
    while n_c<=n*n :
        # go down
        while 1:
            i_c += 1
            mat_s[i_c][j_c] = n_c
            n_c += 1
            if mat_s[i_c][j_c-1] == 0 :
                break
        
        # go left
        while 1:
            j_c -= 1
            mat_s[i_c][j_c] = n_c
            n_c += 1
            if mat_s[i_c-1][j_c] == 0 :
                break
                
        # go up
        while 1:
            i_c -= 1
            mat_s[i_c][j_c] = n_c
            n_c +=1
            if mat_s[i_c][j_c+1] == 0 :
                break
                
        # go right
        while 1:
            j_c +=1
            mat_s[i_c][j_c] = n_c
            n_c +=1
            if mat_s[i_c+1][j_c] == 0 :
                break

def sum_diag(n):            
    sum = 0
    for i in range(0, n):
        for j in range(0,n):
            if (i==j) or (i+j==n-1):
                sum += mat_s[i][j]
            
    print sum
    
if __name__ == "__main__":
    build_mat(1001)
    sum_diag(1001)
    