#include <stdio.h>

char *my_strcpy(char *pd, char *ps);

int main(void){
    char str[80] = "strawberry";    

    printf("바꾸기 전 문자열: %s\n", str);
    my_strcpy(str, "apple");
    printf("바꾼 후 문자열:%s\n", str);
    return 0;
}