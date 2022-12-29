#include <stdio.h>
int main(void){
    int a = 10;
    int *p = &a;
    double *pd;

    //pd = p;
    pd = (double *)p;
    printf("%lf\n", pd);

    return 0;

    double aa = 3.4;
    double *pdpd = &aa;
    int *pipi;
    pipi = (int *) pdpd;
} 