#include <stdio.h>

int main(void){
    int res;
    char str[10];
    int a = sizeof(short);
    int b = sizeof(long);

    res = (a > b)? 1 : 0;
    res = (res == 1)? printf("short\n"):printf("long\n");
    

    return 0;
}