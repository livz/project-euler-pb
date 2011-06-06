# Project Euler problem 48

# Find the last 10 digits of sum(1^1+2^2+...+n^n)


#Last X digits of n^n
def lastX(n, x):
    dig = 1
    i = n
    while(i>0):
        dig *= n        
        i -= 1
        if(dig>10**x):
            dig %= (10**x)
    return dig

def solve(n):
    sum = 0
    
    while(n>0):
        sum += lastX(n,10)
        n -= 1
    return sum
    
if __name__ == "__main__":
    rez = solve(1000)
    
    print rez
