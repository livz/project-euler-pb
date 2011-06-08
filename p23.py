# Project Euler problem 23
# Find the sum of all the positive integers which cannot be written as 
# the sum of two abundant numbers.

def sum_div_pr(n):
    sum = 0
    for i in range (1, n/2+1):
        if n%i==0:            
            sum += i    
    return sum

ab_dict = {}
    
def build_ab(limit):
    for i in range(1, limit):
        if sum_div_pr(i)>i:
            ab_dict[i] = 1
        else:
            ab_dict[i] = 0

# cannot be written as the sum of 2 abundant numbers          
def valid(n):    
    for i in range(1,n):
        j = n-i
        if ab_dict[i] and ab_dict[j] :
            return 0    
    return 1
    
if __name__ == "__main__":
    limit = 28123   
        
    sum = 0
    build_ab(limit)
    for i in range(1, limit):
        if valid(i):
            sum +=i
            
    print sum