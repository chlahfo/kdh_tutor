#include <stdio.h>

int main(void){
    float ft = 1.1234567890123456789;
    double db = 1.1234567890123456789;

    printf("float 형의 변수값: %.20f\n", ft);
    printf("double형의 변수값: %.20lf\n", db);

    return 0;
}