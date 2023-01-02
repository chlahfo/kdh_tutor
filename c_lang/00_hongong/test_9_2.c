#include <stdio.h>

int main(void){
    int a = 10, b = 20;
    int *pa = &a, *pb = &b, *pt;
    pt = pa;// pt --> a
    pa = pb;// pa --> b
    pb = pt;// pb --> a
    printf("%d %d\n", *pa, *pb);//20 10
    return 0;
}