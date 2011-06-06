# Project Euler problem 22

def val(name):
    val = 0
    for i in range(0, len(name)):
        val += ord(name[i])-ord('A')+1
        
    return val
    
def solve():
    file = open("names.txt", "r")
    
    list = []
    for line in file: # file contains just 1 line
        list = line.split(',')        
    
    list_str = []
    for el in list:
        list_str.append(el.strip('"'));
        
    list_str.sort()
    
    total_sum = 0
    for i in range(0, len(list_str)):
        total_sum += (i+1)*val(list_str[i])
    
    print total_sum
    
if __name__ == "__main__":
    solve()
    
