# Project Euler problem 19

import time

def get_day(date):
    return (time.asctime(time.strptime(date, '%Y %m %d'))).split()[0]
    
def solve():
    total = 0
    for i in range(1901, 2001):
        for j in range(1, 13):            
            date_str = str(i)+' '+str(j)+' '+str(1)            
            if 'Sun' == get_day(date_str):
                #print date_str
                total += 1
            
    print total
    
if __name__ == "__main__":
    solve()
