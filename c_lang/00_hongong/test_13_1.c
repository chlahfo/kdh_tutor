#include <stdio.h>
//예상 결과 30

void func(void);

int a = 10;

int main(void){
    a = 20;
    func();
    printf("%d", a);

    return 0;
}

void func(void){
    a = 30;
}