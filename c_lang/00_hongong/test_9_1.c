#include <stdio.h>

int main(void){
    char ch = 'A';
    int in = 10;
    double db = 3.4;

    char *p_ch = &ch;
    int *p_in = &in;
    double *p_db = &db;

    printf("%p\n", &ch);        //메모리 주소
    printf("%p\n", &in);        
    printf("%p\n", &db);        
    printf("%c\n", *&ch);       //메모리 주소에 간접참조 이용시 접근 가능(== *p_ch)
    printf("%d\n", *&in);
    printf("%lf\n", *&db);

    return 0;
}