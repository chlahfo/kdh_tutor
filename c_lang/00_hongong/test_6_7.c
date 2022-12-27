#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int i, j, n;
    int count = 0;
    
    printf("2 이상의 정수를 입력하세요 : ");
    scanf(" %d", &n);

    for (i = 2; i < n; i++){
        int chk = 0;
        for (j = 2; j < i; j++){
            if (i % j == 0){
                chk ++;
            }
        }

        if (chk == 0){
            printf("%d\t", i);
            count ++;

            if(count % 5 == 0){
                printf("[%d, %d]\n", count, i);
            }
        }
        
    }

    printf("\n");
    return 0;
}