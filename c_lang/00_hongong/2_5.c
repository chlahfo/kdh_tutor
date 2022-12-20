#include <stdio.h>

int main(void){
    printf("%d\n", 12);
    printf("%d\n", 014);
    printf("%d\n", 0xc);

    printf("%o\n", 12);//12를 8진수로 출력
    printf("%x\n", 12);//12를 16진수 소문자로 출력
    printf("%X\n", 12);//12를 16진수 대분자로 출력
    
    return 0;
}