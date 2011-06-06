# Project Euler problem 21

# returns the sum of proper divisors of n
def d(n):
    sum = 0
    for i in range(1, n/2+1):
        if(n%i == 0):
            sum += i
    return sum

def solve():
    sum = 0
    divs_sum = {}
    
    for i in range(1, 10000+1):
        divs_sum[i] = d(i)
        
    for i in range(1, 10000+1):
        for j in range(1, 10000+1):
            if(i != j) and (divs_sum[i]==j) and (divs_sum[j]==i) :
                print "pair: " + str(i) + " " + str(j)
                sum += i
    
    return sum
    
if __name__ == "__main__":
    sum = solve()
    print sum
