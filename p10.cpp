/* Project Euler problem 10 */

#include <stdio.h>
#include <math.h>

#include <openssl/bn.h>
#include <openssl/crypto.h>

int is_prime (int n){
    for (int z = 2; z<=sqrt(double(n)); z++){
        if( n%z == 0 )
            return 0;
    }

    return 1;
}

int main(){
    BIGNUM* sum = NULL;
    BN_dec2bn(&sum, "0");

    BN_CTX *ctx = BN_CTX_new();

    BN_init(sum);

    for(unsigned int i=2; i<2000000; i++){
        if(is_prime(i)){
            char *sum_tmp;
            sum_tmp = BN_bn2dec(sum);
            if (!sum_tmp) return 1;
            //printf("Sum tmp is: %s\n", sum_tmp);
            OPENSSL_free(sum_tmp);


            BIGNUM *aux = NULL;
            char buffer[20];

            sprintf(buffer, "%d", i);

            BN_dec2bn(&aux, buffer);

            if(!BN_add(sum, sum, aux)) {
                printf("err\n");
                return 1;
            }
        }
    }

    char *sum_out;
    sum_out = BN_bn2dec(sum);
    if (!sum_out) return 1;
    printf("Sum is: %s\n", sum_out);
    OPENSSL_free(sum_out);

    return 0;
}
