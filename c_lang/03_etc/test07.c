#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int *test1(void){
    static int a = 0;
    a++;

    printf("%d\n", a);

    return &a;
}
int main (void){
    int i ;
    int *pa;
    pa = test1();
    
    for(i = 0; i < 3; i++){
        test1();
    }
    *pa = *pa + 10;//test1함수 호출한 뒤에 연산하여 대입함
    test1();

    return 0;
}