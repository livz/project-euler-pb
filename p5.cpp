/* Project Euler problem 5  */

#include <stdio.h>

int main(){
    unsigned int nr = 21;
    bool found = false;
    
    do{
        found = true;
        
        for(int i=2; i<=20; i++){
            if(nr%i != 0){
                found = false;
                nr++;
                break;
            }
        }
    }while(!found);
     
    printf("Nr: %d\n", nr);
    
    return 0;
}
