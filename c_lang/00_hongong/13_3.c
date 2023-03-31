#include <stdio.h>

void assign10(void);
void assign20(void);

int a;
int main(void){
    printf("함수 호출 전 a 값: %d\n", a);// 자동 0으로 초기화 됨.

    assign10();
    assign20();

    printf("함수 호출 후 a 값 : %d\n", a);

    return 0;
}

void assign10(void){
    a = 10;     //전역 변수의 a에 값 10을 대입하게 된 것.
}
void assign20(void){
    int a;
    a = 20;     //함수 내부에 지역 변수 a 가 있으므로 지역변수 a 에 값 20을 대입하게 된 것.
}