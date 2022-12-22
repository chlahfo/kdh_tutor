#include <stdio.h>

int main(void){
    int a = 10, b = 5;
    int res;

    res = a / b * 2;//우선순위가 같으므로 왼쪽부터 차례로 연산
    printf("res = %d\n", res);

    res = ++a *3;//a 값 증가 후 *3 (a=11)
    printf("res = %d\n", res);

    res = a > b && a != 5;//a > b의 결과와 a!=5 의 결과를 && 연산 
    printf("res = %d\n", res);

    res = a % 3 == 0;//a%3 의 값이 0과 같은지 확인
    printf("res = %d\n", res);

    res = a++ *3;//a *3 후 a 값 증가(a=11 그대로)
    printf("res = %d\n", res);



    return 0;
}