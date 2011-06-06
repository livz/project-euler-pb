/* Project Euler problem 14 */

/* 
 * http://oeis.org/A006877
 * http://oeis.org/A006878
 */

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

int main(int argc, char **argv) { 
    int longest = 0; 
    int terms = 0; 
    int i; 
    unsigned long j; 
    int *steps = (int*)malloc(1000001*sizeof(int));
    memset(steps, 0, 1000001*sizeof(int));

    for (i = 1; i <= 1000000; i++){ 
        j = i; 
        int this_terms = 1; 

        while (j != 1) {             
            this_terms++;

            if (j % 2 == 0) { 
                j = j / 2; 
            } 
            else { 
                j = 3 * j + 1; 
            }
            
            if((j<=1000000)&&(steps[j]!=0)){
                this_terms += steps[j]-1;
                break;
            }
        }
        
        steps[i]=this_terms;
        
        if (this_terms > terms) { 
            terms = this_terms; 
            longest = i; 
        }

    } 

    printf("longest: %d (%d)\n", longest, terms);
    
    free(steps);

    return 0; 
}
