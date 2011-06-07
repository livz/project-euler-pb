# Project Euler problem 30
# Find the sum of all the numbers that can be written as the sum 
# of fifth powers of their digits.

pows = {}

def fill_v():
    for i in range(0, 10):
            pows[i]=i**5

def sum_pow(n):
    sum = 0
    while n>0:
        sum += pows[n%10]
        n /= 10
    
    return sum
    
def solve():
    fill_v()
    i = 2
    total = 0
    # 7*(9**5) has 6 digits, so no 7 or more digits number 
    # can be the sum of its fifth powers of digits
    limit = 7*(9**5)
    while i<limit:
        if i==sum_pow(i):
            total += i
            print str(i)+" sum: " + str(total)
        i += 1
        

if __name__ == "__main__":
    solve()
    