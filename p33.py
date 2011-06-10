# Project Euler problem 33

def sim(aa, bb):
    ret = (0,0)
    
    if(aa%10==bb/10):
        ret = (aa/10, bb%10)        
    if(aa/10==bb%10):
        ret = (aa%10, bb/10)
    
    return ret
    
def solve():
    A = 1
    B = 1
    for i in range (11,100):
        for j in range(i+1, 100):
            a,b = sim(i,j)
            if (a != 0) and (i*b==j*a):
                A *= i
                B *= j
                
    print "%d/%d" % (A,B)
    
if __name__=="__main__":
    solve()