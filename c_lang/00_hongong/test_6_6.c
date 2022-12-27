#include <stdio.h>

int main(void){
    int i, j;
    for (i = 0; i < 5; i ++){
        for (j = 0; j < 5; j ++){
            if(i == j){
                printf("ㄸ");
                continue;
            }
            if(i + j == 4){
                printf("ㅂ");
                continue;
            }

            printf("  ");
        }
        printf("\n");
    }
    
    return 0;
}