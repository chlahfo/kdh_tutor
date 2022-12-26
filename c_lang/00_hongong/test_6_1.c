#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int a;
    do{
        printf("a:");
        scanf("%d", &a);
    }while(a < 0);

    return 0;
}