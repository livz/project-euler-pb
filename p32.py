# Project Euler problem 32

# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital.

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]

def solve():
    perm = all_perms([1,2,3,4,5,6,7,8,9])
    list_p = list(perm)    
    
    for p in list_p:
        for i in range(0,8):
            for j in range(0,8):
                if i+j<=8:
                    n1=0
                    while i>0:
                        n1 +=p
        
if __name__=="__main__":
    solve()
    