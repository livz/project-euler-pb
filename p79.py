# Project Euler problem 79

# Given that the three characters are always asked for in order, analyse the 
# file so as to determine the shortest possible secret passcode of unknown length.

import time
import itertools

nr = []

def read_f():
    file = open("keylog.txt", "r")
    
    for line in file: 
        nr.append(int(line))

# 3-digits i matches the passcode n ?        
def match_n(i,li):       
    i3 = i%10
    i /= 10
    i2 = i%10
    i1 = i/10
    
    if i1 not in li:
        return 0
    else:
        idx_i1 = li.index(i1)
        if i2 not in li[idx_i1+1:]:
            return 0
        else:
            idx_i2 = (li[idx_i1+1:]).index(i2)
            if i3 not in li[idx_i2+1:]:
                return 0
            else:
                return 1

# suppose no repeating digits
def solve():
    read_f()
    list_d = []
    for n in nr:
        while n>0:
            if n%10 not in list_d:
                list_d.append(n%10)
            n /= 10
    
    perm = itertools.permutations(list_d)
    for p in list(perm): 
        ok = 1
        
        for i in nr:
            if match_n(i, p) == 0:
                ok = 0
                break
                
        if ok == 1:
            print reduce(lambda x,y: x*10+y, p)
            break

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"        