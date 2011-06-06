/* Project Euler problem 20 */

#include <stdio.h>
#include <string.h>

#include <openssl/bn.h>
#include <openssl/crypto.h>

/* 100! */
int fact(){
    BN_CTX *ctx = BN_CTX_new();

    BIGNUM *rez = BN_new();
    BN_dec2bn(&rez, "1");

    for(int i=2; i<=100; i++){
        BIGNUM *aux = NULL;
        char buffer[20];

        sprintf(buffer, "%d", i);
        BN_dec2bn(&aux, buffer);

        BN_mul(rez, rez, aux, ctx);
    }

    char *fact;
    fact = BN_bn2dec(rez);

    if (!fact) return 1;

    printf("2^1000 is: %s\n", fact);
    OPENSSL_free(fact);

    return 0;
}

int main(){
    char v[1000]="9332621544394415268169923885626670049071596826438162146859296"
            "389521759999322991560894146397615651828625369792082722375825118521"
            "0916864000000000000000000000000";

    //fact();
    int len = strlen(v);
    int sum=0;

    for(int i=0; i<len; i++){
        sum+=(v[i]-'0');
    }

    printf("sum:%d\n", sum);

    return 0;
}
