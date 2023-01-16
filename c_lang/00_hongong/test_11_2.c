#include <stdio.h>

int main(void){
    int ch;
    printf("문자 입력 : ");
    ch = getchar();
    putchar(ch);
    printf("문자의 아스키 코드값 : %d\n", ch);
    
    return 0;
}