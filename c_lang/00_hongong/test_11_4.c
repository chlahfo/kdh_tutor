#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int chk;
    char str;
    int num;
    int maxnum = 0;
    

    while (1){
        num = 0;
        chk = scanf("%c", &str);
        if (chk == EOF) break;
        
        while (str != '\n'){
            str = getchar();
            ++num;
        }
        if (num > maxnum){
            maxnum = num;
        }
        
    }
    
    printf("가장 긴 단어의 길이 : %d\n", maxnum);
    
    return 0;
}