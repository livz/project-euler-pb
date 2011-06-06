/* Project Euler problem 2 */
#include <stdio.h>

int main() {
    unsigned int a = 1, b = 2;
    unsigned int tmp;
    unsigned int sum = 2;
    
    while(b<=4000000){
        tmp = b;
        b = a + b;
        a = tmp;
        printf("%d ", b);
        if(b % 2 == 0) sum +=b;
    }
    printf("\nSum:%d\n", sum);
    
    return 0;
}
