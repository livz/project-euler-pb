# Project Euler problem 46

from math import sqrt 

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0 :
            return 0
    return 1

def solve():
    primes = []
    
    i = 2
    while i:
        if is_prime(i): 
            primes.append(i)
        else:
            if i % 2 == 1:
                # test conjecture
                ok = 0
                for p in primes:
                    tmp = sqrt((i-p)/2)
                    if tmp == int(tmp):
                        print "%d=%d+2x%d^2" % (i, p, tmp)
                        ok = 1
                        break
                if ok == 0:
                    print i
                    break
        i += 1
        
if __name__=="__main__":
    solve()