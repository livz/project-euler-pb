# Project Euler problem 230

A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

len_term = 100

def fab(n):
    a = 1
    b = 1
    list_f = []
    list_f.append(1)
    list_f.append(1)
    
    while b*len_term<n:    
        tmp = a
        a = b
        b += tmp
        list_f.append(b)
        
    return list_f

def red(n):        
    list = fab(n)
    current = len(list)-2
    #print list
    
    while (n>len_term):
     #   print n, list[current]
        while (n-list[current-1]*100) <= 0 :
            current -= 2            
            
        n -= (list[current-1]*100)    
        
        current -= 1
    
    
    if ((current+1)%2 == 0):
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
    
    