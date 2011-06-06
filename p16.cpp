/* Project Euler problem 16 */

#include <stdio.h>
#include <string.h>

#include <openssl/bn.h>
#include <openssl/crypto.h>


int pow(){
    BN_CTX *ctx = BN_CTX_new();

    BIGNUM *rez = BN_new();

    BIGNUM* two = BN_new();
    BN_dec2bn(&two, "2");

    BIGNUM* th = BN_new();
    BN_dec2bn(&th, "1000");

    BN_exp(rez, two, th, ctx);

    char *prod;
    prod = BN_bn2dec(rez);

    if (!prod) return 1;

    printf("2^1000 is: %s\n", prod);
    OPENSSL_free(prod);

    return 0;
}

int main(){
    char v[1000]="1071508607186267320948425049060001810561404811705533607443750" \
            "3883703510511249361224931983788156958581275946729175531468251871452" \
            "8569231404359845775746985748039345677748242309854210746050623711418" \
            "7795418215304647498358194126739876755916554394607706291457119647768" \
            "6542167660429831652624386837205668069376";

    //pow();
    int len = strlen(v);
    int sum=0;

    for(int i=0; i<len; i++){
        sum+=(v[i]-'0');
    }

    printf("sum:%d\n", sum);

    return 0;
}
