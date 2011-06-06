/* Project Euler problem 9 */

#include <stdio.h>

int main(){
    for(long i=1; i<1000; i++){
        for(long j=i+1; j<1000; j++){
            for(long k=j+1; k<1000; k++){
                if((i*i+j*j==k*k) &&(i+j+k==1000)){
                    printf("i=%ld, j=%ld, k=%ld, p=%ld", i,j,k,i*j*k);
                    return 0;
                }
            }
        }
    }
    return 0;
}
