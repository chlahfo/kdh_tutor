#include <stdio.h>
#include <string.h>

int main(void){
    char str[80];
    printf("공백이 포함된 문자열 : ");
    fgets(str, sizeof(str), stdin);
    printf("입력된 문자열은 %s입니다\n", str);
    str[strlen(str)-1] = '\0';
    
    return 0;
}