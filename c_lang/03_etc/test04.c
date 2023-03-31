#include <stdio.h>

int main(void){
    int a, b;
    int *pa;
    b = a = 10;
    printf("%d %d", b, a);
    //b = &a;
    //printf("%d", b);
    //b = pa = &a;
    pa = &a;
    b = *pa = 30;
    printf("%d %d %p", b, a, pa);
    
    
    return 0;
}