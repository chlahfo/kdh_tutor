#include <stdio.h>
int test1 = 200;
int test2 = 300;
int main(void){
    int a = 10, b = 20;

    printf("교환 전 a 와 b 의 값: %d, %d\n", a, b);
    {
        int temp;

        temp = a;
        a = b;
        b = temp;

        printf("블럭 안에서의 a 와 b 의 값: %d, %d\n", a, b);
    }
    printf("교환 후 a 와 b 의 값: %d, %d\n", a, b);

    return 0;
}