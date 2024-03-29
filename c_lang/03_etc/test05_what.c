#include <stdio.h>
int main(void){
    double a = 3.4;
    double *pd = &a;
    int *pi;
    pi = (int *)pd;

    printf("%p %p %lf %d", pd, pi, *pd, *pi);

    /*
        3.4는 이진법으로 바꾸면
        11.01100110011001100110011···.
        이것을 표준화 하면 
        1.1011001100110011001100110011···. x 2^1
        따라서 부호는 +, 지수는 1 , 맨 처음 1을 제외한 유효숫자는 1011001100110011001100110011...
        이것을 실수 비트열에 대입하면
        01000000 00001011 00110011 00110011 00110011 00110011 00110011 00110011
        여기서 pi 는 포인터 형 변환에 의하여 변수 a가 int형이라고 읽어들이게 된다.
        따라서 앞의 4byte 만 읽고 해당 0과 1을 이진수로 읽어들이게 된다.
        01000000 00001011 00110011 00110011(2)를 십진수로 변환시키면 
        1,074,475,827가 된다.
    */
    
    return 0;
}
