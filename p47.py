# Project Euler problem 47

from math import sqrt 

primes = []

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0 :
            return 0
    return 1


def build():
    for i in range(2, 5000):
        if is_prime(i):
            primes.append(i)
        
def num_pr_fact(n):
    count = 0
    
    if not is_prime(n):
        for num in primes:
            if n%num == 0:
                count += 1
                while n%num == 0:
                    n /= num
    
    return count
    
def solve():
    build()
    
    num_fact = 4
    
    i = 14
    
    while 1:        
        while num_pr_fact(i) != num_fact :
            i += 1
        count = 0
        while num_pr_fact(i) == num_fact :
            count += 1
            i += 1
        if count == num_fact:
            print i-num_fact
            break
   
            
    
if __name__=="__main__":
    solve()
