# Project Euler problem 12
# Based on http://eulerscircus.wordpress.com/2009/06/19/problem-12-triangular-numbers/ and 
# http://numericalrecipes.wordpress.com/2009/04/09/naive-integer-factorization/ 
# with added small missing functions

from time import clock
from time import time

def factorAndSieve(n) :
    """
    Returns a list of prime factors and their power
    """
    t = clock()
    ret = []
    nn = n
    while nn % 2 == 0 : # remove 2's first, as 2 is not in sieve
        nn //= 2
        ret = add_fact(2, ret)
    maxFactor = int(nn**0.5)
    maxI = (maxFactor-3) // 2
    maxP = int(maxFactor**0.5)
    sieve = [True for j in xrange(maxI+1)]
    i = 0
    for p in xrange(3, maxP+1,2) : # we then sieve as far as needed
        if p > maxP :
            break
        i = (p-3) // 2
        if sieve[i] :
            while nn % p == 0 :
                nn //= p
                ret = add_fact(p, ret)
                maxFactor = int(nn**0.5)
                maxI = (maxFactor-3) // 2
                maxP = int(maxFactor**0.5)
            if nn == 1 :
                break
            else :
                i2 = (p*p - 3) // 2
                for k in xrange(i2, maxI+1, p) :
                    sieve[k] = False
    index = i
    for i in xrange(index, maxI+1) : # and inspect the rest of the sieve
        if i > maxI :
            break
        if sieve[i] :
            p = 2*i + 3
            while nn % p == 0 :
                nn //= p
                ret = add_fact(p, ret)
                maxFactor = int(nn**0.5)
                maxI = (maxFactor-3) // 2
                maxP = int(maxFactor**0.5)
            if nn == 1 :
                break
    if nn != 1 :
        ret = add_fact(nn, ret)

    t = clock() - t

    #print "Calculated factors of",n,"in",t,"sec."
    #print "Stopped trial division at",2*i+3,"instead of",int(n**0.5)
    
    return ret

def add_fact(fact, list):
    """
    If factor exists, increase it's power. Else add it
    """
    found = 0
    for item in list:
        if item[0] == fact:
            found = 1
            item[1] = item[1] + 1
            break
    if found == 0:
        list.append([fact,1])
    
    return list
        
def numberDivisors(f):
    """ take a factorization and return the number of divisors """
    return reduce(lambda x,y:x*y, map(lambda t:t[1]+1,f), 1)

def solve(goal):
    """ Find the first triangle number with more than 'goal' divisors

    Return the number and the time taken to find it
    Assumption: goal is a positive integer
    """
    t = time()

    # lets store some factorizations to kick things off
    factorization = { 2:[[2,1]], 3:[[3,1]], 4:[[2,2]], \
                      5:[[5,1]], 6:[[2,1],[3,1]] }

    # since goal is a positive integer, by assumption, we are looking
    # for a triangle number with >=2 divisors

    divs, n, tri, epsilon = 2, 2, 3, 0

    # loop invariant: T_n=tri has divs divisors, epsilon = 0 or 1
    # and n+epsilon is even
    while(divs <= goal):
        n, epsilon = n+1, 1-epsilon
        tri = n * (n+1) // 2
        lesser, greater = (n+epsilon)//2, n+1-epsilon
        if not (lesser in factorization):
            factorization[lesser] = factorAndSieve(lesser)
        if not (greater in factorization):
            factorization[greater] = factorAndSieve(greater)

        # concatenate the lists of factors
        combfact = factorization[lesser] + factorization[greater]

        # we know how to factor the product
        factproddict = {}
        for p,e in combfact:
            if not (p in factproddict):
                factproddict[p] = e
            else:
                factproddict[p] += e

        factorization[tri] = factproddict.items() # convert dictionary => list
        divs = numberDivisors(factorization[tri])

    t = time() - t
    return (tri,t)

 
if __name__ == "__main__":
    list = solve(100)
    print list
