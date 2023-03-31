#include <stdio.h>

void swap(int *pa, int *pb);
void swap2(int a, int b);

int main(void){
    int a = 10, b = 20;
    int c = b + 1;
    swap2(a, b);
    swap2(a+1, b+1);

    printf("a: %d, b: %d\n", a, b);

    swap(&a, &b);
    a + 1;

    printf("a: %d, b: %d\n", a, b);

    return 0;
}

void swap2(int a, int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void swap(int *pa, int *pb){
    int temp;
    temp = *pa;
    *pa = *pb;
    *pb = temp;
}
