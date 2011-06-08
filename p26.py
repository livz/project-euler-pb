# Project Euler problem 26
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

#1.If the fraction terminates, then at some point we get a remainder of 0 meaning that n evenly divides a power of 10. 
#Since 10 has only two divisors, 2 and 5, n evenly divides a power of 10 if and only if n = 2^ax5^b where a,b are 
#non-negative integers (a or b may be 0 in which case n is either only divisible by 2 or by 5).

#2.The fraction will recur if n does not evenly divide any power of 10.
#2.A If n is has no factors in common with 10 (abbreviated as n is coprime with 10), the length of the recurring cycle 
#is equal to the order of 10 in the group Zn (the multiplicative group of integers modulo n). 
#If 10 has order d then 10^d mod n = 1 and 1 becomes the first remainder repeated (since we start with numerator 1).

#2.B If n is not coprime with 10, there is no d for which 10^d mod n = 1. In such cases n=2^ax5^bxm where m is coprime with 10. 
#So 1/n = 1/(2ax5b) x 1/m . The component 1/(2ax5b) will terminate so the cycle that results in 1/n is contributed by 1/m and 
#the length of the cycle is equal to the order of 10 in Zm.

#length of the cycle in 1/n
def len_c(n):
    len = 0
    while n%2 == 0:
        n /= 2
    while n%5 == 0:
        n /= 5
    if n > 1:
        a = 10 % n
        len = 1
        while a != 1:
            a *= 10
            a %= n
            len += 1    
            
    return len

if __name__ == "__main__":
    len_max = 0
    d = 0    
    for i in range(1,1000):
        if len_c(i) > len_max:
            len_max = len_c(i)
            d = i
            
    print "Maximum cycle len %d for d=%d" % (len_max, d)