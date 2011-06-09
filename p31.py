# Project Euler problem 31

# How many different ways can 2 pounds be made using any number of coins?

cents = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
names = {200: "2P", 100: "1P", 50 : "50p", 20 : "20p", 10: "10p", 5:"5p", 2:"2p", 1:"1p"}

def count_combs(left, i, comb, add):
    if add: 
        comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append( (left, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        print " ".join("%d %s" % (n,names[c]) for (n,c) in comb)
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(left/cur)+1))

if __name__=="__main__":    
    print count_combs(cents, 0, [], None)
    
    

