# Project Euler problem 44

# Pentagonal numbers

from math import sqrt
   
def solve():
    limit = 3000

    penta = [ n * (3*n - 1) / 2 for n in range(1, 2*limit) ]
    penta_d = dict.fromkeys(penta)
    
    for i in range(1, limit):
        for j in range(i+1, 2*limit-1):
            p_i = penta[i]
            p_j = penta[j]
            p_sum = p_i + p_j
            p_diff = p_j - p_i
            if penta_d.has_key(p_sum) and penta_d.has_key(p_diff):
                print p_i, p_j, p_diff

if __name__=="__main__":
    solve()