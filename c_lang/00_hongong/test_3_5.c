#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    char ch;

    printf("문자 입력 :");
    scanf("%c", &ch);
    int as = ch;
    printf("%c의 아스키 코드 값은 %d입니다.\n", ch, as);

    return 0;
}
