#include <stdio.h>

int main(void){
    int a;
    double b;
    char c;

    printf("int 형 변수의 주소 : %p\n", &a);
    printf("double 형 변수의 주소 : %p\n", &b);
    printf("char 형 변수의 주소 : %p\n", &c);

    int sa = sizeof(a);
    int sb = sizeof(b);
    int sc = sizeof(c);

    printf("int형 변수 사이즈 : %d\n", sa);
    printf("double형 변수 사이즈 : %d\n", sb);
    printf("char형 변수 사이즈 : %d\n", sc);

    
    return 0;
}