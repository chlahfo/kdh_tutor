#include <stdio.h>

void swap(double *pa, double *pb);
void line_up(double *maxp, double *midp, double *minp);

int main(void){ 
    double max, mid, min;
    printf("실수값 3개 입력: ");
    scanf("%lf%lf%lf", &max, &mid, &min);
    line_up(&max, &mid, &min);
    printf("정렬된 값 출력 %f, %lf, %lf\n", max, mid, min);

    return 0;
}

void swap(double *pa, double *pb){
    double temp;

    temp = *pa;
    *pa = *pb;
    *pb = temp;
}
//321
//123
//231
//132
void line_up(double *maxp, double *midp, double *minp){
    if (*minp > *maxp){
        swap(minp, maxp);
    }
    if (*midp > *maxp){
        swap(midp, maxp);
    }
    if (*minp > *midp){
        swap(minp, midp);
    }
}