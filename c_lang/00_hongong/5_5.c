#include <stdio.h>

int main(void){
    int a = 10, b = 20;

    if(a < 0){
        if (b > 0){
            printf("ok1\n");
        }
    }else{
        printf("ok2\n");
    }

    return 0;
}