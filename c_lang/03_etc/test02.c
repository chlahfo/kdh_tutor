//포인터 형변환
#include <stdio.h>

int main(void){
    int a = 20;
    int *pa;
    pa = &a;
    *pa = 32;               //a = 32
    printf("%d\n", a);

    double *test;
    test = (double *)pa;    //test 변수 안에 포인터 *pa의 주소가 담겼다. 여기서는 *pa를 double 이라고 속이는 것이다. 

    printf("%lf\n", *test);
    printf("%lf\n", test);
    printf("%d\n", *pa);
    printf("%d\n", a);

    return 0;
}