#include <stdio.h>

int main(void){
    int a = 20;
    int *pa;
    pa = &a;
    *pa = 32;
    double *test;
    printf("%d\n", a);

    //*pa = (double) a;
    //*pa = (double *)pa;
    //pa = (double *)pa;
 
    test = (double *)pa;

    printf("%lf\n", *test);
    printf("%lf\n", test);
    printf("%lf\n", *pa);
    printf("%lf\n", a);

    return 0;
}