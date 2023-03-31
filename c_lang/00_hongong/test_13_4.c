#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void input_data(int *pa, int *pb);
void swap_data(void);
void print_data(int a, int b);

int a, b;

int main(void){
    input_data(&a, &b);
    swap_data();
    print_data(a, b);

    return 0;
}

void input_data(int *pa, int *pb){
    printf("두 정수 입력(띄어쓰기 구분): ");
    
    scanf("%d", pa);
    scanf("%d", pb);
}

void swap_data(void){
    int temp = a;
    a = b;
    b = temp;
}
void print_data(int a, int b){
    printf("a is : %d\n", a);
    printf("b is : %d\n", b);
}