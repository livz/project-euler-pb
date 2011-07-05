# Project Euler problem 59

import time

def decode():
    file = open("cipher1.txt", "r")
    
    enc = []
    for line in file:  # just 1 line
        enc = [int(el) for el in line.split(',')]
    
    for i in range(97, 123): # [a-z]
        for j in range(97, 123): 
            for k in range(97, 123): 
                key = [i, j, k]                
                dec = []
                for idx in range(0, len(enc)):
                    dec.append(enc[idx]^key[idx%3])
                print key, reduce(lambda x,y: x+y,  map(lambda x: chr(x), dec)[:40])
    
    # ==> pass is 'god'
    
def solve():
    file = open("cipher1.txt", "r")
    
    key = [103, 111, 100] # 'god'
    
    enc = [int(el) for el in (file.readline()).split(',')]        
    dec = map(lambda x: x[1]^key[x[0]%3],  enumerate(enc))
    
    #print reduce(lambda x,y:x+y, map(lambda x:chr(x), dec))
    
    print reduce(lambda x,y: x+y, dec)
    
    
    
if __name__=="__main__":
    start = time.time()
    solve()
    print "Elapsed Time:", (time.time() - start), "sec"
