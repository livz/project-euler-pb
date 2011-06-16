# Project Euler problem 45

from math import sqrt

def is_penta(n):
    tmp = (sqrt(24*n+1)+1)/6
    
    if tmp == int(tmp):
        return 1
    return 0
    
def is_hexa(n):
    tmp = (sqrt(8*n+1)+1)/4
    
    if tmp == int(tmp):
        return 1
    return 0
    
def solve():
    i = 285 + 1
    
    while 1:
        n = i*(i+1)/2
        if is_penta(n) and is_hexa(n):
            print n
            return
        i +=1
        
if __name__=="__main__":
    solve()