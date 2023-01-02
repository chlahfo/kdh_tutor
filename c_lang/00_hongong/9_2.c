#include <stdio.h>

int main(void){
    int a;      //변수 a 선언
    int *pa;    //포인터 선언(* = 메모리 주소 저장하겠다고 선언하는거)
                //pa를 int형 변수의 주소를 저장하는데 쓸 것이다..(?)
                //[주소 위치에 있는 변수 자료형으로 a가 int 이므로 int 로 선언] 

    pa = &a;    //pa에 변수 a 의 주소값 저장(주소 연산자 사용)
    *pa = 10;   //a의 주소값으로 가서 10을 저장(* = 그쪽으로 가라.) 간접 참조 연산자(= 포인터 연산자)
                //pa ---> a (포인터 pa 는 변수 a 를 가르킨다.)

    printf("포인터로 a 값 출력 : %d\n", *pa);
    printf("변수명으로 a 값 출력: %d\n", a);

    return 0;
}