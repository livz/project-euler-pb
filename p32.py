# Project Euler problem 32

# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital.

import itertools

def solve():
    perm = itertools.permutations([1,2,3,4,5,6,7,8,9])

    list_prod = []
    for p in list(perm):
        for i in range(1,9):
            for j in range(i+1,9):
                if j<=8:
                    a = reduce(lambda x,y: x*10+y, p[:i])
                    b = reduce(lambda x,y: x*10+y, p[i:j])
                    c = reduce(lambda x,y: x*10+y, p[j:9])
                    if (a*b==c):                        
                        list_prod.append(c)
    print set(list_prod)
    print reduce(lambda x,y:x+y, set(list_prod))
        
if __name__=="__main__":
    solve()
    