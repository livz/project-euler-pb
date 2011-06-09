# Project Euler problem 230

A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

def fab(n):
    a = 1
    b = 1
    prev_a = a
    while b*100<n:
        prev_a = a
        tmp = a
        a = b
        b += tmp
        
    return (prev_a,a)

def red(n):
    while n>100:
        print fab(n)
        n -= (fab(n)[0]*100)
    return n
    
def solve():
    for i in range(0, 18):
        x = (127+19*i)*(7**i)
        print x
        
if __name__=="__main__":
    #solve()
    print red(360)
    