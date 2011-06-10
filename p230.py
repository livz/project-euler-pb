# Project Euler problem 230

A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

len_term = 100

def fab(n):
    a = 1
    b = 1
    prev_a = a
    while b*len_term<n:
        prev_a = a
        tmp = a
        a = b
        b += tmp
        
    return (prev_a,a)

def red(n):
    term = 0
    
    while n>len_term:
        term += 1
        n -= (fab(n)[0]*len_term)
        
    if (term%2 == 0):
        return A[n-1]
    else:
        return B[n-1]
    
def solve():
    sum = 0
    
    for i in range(0, 18):
        x = (127+19*i)*(7**i)
        sum += (10**i) * int(red(x))
        print "%d %d" % (x, int(red(x)))
    print sum
    
if __name__=="__main__":
    solve()
    