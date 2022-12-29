#include <stdio.h>

void test1(int *pa);
int main(void){
    int a = 10;
    
    test1(&a);
    printf("%d\n", a);

    return 0;
}

void test1(int *pa){
    *pa = 1234;
}  