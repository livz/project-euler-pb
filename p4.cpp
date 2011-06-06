/* Project Euler problem 4 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool is_pali(long n){
    char buffer[10];
    bool ret = true;
    
    sprintf(buffer, "%ld", n);
    
    for(int i=0, j=strlen(buffer)-1; i<j; i++, j--){
        if(buffer[i] != buffer[j]){
            ret = false;
            break;
        }
    }
    
    //printf("Nr: %s is %s palindrome\n", buffer, ret?"":"not");
    
    return ret;
}

int main(){
    int i=0, j=0;
    long int max_pal = 0;
    
    for(i=0; i<=999; i++) {
        for(j=0; j<=999; j++){
            long prod = i * j;
            
            if(is_pali(prod)){
                if(prod>max_pal){
                    max_pal = prod;
                }
            }
        }
    }
    
    printf("max pali: %ld\n", max_pal);
    
    return 0;
}
